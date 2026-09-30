// script.js - Vasco Tech Alcobendas
document.addEventListener('DOMContentLoaded', function() {
    // --- Mobile Menu Toggle ---
    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            // Change icon
            const icon = menuToggle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-times');
                }
            });
        });
    }
});n(e) {            if (e.target === adminModal) {                closeAdminModal();            }        });    }        // Close modal with Escape key    document.addEventListener('keydown', function(e) {        if (e.key === 'Escape' && adminModal && adminModal.style.display === 'flex') {            closeAdminModal();        }    });        // Form submission    if (adminForm) {        adminForm.addEventListener('submit', function(e) {            e.preventDefault();            const password = document.getElementById('admin-password').value;            const heroImageUrl = document.getElementById('hero-image-url').value;                        if (password !== 'jonva1985') {                adminMessage.textContent = 'Contrase�a incorrecta.';                adminMessage.style.color = '#ea4335';                return;            }                        // Save to localStorage            localStorage.setItem('adminImageHero', heroImageUrl);                        // Apply changes immediately            applyHeroImage(heroImageUrl);                        adminMessage.textContent = 'Configuraci�n guardada exitosamente.';            adminMessage.style.color = '#10b981';                        // Close modal after short delay            setTimeout(closeAdminModal, 1500);        });    }    // --- Apply saved settings on page load ---    function applyHeroImage(url) {        const heroSection = document.querySelector('.hero-section');        if (heroSection && url) {            heroSection.style.backgroundImage = `url(${url})`;            heroSection.style.backgroundSize = 'cover';            heroSection.style.backgroundPosition = 'center';            // Hide the default background image            const bgImg = heroSection.querySelector('.hero-background img');            if (bgImg) bgImg.style.display = 'none';        }    }    // $content[$i]// $content[$i]// $content[$i]    }    // --- Scroll Animations (IntersectionObserver) ---    const observerOptions = {        threshold: 0.1,        rootMargin: '0px 0px -50px 0px'    };        const observer = new IntersectionObserver(function(entries) {        entries.forEach(entry => {            if (entry.isIntersecting) {                entry.target.classList.add('element-visible');                observer.unobserve(entry.target);            }        });    }, observerOptions);        const fadeElements = document.querySelectorAll('.fade-in');    fadeElements.forEach(el => {        el.classList.add('element-hidden');        observer.observe(el);    });    // --- Smooth scroll for anchor links ---    document.querySelectorAll('a[href^="#"]').forEach(anchor => {        anchor.addEventListener('click', function(e) {            const targetId = this.getAttribute('href');            if (targetId === '#') return;            const target = document.querySelector(targetId);            if (target) {                e.preventDefault();                target.scrollIntoView({ behavior: 'smooth', block: 'start' });            }        });    });    // --- Print/Download CV button ---    const printBtn = document.querySelector('.btn-print');    if (printBtn) {        printBtn.addEventListener('click', function() {            window.print();        });    }    // --- AOS Initialization (if AOS is loaded) ---    if (typeof AOS !== 'undefined') {        AOS.init({            duration: 800,            once: true,            offset: 100        });    }});// --- Legacy functions (kept for compatibility) ---function cambiarImagenCabecera() {    alert('Funcionalidad de cambio de imagen: En una aplicaci�n completa, aqu� se abrir�a un selector de archivo para subir una nueva imagen de cabecera que ser�a guardada en el servidor y aplicada a todos los usuarios.');}