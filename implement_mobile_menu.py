import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

menu_html = """
    <div class="mobile-menu-overlay">
      <ul class="mobile-nav-list">
        <li><a href="#home" class="mobile-nav-link">Главная</a></li>
        <li><a href="#manifesto" class="mobile-nav-link">Ценности</a></li>
        <li><a href="#services" class="mobile-nav-link">Услуги</a></li>
        <li><a href="#portfolio" class="mobile-nav-link">Портфолио</a></li>
        <li><a href="#team" class="mobile-nav-link">Команда</a></li>
        <li><a href="#contact" class="mobile-nav-link">Контакты</a></li>
      </ul>
    </div>
"""
if '<div class="mobile-menu-overlay">' not in html:
    html = html.replace('</header>', '</header>\n' + menu_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* --- Mobile Menu --- */
.mobile-menu-overlay {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100vh;
  background: rgba(10, 10, 10, 0.98);
  backdrop-filter: blur(10px);
  z-index: 999;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  pointer-events: none;
  transition: all 0.4s ease;
}
.mobile-menu-overlay.active {
  opacity: 1;
  pointer-events: all;
}
.mobile-nav-list {
  list-style: none;
  text-align: center;
  padding: 0;
}
.mobile-nav-link {
  display: block;
  font-size: 24px;
  color: var(--color-accent);
  text-transform: uppercase;
  margin: 24px 0;
  text-decoration: none;
  font-weight: 500;
  letter-spacing: 2px;
}

.burger-menu {
  display: none;
  cursor: pointer;
  z-index: 1001;
  width: 24px;
  height: 18px;
  position: relative;
}
.burger-menu div {
  width: 100%;
  height: 2px;
  background-color: var(--color-text);
  position: absolute;
  transition: all 0.3s ease;
  left: 0;
}
.burger-menu .line1 { top: 0; }
.burger-menu .line2 { top: 8px; }
.burger-menu .line3 { top: 16px; }

.burger-menu.active .line1 { transform: rotate(-45deg); top: 8px; background-color: var(--color-accent); }
.burger-menu.active .line2 { opacity: 0; }
.burger-menu.active .line3 { transform: rotate(45deg); top: 8px; background-color: var(--color-accent); }

@media (max-width: 768px) {
  .burger-menu {
    display: block;
  }
}

/* Fix spacing for manifesto */
#manifesto {
  padding-top: 40px !important;
}
.manifesto-container {
  padding-top: 0 !important;
}
"""
if '.mobile-menu-overlay {' not in css:
    css += "\n" + new_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 3. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js_additions = """
  // Mobile Menu Logic
  const burgerMenu = document.querySelector('.burger-menu');
  const mobileMenu = document.querySelector('.mobile-menu-overlay');
  
  if (burgerMenu && mobileMenu) {
    burgerMenu.addEventListener('click', () => {
      burgerMenu.classList.toggle('active');
      mobileMenu.classList.toggle('active');
    });

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => {
        burgerMenu.classList.remove('active');
        mobileMenu.classList.remove('active');
      });
    });
  }
"""

if 'mobile-menu-overlay' not in js:
    # insert before end
    js = js + '\n' + js_additions
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Menu and padding fixed.")
