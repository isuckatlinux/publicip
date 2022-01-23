#!/usr/bin/env python3
import json
import requests
r = requests.get('https://ipinfo.io/')
js = json.loads(r.text)
print(f"Public IP -> {js['ip']}\n"
      f"HostName -> {js['hostname']}\n"
      f"Country, Region, City -> {js['country']}{js['region']}{js['city']}\n"
      f"Location -> {js['loc']}\n"
      f"Organization -> {js['org']}\n"
      f"Postal -> {js['postal']}\n"
      f"Timezone -> {js['timezone']}")


