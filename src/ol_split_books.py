#!/usr/bin/env python

import sys
import unicodedata
import json

letter = sys.argv[1]

for line in sys.stdin:
	line = line.strip()
	try:
		jsonStr = line
		data = json.loads(jsonStr)
		title = data["title"].encode('UTF-8')
		if( title[0:1].lower() == letter):
			print jsonStr.encode('UTF-8')
	except:
		continue
							
