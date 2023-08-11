import os
import subprocess
chapter='第八章 掌握主要的 NLP 任务'
# Specify the source and destination folders
source_folder = f'Course\publish/{chapter}'
destination_folder = 'Course\docx_output'

# Specify the path to the filter and the reference doc
filter_path = './utils/tip_filter.py'
reference_doc = './utils/reference.docx'
resource_folder=source_folder+'/assets'
# Iterate over all markdown files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.mdx'):
        # Construct the full paths to the source file and the output file
        source_file = os.path.join(source_folder, filename)
        output_file = os.path.join(destination_folder, chapter+'-'+filename.replace('.md', '.doc'))
        
        # Construct the pandoc command
        cmd = [
            'pandoc', '-s', source_file,
            '--filter', filter_path,
            '-o', output_file,
            '--reference-doc', reference_doc,
            "--resource-path", source_folder,
            "--highlight-style","pygments"
        ]

        # Execute the pandoc command
        subprocess.run(cmd)
