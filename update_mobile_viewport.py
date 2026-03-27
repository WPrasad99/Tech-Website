import os

files = [
    r"c:\Users\Prasad\Desktop\Tech-Website\index.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
]

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Disable zoom to prevent the "cut off" zooming issue seen in the screenshot
    old_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    new_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">'
    content = content.replace(old_meta, new_meta)

    # Force strict html and body overflow rules
    old_body_css = '''        body {
            font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
            background-color: #f8fafc;
            /* Slate 50 (Light Mode Background) */
            color: #1e293b;
            /* Slate 800 for text */
        }'''
    
    new_body_css = '''        html, body {
            overflow-x: hidden;
            width: 100%;
            max-width: 100vw;
            position: relative;
        }

        body {
            font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
            background-color: #f8fafc;
            /* Slate 50 (Light Mode Background) */
            color: #1e293b;
            /* Slate 800 for text */
        }'''
    if old_body_css in content:
        content = content.replace(old_body_css, new_body_css)
        
    old_body_css2 = '''        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #ffffff;
            color: #1e293b;
            overflow-x: hidden;
        }'''
    new_body_css2 = '''        html, body {
            overflow-x: hidden;
            width: 100%;
            max-width: 100%;
            position: relative;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #ffffff;
            color: #1e293b;
        }'''
    if old_body_css2 in content:
        content = content.replace(old_body_css2, new_body_css2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in files:
    update_file(filepath)

print("Viewport and body constraints updated.")
