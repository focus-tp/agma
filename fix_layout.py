import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the grid layout and the image block
html = html.replace('<div class="services-grid-layout animate-on-scroll">\n            <div class="services-image-sticky">\n              <img src="/prices_app.png" alt="Цены ВКонтакте" />\n            </div>', '')
html = html.replace('<div class="accordion-container">', '<div class="accordion-container animate-on-scroll">')
# Fix the extra closing div
html = html.replace('          </div>\n          </div>\n        </div>\n      </section>', 
                    '          </div>\n        </div>\n      </section>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed image block")
