#!/usr/bin/env python3

import requests
import sys

html_ = requests.get('https://projecteuler.net/problem=13').content.decode('utf-8')

START = '''<div style='font-family:courier new;font-size:10pt;text-align:center;'>'''
END = '''</div>'''

start = html_.find(START)
end = html_.find(END, start)
numbers = html_[start+len(START):end].replace('<br />', '').strip()
    
with open(sys.argv[1], 'w') as f:
    f.write(numbers)
