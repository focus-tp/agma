import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the 2-column layout back
new_layout = """
          <div class="services-grid-layout animate-on-scroll">
            <div class="services-image-sticky">
              <img src="/prices_app.png" alt="Цены ВКонтакте" />
            </div>
            <div class="accordion-container">
"""

html = html.replace('<div class="accordion-container animate-on-scroll">', new_layout)
html = html.replace('          </div>\n        </div>\n      </section>', 
                    '          </div>\n          </div>\n        </div>\n      </section>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Re-added image layout")
