import os
import re

files = [
    r"c:\Users\Prasad\Desktop\Tech-Website\index.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\about-us.html",
    r"c:\Users\Prasad\Desktop\Tech-Website\careers.html"
]

new_social_block = """<div class="flex justify-center space-x-6 mb-4">
                        <!-- LinkedIn -->
                        <a href="https://www.linkedin.com/in/kln-business-solutions-company-6b7720411/" target="_blank" class="text-gray-400 hover:text-blue-600 transition"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" /><rect width="4" height="12" x="2" y="9" /><circle cx="4" cy="4" r="2" /></svg></a>
                        <!-- Facebook -->
                        <a href="https://www.facebook.com/profile.php?id=61590479276674" target="_blank" class="text-gray-400 hover:text-blue-600 transition"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                        <!-- Instagram -->
                        <a href="https://www.instagram.com/klnbusinesssolutions?utm_source=qr&igsh=Y3RhZ3ZzN2VmeHZi" target="_blank" class="text-gray-400 hover:text-blue-600 transition"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5"><rect width="20" height="20" x="2" y="2" rx="5" ry="5" /><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" /><line x1="17.5" x2="17.51" y1="6.5" y2="6.5" /></svg></a>
                    </div>"""

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire social div block using regex (dot matches newline)
        pattern = r'<div class="flex justify-center space-x-6 mb-4">.*?</div>'
        content = re.sub(pattern, new_social_block, content, flags=re.DOTALL)
        
        # Replace phone number links
        content = content.replace("tel:+1-555-123-4567", "tel:+919175498572")
        content = content.replace("+1-555-123-4567", "+91 91754 98572")
        
        # Replace google map link
        content = content.replace("https://maps.google.com/?q=18.4590521,73.8391388", "https://share.google/CQaj5y0FpkDuklEFh")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Footer updated successfully across all files.")
