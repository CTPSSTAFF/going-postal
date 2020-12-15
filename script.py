from bs4 import BeautifulSoup

# Replace XXX with path to directory containing HTML file.
root = r'XXX/'
# Replace YYY with name of HTML saved after running USPS Find USPS Locations page.
fn = 'YYYY.html'
full_fn = root + fn
fp = open(full_fn)
html = fp.read()
soup = BeautifulSoup(html)
results = soup.findAll("p", class_="address")
for r in results:
	# Grab the post office address
	the_address = r.contents[0]
	# Grab the post office name
	prev_sib = r.find_previous_sibling()
	# Filter out those pesky "Special hours are currently in effect..." records.
	if prev_sib != None:
		po_name = prev_sib.find("strong").contents[0]
		# Here: compose a string consisting of:
		#	  1. the PO name
		#	  2. a comma
		#	  3. the PO's address
		# and print it out
		outstr = po_name + ',' + the_address
		print(outstr)
	# end_if
# end_for