import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove inline style and add class
html = re.sub(
    r'<img src="/hero_team2\.jpg" alt="Команда Beauty Sekta" style="object-position: center 70%;" />',
    '<img src="/hero_team2.jpg" alt="Команда Beauty Sekta" class="hero-img" />',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_img_css = """
.hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-img {
  object-position: center 50%;
}

@media (max-width: 768px) {
  .hero-img {
    object-position: center 25%;
  }
}
"""

if '.hero-img {' not in css:
    css += "\n" + hero_img_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hero position updated.")
