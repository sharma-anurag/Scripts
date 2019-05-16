#!/usr/bin/env python

import requests
import json
import sys
import os

nr_url = "https://api.newrelic.com/v2/applications.json"

res = requests.get(nr_url, headers={"X-Api-Key":"Your-New-Relic-Account-API-Key"})
app_json = json.loads(res.content)

i = 0
for task in app_json["applications"][:-1]:
    if task["health_status"] == "unknown":
        print task["name"]
    i += 1
