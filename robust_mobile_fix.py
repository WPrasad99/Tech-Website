import os
import re

files = [
    r"c:\Users\Prasad\Desktop\Tech-Website\index.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
]

injection_css = """
        /* Critical Mobile Responsiveness & Overflow Fixes */
        html, body {
            overflow-x: hidden !important;
            width: 100vw !important;
            max-width: 100% !important;
            position: relative;
        }
        * {
            box-sizing: border-box;
        }
"""

for filepath in files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject CSS before </style> to guarantee application
    if "/* Critical Mobile Responsiveness" not in content:
        content = content.replace("</style>", injection_css + "</style>")

    # 2. Fix viewport meta tags robustly
    content = re.sub(r'<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                     '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">', content)

    # 3. Reduce 7-second loader timeout to 1.5 seconds (1500ms)
    content = content.replace("7000);", "1500);")
    
    # 4. Preload videos so loading animation isn't blank while loading
    content = content.replace("<video autoplay muted", '<video autoplay muted preload="auto"')

    # Fix AOS fade directions just to be strictly safe on mobile horizontal layout shifts
    # Some layouts break even with overflow-x: hidden if AOS pushes them 3000px right
    content = content.replace('data-aos="fade-right"', 'data-aos="fade-up"')
    content = content.replace('data-aos="fade-left"', 'data-aos="fade-up"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Robust mobile and performance fixes applied to all files.")
