import os
import re

input_file = 'Work/Activity 2. Scientific Intelligence Report.md'
output_dir = '06 - Scientific Intelligence Report'
os.makedirs(output_dir, exist_ok=True)

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

files = [
    {'name': '01 - Research Problem & Questions.md', 'start': '## 1. Research Problem Summary', 'end': '## 4. Scientific Search Strategy'},
    {'name': '02 - Scientific Search Strategy & Selection.md', 'start': '## 4. Scientific Search Strategy', 'end': '## 6. Scientific Evidence Matrix'},
    {'name': '03 - Scientific Evidence & Methodological Comparison.md', 'start': '## 6. Scientific Evidence Matrix', 'end': '## 9. Thematic Literature Map'},
    {'name': '04 - Thematic Literature Map & Evolution.md', 'start': '## 9. Thematic Literature Map', 'end': '## 12. Science-Technology Connection'},
    {'name': '05 - Science-Technology Connection & Gap Analysis.md', 'start': '## 12. Science-Technology Connection', 'end': '## 18. Scientific Foundation and Preliminary Hypothesis'},
    {'name': '06 - Scientific Foundation & Hypothesis.md', 'start': '## 18. Scientific Foundation and Preliminary Hypothesis', 'end': None}
]

for file_info in files:
    start_idx = content.find(file_info['start'])
    end_idx = content.find(file_info['end']) if file_info['end'] else len(content)
    
    if start_idx != -1:
        file_content = content[start_idx:end_idx].strip()
        
        title = file_info['name'].replace('.md', '').split(' - ')[1]
        frontmatter = f'---\\ntitle: \"{title}\"\\nproject: \"TERRA-FIRE\"\\ntags:\\n  - scientific-intelligence\\n  - terra-fire\\n---\\n\\n'
        
        output_path = os.path.join(output_dir, file_info['name'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + file_content + '\\n')

print('Files created successfully.')
