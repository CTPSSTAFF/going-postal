# going-postal

This repository illustrates how to extract the names and addresss of post offices
from the HTML "blob" returned by running the 
USPS's [Find USPS Locations](https://tools.usps.com/find-location.htm) website.

The extraction is performed by the Python script _script.py_ using version 4 of the 
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library.
A sample HTML "blob" used to develop and test the script is found in query_page_1.html.

The extraction code relies upon the structure of the HTML returned by the 
_Find USPS Locations_ page __as of 14 December 2020__. Changes to the structure
of the HTML returned by the USPS's Find USPS Locations page will likely render
the extraction logic invalid, and in need of being rewritten. _Caveat emptor._

## Colophon
Author: Ben Krepp (bkrepp@ctps.org)
Last revision 15 December 2020
Location: Cyberspace
