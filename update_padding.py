import os

# Fix padding in about-us.html
about_file = r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html"
with open(about_file, 'r', encoding='utf-8') as f:
    about_content = f.read()
about_content = about_content.replace('py-24', 'py-12 md:py-24')
with open(about_file, 'w', encoding='utf-8') as f:
    f.write(about_content)

# Fix padding in careers.html
careers_file = r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
with open(careers_file, 'r', encoding='utf-8') as f:
    careers_content = f.read()
careers_content = careers_content.replace('pt-20 pb-20', 'pt-10 md:pt-20 pb-10 md:pb-20')
careers_content = careers_content.replace('mt-24 pb-12', 'mt-12 md:mt-24 pb-12')
with open(careers_file, 'w', encoding='utf-8') as f:
    f.write(careers_content)

print("Vertical padding updated for mobile responsiveness")
