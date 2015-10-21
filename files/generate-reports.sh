#!/bin/bash

#Author: Nick Balkissoon
#Email: nbalkiss@redhat.com

#First Argument: username
#Second Argument: password
#Third Argument: application name

#This script downloads all reports for a given application name in JSON format and places those
#reports in ~/reports/  

cd ~/nexus/sonatype-work/clm-server/report
rm -rf ~/reports
mkdir ~/reports

for d in */ ; do
    cd $d
    for r in */; do
		curl -u $1:$2 -X GET "http://localhost:8070/api/v1/applications/$3/reports/$r" >> ~/reports/${r%?}.json
    done
done
