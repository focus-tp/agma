document.addEventListener('DOMContentLoaded', () => {
  // Sticky Header
  const header = document.getElementById('header');
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Smooth Scroll for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80, // Offset for header
          behavior: 'smooth'
        });
      }
    });
  });

  // Scroll Animations (Intersection Observer)
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target); // Optional: stop observing once visible
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
  });

  // Parallax Effect
  const parallaxImages = document.querySelectorAll('.parallax-img');
  
  window.addEventListener('scroll', () => {
    parallaxImages.forEach(img => {
      const container = img.parentElement;
      const rect = container.getBoundingClientRect();
      
      // Check if container is in viewport
      if (rect.top <= window.innerHeight && rect.bottom >= 0) {
        // Calculate offset relative to viewport center
        const scrollOffset = (window.innerHeight / 2) - (rect.top + rect.height / 2);
        const speed = 0.15;
        img.style.transform = `translateY(${scrollOffset * speed}px)`;
      }
    });
  });

  // Custom Cursor
  if (window.matchMedia("(pointer: fine)").matches) {
    const cursor = document.getElementById('custom-cursor');
    
    document.addEventListener('mousemove', (e) => {
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
    });

    // Add hover states for links and buttons
    const hoverElements = document.querySelectorAll('a, button, .btn');
    hoverElements.forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hovering-link'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hovering-link'));
    });

    // Add special hover state for portfolio items
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    portfolioItems.forEach(item => {
      item.addEventListener('mouseenter', () => cursor.classList.add('hovering-portfolio'));
      item.addEventListener('mouseleave', () => cursor.classList.remove('hovering-portfolio'));
    });
  } // Restore missing brace
  
  // Accordion Logic
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const accordionItem = header.parentElement;
      const accordionContent = header.nextElementSibling;
      const isActive = accordionItem.classList.contains('active');

      
      // Toggle current accordion
      if (!isActive) {
        accordionItem.classList.add('active');
        accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
      } else {
        accordionItem.classList.remove('active');
        accordionContent.style.maxHeight = null;
      }

    });
  });


  // Image Reveal on Hover (Price list)
  if (window.matchMedia("(pointer: fine)").matches) {
    const hoverImageEl = document.getElementById('hover-image-reveal');
    const priceRows = document.querySelectorAll('.accordion-header[data-image]');
    
    // We already have mousemove for custom cursor, let's just add one for hover-image
    document.addEventListener('mousemove', (e) => {
      if (hoverImageEl.classList.contains('active')) {
        // slight offset so it doesn't block the cursor exactly
        hoverImageEl.style.left = (e.clientX + 50) + 'px';
        hoverImageEl.style.top = (e.clientY) + 'px';
      }
    });

    // Preload images to prevent delay on first hover
    const preloadedImages = {};
    priceRows.forEach(row => {
      const imageUrl = row.getAttribute('data-image');
      if (imageUrl) {
        preloadedImages[imageUrl] = new Image();
        preloadedImages[imageUrl].src = imageUrl;
      }

      row.addEventListener('mouseenter', (e) => {
        if (!row.parentElement.classList.contains('active')) {
          hoverImageEl.style.backgroundImage = `url(${imageUrl})`;
          hoverImageEl.classList.add('active');
          hoverImageEl.style.left = (e.clientX + 50) + 'px';
          hoverImageEl.style.top = (e.clientY) + 'px';
        }
      });
      row.addEventListener('click', () => {
        hoverImageEl.classList.remove('active');
      });
      row.addEventListener('mouseleave', () => {
        hoverImageEl.classList.remove('active');
      });
    });
  }

});

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


  // Cookie Banner Logic
  const cookieBanner = document.getElementById('cookie-banner');
  const cookieAcceptBtn = document.getElementById('cookie-accept');

  if (cookieBanner && cookieAcceptBtn) {
    // Check if user already accepted
    if (!localStorage.getItem('cookiesAccepted_v2')) {
      setTimeout(() => {
        cookieBanner.classList.add('show');
      }, 2000); // Show after 2 seconds
    }

    cookieAcceptBtn.addEventListener('click', () => {
      localStorage.setItem('cookiesAccepted_v2', 'true');
      cookieBanner.classList.remove('show');
    });
  }
