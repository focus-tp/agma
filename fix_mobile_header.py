import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_header_css = """
@media (max-width: 768px) {
  .header-container {
    flex-wrap: nowrap !important;
    gap: 8px;
  }
  
  .header-container .logo {
    font-size: 1.1rem;
    white-space: nowrap;
  }
  
  .header-container .btn-outline {
    padding: 8px 12px;
    font-size: 10px;
    white-space: nowrap;
    margin-left: auto;
  }
  
  .header-container .burger-menu {
    margin-left: 8px;
  }
}
"""

if '.header-container .btn-outline' not in css:
    css += "\n" + mobile_header_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Mobile header fixed.")
