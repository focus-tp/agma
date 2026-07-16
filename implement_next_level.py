import re

# ================== 1. CSS CHANGES ==================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change Accent Color to Burgundy
css = re.sub(r'--color-accent:\s*#[a-fA-F0-9]+;', '--color-accent: #7a1a26;', css)

# Append new styles
new_css = """
/* --- NEXT-LEVEL EFFECTS --- */

/* 1. Film Grain Overlay */
#noise-overlay {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  pointer-events: none; z-index: 9999; opacity: 0.04;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  animation: noiseAnimation 0.2s infinite;
}
@keyframes noiseAnimation {
  0% { transform: translate(0, 0); }
  10% { transform: translate(-5%, -5%); }
  20% { transform: translate(-10%, 5%); }
  30% { transform: translate(5%, -10%); }
  40% { transform: translate(-5%, 15%); }
  50% { transform: translate(-10%, 5%); }
  60% { transform: translate(15%, 0); }
  70% { transform: translate(0, 15%); }
  80% { transform: translate(3%, 35%); }
  90% { transform: translate(-10%, 10%); }
  100% { transform: translate(0, 0); }
}

/* 2. Text Reveal Animation */
.reveal-text span {
  display: inline-block;
  transform: translateY(100%);
  opacity: 0;
  transition: transform 1s cubic-bezier(0.19, 1, 0.22, 1), opacity 1s ease;
}
.reveal-text.is-visible span {
  transform: translateY(0);
  opacity: 1;
}
.reveal-text span:nth-child(2) { transition-delay: 0.15s; }
.reveal-text span:nth-child(3) { transition-delay: 0.3s; }

/* 3. Hover Image Reveal (Price list) */
#hover-image-reveal {
  position: fixed;
  top: 0; left: 0;
  width: 250px; height: 350px;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
  pointer-events: none;
  z-index: 9998;
  opacity: 0;
  transform: translate(-50%, -50%) scale(0.9);
  transition: opacity 0.4s ease, transform 0.4s ease;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}
#hover-image-reveal.active {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}
"""
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + new_css)


# ================== 2. HTML CHANGES ==================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add noise and hover image div to body
body_additions = """
    <div id="noise-overlay"></div>
    <div id="hover-image-reveal"></div>
"""
if '<div id="noise-overlay">' not in html:
    html = html.replace('<body>', '<body>\n' + body_additions)

# Wrap hero title in span
html = html.replace(
    '<h1 class="hero-title animate-on-scroll">Твоя красота<br>Твоя секта</h1>',
    '<h1 class="hero-title animate-on-scroll reveal-text"><span>Твоя красота</span><br><span>Твоя секта</span></h1>'
)
# Wrap manifesto header
html = html.replace(
    '<h2 class="animate-on-scroll">Наши Ценности</h2>',
    '<h2 class="animate-on-scroll reveal-text"><span>Наши Ценности</span></h2>'
)
# Wrap team header
html = html.replace(
    '<h2 class="section-title animate-on-scroll">Команда</h2>',
    '<h2 class="section-title animate-on-scroll reveal-text"><span>Команда</span></h2>'
)

# Add data-image to some price rows as examples
html = html.replace(
    '<div class="price-row"><span class="price-name">Окрашивание в 1 тон (корни)</span>',
    '<div class="price-row" data-image="/hero_team2.jpg"><span class="price-name">Окрашивание в 1 тон (корни)</span>'
)
html = html.replace(
    '<div class="price-row"><span class="price-name">Сложное окрашивание (до 15см)</span>',
    '<div class="price-row" data-image="/team_value.jpg"><span class="price-name">Сложное окрашивание (до 15см)</span>'
)
html = html.replace(
    '<div class="price-row"><span class="price-name">Стрижка (длинные)</span>',
    '<div class="price-row" data-image="/master_clean1.jpg"><span class="price-name">Стрижка (длинные)</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ================== 3. JS CHANGES ==================
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_additions = """
  // Image Reveal on Hover (Price list)
  if (window.matchMedia("(pointer: fine)").matches) {
    const hoverImageEl = document.getElementById('hover-image-reveal');
    const priceRows = document.querySelectorAll('.price-row[data-image]');
    
    // We already have mousemove for custom cursor, let's just add one for hover-image
    document.addEventListener('mousemove', (e) => {
      if (hoverImageEl.classList.contains('active')) {
        // slight offset so it doesn't block the cursor exactly
        hoverImageEl.style.left = (e.clientX + 50) + 'px';
        hoverImageEl.style.top = (e.clientY) + 'px';
      }
    });

    priceRows.forEach(row => {
      row.addEventListener('mouseenter', (e) => {
        const imageUrl = row.getAttribute('data-image');
        hoverImageEl.style.backgroundImage = `url(${imageUrl})`;
        hoverImageEl.classList.add('active');
        hoverImageEl.style.left = (e.clientX + 50) + 'px';
        hoverImageEl.style.top = (e.clientY) + 'px';
      });
      row.addEventListener('mouseleave', () => {
        hoverImageEl.classList.remove('active');
      });
    });
  }
"""
if 'hover-image-reveal' not in js:
    # insert before the last '});'
    js = js[:js.rfind('});')] + js_additions + '\n});'
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Next-Level implemented.")
