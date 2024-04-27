#!/usr/bin/env python3
import re

# with open('/Users/zachheaton/Desktop/work/geofeed/crap_format.txt', 'r') as file:
#     lines = file.readlines()
#     formatted_lines = []
#     for line in lines:
#         components = re.split(r'\s{2,}', line.strip())

#         ip_network = components[0]
#         location_info = components[1].split(', ')

#         reformatted_line = ','.join([ip_network] + location_info)

#         reformatted_line = reformatted_line + ','

#         formatted_lines.append(reformatted_line)

# for line in formatted_lines:
#     print(line)


formatted_lines = []

with open('/Users/zachheaton/Desktop/work/geofeed/crap_format.txt', 'r') as file:
    for line_number, line in enumerate(file, start=1):
        # Split line into IP network and location info
        ip_network, location_info = line.strip().split('\t')

        # Remove leading and trailing whitespace from location info components
        location_info = [info.strip() for info in location_info.split(',')]

        # Join IP network and location info with commas
        reformatted_line = f"{ip_network},{','.join(location_info)},"

        # Append the formatted line to the list
        formatted_lines.append(reformatted_line)

# Print formatted lines
for line in formatted_lines:
    print(line)
