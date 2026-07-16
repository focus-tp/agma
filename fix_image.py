import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the services-grid-layout and the image
html = re.sub(r'<div class="services-grid-layout animate-on-scroll">\s*<div class="services-image-sticky">\s*<img src="/vk_prices\.png" alt="Прайс-лист ВКонтакте" />\s*</div>\s*<div class="accordion-container">', 
              r'<div class="accordion-container animate-on-scroll">', html)

# Fix the closing divs
html = html.replace('          </div>\n          </div>\n        </div>\n      </section>', 
                    '          </div>\n        </div>\n      </section>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed image")
