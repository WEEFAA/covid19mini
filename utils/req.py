from requests import request
from tkinter import Label
import os

covi_19_api_url = "https://covid-19-tracking.p.rapidapi.com/v1/"

# I'm supplying my dummy account api key here
# get yours here = https://rapidapi.com/slotixsro-slotixsro-default/api/covid-19-tracking
os.environ['covid19key_key'] = "fe52edfd5emsha37d6405164886ap13df09jsnf99c470513c2" # set your key here or set it manually on the command line

request_headers = {
    'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
    'x-rapidapi-key': os.getenv('covid19key_key') 
}

def request_api(country = ""): 
	response = request("GET", f'{covi_19_api_url}{country}', headers=request_headers)
	if response.status_code == 200:
		return {
			"success": True,
			"data": response.json(),
			"response": response
		}
	else:
		return {
			"success": False,
			"data": {},
			'response': response
		}
