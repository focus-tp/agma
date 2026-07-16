import re

# 1. Update main.js to remove auto-closing accordion logic
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

auto_close_code = """
      // Close all other accordions (optional, but good for UX)
      document.querySelectorAll('.accordion-item').forEach(item => {
        item.classList.remove('active');
        item.querySelector('.accordion-content').style.maxHeight = null;
      });
"""
if auto_close_code in js:
    js = js.replace(auto_close_code, '')

# Wait, if an accordion is already active, clicking it again should close it. The old code did that because it toggled if !isActive.
# Let's rewrite the accordion logic properly.
accordion_logic = """
      // Toggle current accordion
      if (!isActive) {
        accordionItem.classList.add('active');
        accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
      } else {
        accordionItem.classList.remove('active');
        accordionContent.style.maxHeight = null;
      }
"""
js = re.sub(r'// Toggle current accordion\n\s*if \(!isActive\) \{.*?\n\s*\}', accordion_logic, js, flags=re.DOTALL)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Update index.html logo to be an anchor link
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div class="logo logo-difference">Beauty Sekta</div>', '<a href="#home" class="logo logo-difference" style="text-decoration: none;">Beauty Sekta</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bugs fixed.")
