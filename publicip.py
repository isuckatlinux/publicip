#!/usr/bin/env python3
import json
import requests
r = requests.get('https://ipinfo.io/')
js = json.loads(r.text)
print(js)

