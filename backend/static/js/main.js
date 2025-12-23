// backend/static/js/main.js

document.addEventListener("DOMContentLoaded", function() {
    const scenes = document.querySelectorAll('.scroll-scene');
    const stickyContainer = document.querySelector('.sticky-shoe-container');
    const shoeWrapper = document.querySelector('.shoe-wrapper');
    const scrollContent = document.querySelector('.scroll-content');

    if (!scenes.length || !stickyContainer || !shoeWrapper || !scrollContent) {
        console.error("Scrolly-telling elements are missing. Animation will not run.");
        return;
    }

    // First scene active
    scenes[0].classList.add('is-active');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-active');
            } else {
                entry.target.classList.remove('is-active');
            }
        });
    }, { threshold: 0.5 });

    scenes.forEach(scene => observer.observe(scene));

    let ticking = false;
    let isScrolling;

    function handleScroll() {
        const scrollRect = scrollContent.getBoundingClientRect();
        const scrollHeight = scrollContent.scrollHeight - window.innerHeight;
        const scrollTop = -scrollRect.top;
        let progress = scrollTop / scrollHeight;
        progress = Math.max(0, Math.min(1, progress));

        // Stronger zoom effect (1x -> 1.8x)
        const scale = 1 + Math.sin(progress * Math.PI) * 0.8;
        const rotate = -10 + (progress * 20);

        shoeWrapper.style.transition = "transform 0.15s ease-out";
        shoeWrapper.style.transform = `rotate(${rotate}deg) scale(${scale})`;

        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) {
            handleScroll();
            ticking = true;
        }

        // When user stops scrolling → zoom out smoothly
        clearTimeout(isScrolling);
        isScrolling = setTimeout(() => {
            shoeWrapper.style.transition = "transform 0.8s ease-out";
            shoeWrapper.style.transform = "rotate(0deg) scale(1)";
        }, 300);
    });
});
