with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract the new services_price block
import re

# Find the start of services_price
new_services_match = re.search(r'      <!-- Services Section -->\s+<section class="services-section section-light" id="services_price">.*?</section>', html, re.DOTALL)
if new_services_match:
    new_services_html = new_services_match.group(0)
    # Remove the new services block from where it was appended
    html = html.replace(new_services_html, '')
    
    # Change its id back to "services" so links work
    new_services_html = new_services_html.replace('id="services_price"', 'id="services"')
    
    # 2. Find the old services block and replace it
    old_services_match = re.search(r'      <!-- Services Section -->\s+<section class="services section-light" id="services">.*?</section>', html, re.DOTALL)
    if old_services_match:
        old_services_html = old_services_match.group(0)
        html = html.replace(old_services_html, new_services_html)
    else:
        print("Could not find old services block")
        
    # Update navigation if it was pointing to services_price
    html = html.replace('href="#services_price"', 'href="#services"')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
else:
    print("Could not find new services block")

