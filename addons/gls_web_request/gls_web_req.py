import urllib2
from xml.etree.ElementTree import fromstring

host = 'http://www.gls.dk'
street = 'Ouwegemsesteenweg'
zipcode = '9870'
amount='100'

get_url = '/webservices/wsPakkeshop.asmx/SearchNearestParcelShops?street='+street+'&zipcode='+zipcode+'&Amount='+amount
url =host+get_url

xml_str = urllib2.urlopen(url).read()
tree = fromstring(xml_str)

result=[]
for node in tree.iter('{http://gls.dk/webservices/}PakkeshopData'):
	result.append({'Number':node[0].text,
			'CompanyName':node[1].text,
			'Streetname':node[2].text,
			'Streetname2':node[3].text,
			'ZipCode':node[4].text,
			'CityName':node[5].text,
			'CountryCode':node[6].text,
			'CountryCodeISO3166A2':node[7].text,
			'Telephone':node[8].text,
			'Longitude':node[9].text,
			'Latitude':node[10].text,})
print "----List of Nearby ParcelShops----"
print "\n"

print result
