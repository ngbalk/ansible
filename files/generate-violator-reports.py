import json
import os

policiesAsString = os.popen('curl -u admin:admin123 -X GET http://10.3.10.0:8070/api/v2/policies').read()
policiesAsJSON = json.loads(policiesAsString)
for policy in policiesAsJSON['policies']:
	print os.popen('curl -u admin:admin123 -X GET http://localhost:8070/api/v2/policyViolations?p='+policy[id])
