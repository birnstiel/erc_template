#!/usr/bin/env python
"""
Takes a list of bibcodes and gets the ADS data in a latex list of items and writes it out to a file.

You can get all your bibcodes by going to this URL:

	http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?author=Birnstiel,+T.&jou_pick=NO&data_type=Custom&sort=NDATE&format=%5C%25R
	
where you replace Birnstiel with your last name and T. with your initial.
	
select those bibcodes you want and copy them into the array below.

Set your last name and your advisors last name below
"""
lastname='Birnstiel'
advisor='Dullemond'
import re
in_press = [
'2014arXiv1402.1354T']

in_press_text = [
r'accepted chapter in \\textit{Protostars \& Planets VI}, Arizona University Press,']

published = [
'2015A&A...573A..19S',
'2015A&A...573A...9P',
'2014ApJ...791L...6W',
'2014ApJ...787..148A',
'2014A&A...564A..51P'
'2014ApJ...780..153B',
'2013A&A...560A.111D',
'2013Sci...340.1199V',
'2013A&A...554A..95P',
'2013ApJ...766....8A',
'2013A&A...550L...8B',
'2012A&A...548C...1W',
'2012A&A...545A..81P',
'2012A&A...544L..16W',
'2012A&A...544A..79B',
'2012A&A...540A..73W',
'2012A&A...539A.148B',
'2012A&A...538A.114P',
'2012ApJ...744..162A',
'2011ApJ...739L...8R',
'2011PhDT.......279B',
'2011ApJ...727...76V',
'2011A&A...525A..11B',
'2010A&A...516L..14B',
'2010A&A...513A..79B',
'2009A&A...503L...5B ']

highlights = [
'2014arXiv1402.1354T',
'2013Sci...340.1199V',
'2012A&A...545A..81P',
#'2012A&A...544L..16W',
'2010A&A...516L..14B',
'2010A&A...513A..79B']

bibcodes = in_press + published

import urllib2
FILE = 'pub_list.tex'
format = '\\\\item %\\13M: \\\\textit{%\\t}, %\\j (%\\Y) vol. %\\V, %\\p%-\\P\\. [%\c citations]'
bib_split = '\r\n'
URL  = r'http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?db_key=ALL&warnings=YES&version=1&bibcode=%s&nr_to_return=1000&start_nr=1&data_type=Custom&sort=NDATE&format=%s'%(urllib2.quote(bib_split.join(bibcodes)),urllib2.quote(format))
#
# get the data
#
response = urllib2.urlopen(URL)
html = response.read()
response.close()
#
# split in lines
#
html = html.split('\n')
#
# cut the header
#
while '\item' not in html[0]: del html[0]
while '' in html: html.remove('')
pubs = []
pub  = []
for j,i in enumerate(html):
    if '\\item' in i:
		#
		# when a new publication starts
		#
        pubs+= [pub]
        pub  = [i]
    else:
		#
		# else: keep adding the line
		#
        pub += [i]
    #
    # add the last one
    #
    if j==len(html)-1: pubs += [pub]
#
#
#
# remove empty entries
#
while [] in pubs: pubs.remove([])
#
# find the highlighted indices
#
index_highlights = [bibcodes.index(entry) for entry in highlights]
#
# find the in-press indices
#
index_inpress = [bibcodes.index(entry) for entry in in_press]
#
# write results
#
f = open(FILE,'w')
# write header if necessary
for ipub,pub in enumerate(pubs):
    line = ''.join(pub)
    line = line.replace('&','\&')
    line = line.replace('[1 citations]','[1 citation]')
    line = line.replace(lastname,'\\textbf{'+lastname+'}')
    #
    # write line ending if necessary
    #
    ending = '\n'
    if 'Thesis' in line: line=line.replace(' vol.  ','')
    #
    # make open/closed symbols depending on advisor
    #
    if advisor in line:
        line=line.replace('\\item','\\item[$\\circ$]')
    else:
        line=line.replace('\\item','\\item[$\\bullet$]')
    #
    # switch to star for highlighted papers
    #
    if ipub in index_highlights:
    	line=line.replace('\\circ','\\ostar')
    	line=line.replace('\\bullet','\\fstar')
    #
    # modify articles in-press
    #
    if ipub in index_inpress:
    	idx = in_press.index(bibcodes[ipub])
    	line = re.sub(r'\([0-9]{4}\) vol. ', in_press_text[idx], line)
    f.write(line+ending)
# write fooder if necessary, then close
f.close()
