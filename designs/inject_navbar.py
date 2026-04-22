import os
import re

base_dir = '/home/mehulc07/Company/Bugle/Taigus_IML-Solutions/designs'

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    favicon_tag = '<link rel="icon" type="image/svg+xml"\n        href="https://favicons.teamtailor-cdn.com/icon?size=80..120..200&url=https%3a%2f%2ftaigus.in%2f">'
    
    if 'rel="icon"' in content:
        content = re.sub(r'<link[^>]*rel="icon"[^>]*>', favicon_tag, content)
    else:
        # Insert before </head> if it exists
        if '</head>' in content:
            content = re.sub(r'(</head>)', r'    ' + favicon_tag + '\n\1', content)

    with open(filepath, 'w') as f:
        f.write(content)

# Process all html files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("All files processed for favicon injection.")
