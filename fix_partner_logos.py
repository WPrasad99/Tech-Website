import os

files = [
    r"c:\Users\Prasad\Desktop\Tech-Website\index.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix accidental replacement of 'logo.png' in other filenames
        content = content.replace("rikarena_logo1.png", "rikarena_logo.png")
        content = content.replace("systera_logo1.png", "systera_logo.png")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Partner company logos repaired successfully.")
