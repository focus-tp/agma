import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Contact tweaks
css = css.replace('font-size: clamp(1.25rem, 3vw, 1.5rem);', 'font-size: 1.1rem;')
css = css.replace('.contact-list li {\n  margin-bottom: 24px;\n  display: flex;\n  flex-direction: column;\n}', '.contact-list li {\n  margin-bottom: 12px;\n  display: flex;\n  flex-direction: column;\n}')

# Noise overlay
noise_css = """
/* Noise Texture */
.noise-overlay {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}
"""
if '.noise-overlay' not in css:
    css += "\n" + noise_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add noise overlay
if '<div class="noise-overlay"></div>' not in html:
    html = html.replace('<body>', '<body>\n    <div class="noise-overlay"></div>')

# Shorten team text
html = html.replace("""<p>В профессии 5 лет. Создает идеальные короткие стрижки.</p>
                  <p>Регулярно повышает квалификацию, следит за трендами и внедряет передовые техники, обеспечивая индивидуальный подход и безупречное качество.</p>
                  <p>Направление:</p>
                  <ul>
                    <li>Идеальные короткие стрижки</li>
                    <li>Передовые техники окрашивания</li>
                  </ul>""", """<p>Опыт 5 лет.</p>
                  <ul>
                    <li>Короткие стрижки</li>
                    <li>Передовые окрашивания</li>
                  </ul>""")

html = html.replace("""<p>Сложные техники окрашивания - это её стихия. Анастасия создаёт сложный блонд на высшем уровне, сочетая это с профессиональным знанием трихологических особенностей.</p>
                  <p>Направление:</p>
                  <ul>
                    <li>Сложные техники окрашивания</li>
                    <li>Профессиональный подбор оттенков</li>
                  </ul>""", """<ul>
                    <li>Сложный блонд</li>
                    <li>Трихология и уходы</li>
                  </ul>""")

html = html.replace("""<p>Работа с разными типами волос, кудри.</p>
                  <p>Направление:</p>
                  <ul>
                    <li>Стрижки (модельные, повседневные)</li>
                    <li>Современные техники окрашивания</li>
                    <li>Завивка</li>
                    <li>Кудрявый метод укладки</li>
                    <li>Работа с натуральными и химически завитыми волосами</li>
                  </ul>""", """<ul>
                    <li>Кудрявый метод укладки</li>
                    <li>Современные окрашивания</li>
                    <li>Завивка и модельные стрижки</li>
                  </ul>""")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Team, Contact and Noise fixed.")
