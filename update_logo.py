import os

files = [
    r"c:\Users\Prasad\Desktop\Tech-Website\index.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if 'image/svg+xml' in line and ('logo1.png' in line or 'logo.png' in line):
            continue  # Remove the incorrect SVG MIME type line completely
        
        # Add cache buster ?v=2 to favicon links to force browser reload
        if 'rel="icon"' in line or 'rel="apple-touch-icon"' in line or 'rel="shortcut icon"' in line:
            line = line.replace('href="logo1.png"', 'href="logo1.png?v=2"')
            
        new_lines.append(line)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Favicons cache-busted and fixed")
