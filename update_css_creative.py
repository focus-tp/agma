import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

creative_styles = """
/* --- CREATIVE ASYMMETRY & EFFECTS --- */

/* Logo Difference Effect */
.logo-difference {
  mix-blend-mode: difference;
  color: #fff; /* White becomes inverted against background */
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px;
  text-transform: uppercase;
  letter-spacing: 2px;
  z-index: 1000;
  position: relative;
}

/* Header Background Transparent so difference works against the page body */
.header {
  background: transparent !important;
  backdrop-filter: none !important;
  border-bottom: none !important;
}

/* Marquee Background */
.manifesto {
  position: relative;
  overflow: hidden;
}
.marquee-bg {
  position: absolute;
  top: 20%;
  left: 0;
  width: 100%;
  white-space: nowrap;
  opacity: 0.03;
  z-index: 0;
  pointer-events: none;
  font-family: 'Montserrat', sans-serif;
  font-size: clamp(100px, 15vw, 200px);
  font-weight: 900;
  color: #fff;
  line-height: 1;
}
.marquee-content {
  display: inline-block;
  animation: marquee 30s linear infinite;
}
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Asymmetric Values Grid */
.values-editorial-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  position: relative;
  z-index: 2;
}
@media (min-width: 768px) {
  .values-editorial-grid {
    grid-template-columns: 1fr 1fr;
  }
  .values-editorial-grid .val-card:nth-child(even) {
    transform: translateY(60px);
  }
  .values-editorial-grid .val-card:hover {
    transform: translateY(50px) scale(1.02);
  }
  .values-editorial-grid .val-card:nth-child(odd):hover {
    transform: translateY(-10px) scale(1.02);
  }
}

/* Staggered Team Photos */
@media (min-width: 768px) {
  .masonry-grid .editorial-image-wrapper:nth-child(even) {
    transform: translateY(80px);
  }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n' + creative_styles)

print("CSS Updated.")
