import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update global logo font-size
css = css.replace(""".logo {
  font-size: 1.1rem;""", """.logo {
  font-size: clamp(1.5rem, 4vw, 2rem);""")

# Update mobile logo font-size
css = css.replace("""  .header-container .logo {
    font-size: 1.1rem;""", """  .header-container .logo {
    font-size: 1.4rem;""")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Logo enlarged.")
