import os

filepath = '/home/mehulc07/Company/Bugle/Taigus_IML-Solutions/designs/navbar.html'

with open(filepath, 'r') as f:
    content = f.read()

# Replace hex colors with Tailwind theme colors
content = content.replace('text-[#003087]', 'text-primary')
content = content.replace('hover:text-[#003087]', 'hover:text-primary')
content = content.replace('border-[#003087]', 'border-primary')
content = content.replace('hover:border-[#003087]', 'hover:border-primary')
content = content.replace('bg-[#003087]', 'bg-primary')
content = content.replace('group-hover:text-[#003087]', 'group-hover:text-primary')
content = content.replace('#003087', '#9d4223') # For CSS hardcoded

# Replace light blue
content = content.replace('bg-[#dbe1ff]', 'bg-primary-container')

# Replace teal colors with primary
content = content.replace('bg-teal-600', 'bg-primary')
content = content.replace('hover:bg-teal-700', 'hover:bg-[#7e2b0d]')
content = content.replace('text-teal-600', 'text-primary')
content = content.replace('text-teal-500', 'text-primary')

# "Request a Quote" button
content = content.replace('bg-primary text-white px-6 py-2.5 text-sm font-bold rounded-lg', 'primary-gradient text-white px-6 py-2.5 text-sm font-bold rounded-full')

# Add primary-gradient style if not exists
style_to_add = """
        .primary-gradient {
            background: linear-gradient(45deg, #9d4223, #f4845f);
        }
"""
if '.primary-gradient' not in content:
    content = content.replace('</style>', style_to_add + '    </style>')

with open(filepath, 'w') as f:
    f.write(content)
print("Color updated in navbar.html")
