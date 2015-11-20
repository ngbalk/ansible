import requests, json, time

authenticationUrl="http://10.3.8.223:8080/j_spring_security_check"

reportsUrl = 'http://10.3.8.223:8080/api/vulnerability-update-reports'

credentials = {'j_username':'sysadmin', 'j_password':'blackduck'}

payload = json.dumps({"endDate": "2015-11-19T21:08:15.293Z","startDate": "2015-11-19T21:08:15.293Z"})

print payload
session = requests.Session()

authResponse = session.post(authenticationUrl, data=credentials)

createReportsResponse = session.post(reportsUrl, data=payload, headers={'Content-Type': 'application/json'})
reportsJson = json.loads(session.get(createReportsResponse.headers["location"]).text)


for link in reportsJson["_meta"]["links"]:
	if(link["rel"]=="content"):
		while("errorMessage" in json.loads(session.get(link["href"]).text)):
			print "report not generated... waiting 5 seconds"
			time.sleep(5)
		reportData = json.loads(session.get(link["href"]).text)
		print reportData



