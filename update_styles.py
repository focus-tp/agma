import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace floating-booking with mobile-bottom-bar
css = re.sub(
    r'\.floating-booking \{.*?\n\}', 
    '''
.mobile-bottom-bar {
  display: none;
}

@media (max-width: 768px) {
  .mobile-bottom-bar {
    display: flex;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 16px;
    gap: 12px;
    background: rgba(14, 14, 14, 0.7);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    z-index: 999;
  }
  .bottom-bar-btn {
    flex: 1;
    text-align: center;
    padding: 14px 0;
    font-size: 14px;
    font-weight: 500;
    border-radius: 8px;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  .btn-secondary {
    background: rgba(255, 255, 255, 0.05);
    color: var(--color-text);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }
  .btn-secondary:hover {
    background: rgba(255, 255, 255, 0.1);
  }
  .mobile-bottom-bar .btn-primary {
    background: var(--color-primary);
    color: #fff;
    border: none;
  }
}
''', 
    css, 
    flags=re.DOTALL
)

# Fluid typography
css = re.sub(r'font-size:\s*72px;', 'font-size: clamp(3rem, 8vw, 4.5rem);', css) # .hero-title
css = re.sub(r'font-size:\s*48px;', 'font-size: clamp(2rem, 5vw, 3rem);', css) # .manifesto-header h2
css = re.sub(r'font-size:\s*36px;', 'font-size: clamp(1.75rem, 4vw, 2.25rem);', css) # h2
css = re.sub(r'font-size:\s*24px;', 'font-size: clamp(1.25rem, 3vw, 1.5rem);', css) # .manifesto-lead

# Value Cards updates
css = re.sub(
    r'\.val-card \{([\s\S]*?)\}',
    r'.val-card {\1\n  padding: 24px;\n  border: 1px solid rgba(255, 255, 255, 0.05);\n  border-radius: 12px;\n  transition: all 0.3s ease;\n}\n.val-card:hover {\n  background: rgba(255, 255, 255, 0.02);\n  transform: translateY(-4px);\n  border-color: rgba(255, 255, 255, 0.1);\n}',
    css
)

# Price list hover
css = re.sub(
    r'\.price-row \{([\s\S]*?)\}',
    r'.price-row {\1\n  padding: 8px;\n  border-radius: 8px;\n  transition: all 0.3s ease;\n}\n.price-row:hover {\n  background: rgba(255, 255, 255, 0.03);\n  color: #fff;\n}\n.price-row:hover .price-dots {\n  border-bottom: 1px dotted rgba(255, 255, 255, 0.4);\n}',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.")
