import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change section-light to section-dark
html = html.replace('<section class="services-section section-light" id="services">', 
                    '<section class="services-section section-dark" id="services">')

# To add the image, let's wrap the accordion in a grid
# Currently it looks like:
# <div class="accordion-container animate-on-scroll">
#   <!-- Волосы -->
# Let's change accordion-container to services-grid-layout and add the image

new_layout = """
          <div class="services-grid-layout animate-on-scroll" style="display: grid; grid-template-columns: 1fr 1.5fr; gap: 40px; align-items: start;">
            <div class="services-image-wrapper" style="position: sticky; top: 100px; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
              <img src="/vk_prices.png" alt="Прайс-лист ВКонтакте" style="width: 100%; height: auto; display: block;" />
            </div>
            <div class="accordion-container" style="max-width: 100%;">
"""

html = html.replace('<div class="accordion-container animate-on-scroll">', new_layout)
# And we need to close the extra div after accordion-container ends. 
# Wait, let's just use regex to find where accordion-container ends.
# It ends right before "</div>\n        </div>\n      </section>"

html = re.sub(r'(</button>\s*<div class="accordion-content">.*?</div>\n\s*</div>\n\n\s*)</div>', r'\1</div>\n          </div>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated HTML")
