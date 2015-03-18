# ERC Starting Grant Template
*by Tilman Birnstiel*

This repository contains a template for an ERC starting grant proposal, based on the 2015 call for proposals. Included are:

- the template `tex`-files for Part B1 and Part B2 of the proposal including some auxiliary files (bibliography files, header, ...).
- the template commitment letter for the host institution.
- a python script that builds the publication list based on [NASA ADS](http://adsabs.harvard.edu) bibcodes (so it will mostly work for astronomers). To make it work, add in the bib codes for all the papers you want to list, put in the last names of yourself (in order to bold-face your name) and of your PhD advisor (to highlight which publications are with or without the advisor) and finally also add the bibcodes of the papers you want to highlight.
- A makefile that should compile everything and provides some more functionality like translating the summary to a plain txt file and counting words.

# Disclaimer

These templates are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of merchantability or fitness for a particular purpose. Use at own risk and make sure that you follow all the guidelines of future ERC calls, which might look different than this template.