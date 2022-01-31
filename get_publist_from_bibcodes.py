#!/usr/bin/env python
"""
Takes a list of bibcodes & creates a latex publication list from the ADS data.

You can get all your bibcodes by going to this URL:

http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?author=Birnstiel,+T.&jou_pick=NO&data_type=Custom&sort=NDATE&format=%5C%25R

where you replace Birnstiel with your last name and T. with your initial.

Select the bibcodes you want and provide them in a text file, one bibkey per
line. By setting the supervisor, the bullets highlight supervisor contributions.
By setting the author, that author will be typeset in bold face. The -c option
adds the citation count to each output, this will take a little longer to get
from the ADS database.
"""
import ads
import os
import argparse

RTHF = argparse.RawTextHelpFormatter
PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=RTHF)
PARSER.add_argument('bibfile', help='file containing the bib codes', type=str, default='bibcodes.txt')
PARSER.add_argument('-m', '--mark-highlights', help='file containing bib codes to highlight', type=str, default=None)
PARSER.add_argument('-c', '--citations', help='also add number of citations', action='store_true')
PARSER.add_argument('-a', '--author', help='highlight author and override -n up that author', type=str)
PARSER.add_argument('-s', '--supervisor', help='highlight supervisor', type=str)
PARSER.add_argument('-o', '--outfile', help='output file. Will be overwritten if it exists', type=str)
PARSER.add_argument('-n', '--author-number', help='after how many authors to cut with "et al.".', type=str)
ARGS = PARSER.parse_args()
#
# get the bibcodes
#
with open(ARGS.bibfile) as f:
    bibcodes = [line.strip() for line in f]
#
# get bibcodes of those papers you want to highlight in the list
#
highlights = []
if ARGS.mark_highlights:
    with open(ARGS.mark_highlights) as f:
        highlights = [line.strip() for line in f]
#
# get the bibliography data
#
articles = [list(ads.SearchQuery(
    bibcode=bibcode,
    fl=['author', 'first_author', 'bibcode', 'id', 'year', 'title', 'citation_count', 'pub', 'bibtex', 'page', 'volume'],
))[0] for bibcode in bibcodes]

#
# write results
#
if ARGS.outfile is None:
    overwrite = False
    file_name = 'pub_list.tex'
    if os.path.exists(file_name):
        raise FileExistsError('Output file exists, use -o option to overwrite file!')
else:
    overwrite = True
    file_name = ARGS.outfile


with open(file_name, 'w') as f:

    for bibcode, article in zip(bibcodes, articles):
        values = {}
        if 'pub' not in article.keys():
            values['pub'] = ''
        else:
            values['pub'] = article.pub

        # full author list: get only the last names
        authors = [author.split(",")[0] for author in article.author]
        all_authors = authors.copy()

        if ARGS.author is not None and ARGS.author in authors:
            author_idx = authors.index(ARGS.author)
            authors[author_idx] = '\\textbf{{{}}}'.format(ARGS.author)
        else:
            author_idx = None

        values['author'] = ', '.join(authors)

        if ARGS.author_number is not None:

            # limit numbers of authors to be written
            # if author highlighting is on, then go up to that author

            n = int(ARGS.author_number)
            if ARGS.author is not None and author_idx is not None:
                n = max(n, author_idx + 1)

            if n < len(authors):
                values['author'] = ', '.join(authors[:n]) + ' et al.'

        values['year'] = article.year
        values['volume'] = article.volume
        values['page'] = article.page[0]
        values['title'] = article.title[0]

        if 'volume' not in article.keys() or article.volume is None:
            line = '\\item {author}: \\textit{{{title}}}, {pub} ({year}), {page}'.format(**values)
        else:
            line = '\\item {author}: \\textit{{{title}}}, {pub} ({year}), vol. {volume}, {page}'.format(**values)

        if ARGS.citations:
            line += ' [{} citation{}]'.format(article.citation_count, 's' * int(article.citation_count != 1))

        # some fixes

        line = line.replace('&', '\\&')

        if 'Thesis' in line:
            line = line.replace(' vol.  ', '')

        # line = line.replace(r'\textbackslash ', '\\')
        # line = line.replace(r'ensuremath ', '\\')
        line = line.replace('μ', r'$\mu$')
        #
        # make open/closed symbols depending on advisor
        #
        if ARGS.supervisor is not None and ARGS.supervisor in all_authors:
            line = line.replace('\\item', '\\item[$\\circ$]')
        else:
            line = line.replace('\\item', '\\item[$\\bullet$]')
        #
        # switch to star for highlighted papers
        #
        if bibcode in highlights:
            line = line.replace('\\circ', '\\ostar')
            line = line.replace('\\bullet', '\\fstar')

        f.write(line + '\n')
