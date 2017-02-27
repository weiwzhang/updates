import glob
from collections import defaultdict


all_files = glob.glob('**/*.md', recursive=True)
all_files = [f for f in all_files if not ('README' in f or 'admin' in f)]

reports = defaultdict(list)
for f in all_files:
    _, project, person = f.split('/')
    reports[project].append(person.replace('.md', ''))

print('# Machine Shop Semester Reports')

for project in sorted(reports):
    print('\n## {}\n'.format(project))

    for student in sorted(reports[project]):
        print('- [{}](updates/{}/{})'.format(
            student, project, student + '.md'
            ))
