#!/usr/bin/env python3
import re

with open('/Users/zachheaton/Desktop/work/geofeed/crap_format.txt', 'r') as file:
    lines = file.readlines()
    formatted_lines = []
    for line in lines:
        components = re.split(r'\s{2,}', line.strip())

        ip_network = components[0]
        location_info = components[1].split(', ')

        reformatted_line = ','.join([ip_network] + location_info)

        reformatted_line = reformatted_line + ','

        formatted_lines.append(reformatted_line)

for line in formatted_lines:
    print(line)
