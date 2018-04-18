import http.client
import json
from secrets import *

#######################################################################################

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': FOOTDATA_TOKEN , 'X-Response-Control': 'minified' }

#######################################################################################


connection.request('GET', '/v1/competitions/', None, headers )
response = json.loads(connection.getresponse().read().decode())

print (response, end='\n')