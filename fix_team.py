import re

# 1. Shorten Nataly's text in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

nataly_text = """                  <p>Сооснователь салона красоты.</p>
                  <p>Идейный вдохновитель Beauty Sekta. Лично отбирает команду и обучает мастеров уникальным <strong>авторским методикам</strong> работы с волосами, доводя каждый срез и оттенок до абсолютного идеала.</p>
                  <p>Направление:</p>
                  <ul>
                    <li>Внедрение авторских методик сложных окрашиваний и стрижек</li>
                    <li>Бескомпромиссный контроль качества и стандартов премиум-сервиса</li>
                    <li>Создание уникального стиля Beauty Sekta</li>
                  </ul>"""

short_nataly_text = """                  <p>Сооснователь салона.</p>
                  <p>Идейный вдохновитель Beauty Sekta. Обучает мастеров <strong>авторским методикам</strong>.</p>
                  <p>Направление:</p>
                  <ul>
                    <li>Сложные окрашивания и стрижки</li>
                    <li>Контроль качества</li>
                  </ul>"""

html = html.replace(nataly_text, short_nataly_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix CSS Grid for masonry and odd transform
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace masonry grid columns with grid
css = re.sub(
    r'\.masonry-grid \{\n\s*columns: 1;\n\s*column-gap: 32px;\n\}',
    '.masonry-grid { display: grid; grid-template-columns: 1fr; gap: 32px; align-items: start; }',
    css
)
css = re.sub(
    r'@media \(min-width: 768px\) \{\n\s*\.masonry-grid \{\n\s*columns: 2;\n\s*\}\n\}',
    '@media (min-width: 768px) { .masonry-grid { grid-template-columns: 1fr 1fr; } }',
    css
)

# Replace nth-child(even) with nth-child(odd)
css = css.replace('.masonry-grid .editorial-image-wrapper:nth-child(even) {', '.masonry-grid .editorial-image-wrapper:nth-child(odd) {')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Team fixed.")
