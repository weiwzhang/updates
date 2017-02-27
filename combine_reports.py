"""
usage: combine_reports.py 'student name' file1 file2 file3
"""

import sys

student = sys.argv[1]
files = sys.argv[2:]

print('# Report for {}\n'.format(student))
print('*This report combines {} individual submissions.*\n'.format(len(files)))

out = []
for filename in files:
    with open(filename) as f:
        out.append(f.read())

print('\n\n<hr/>\n\n'.join(out))
