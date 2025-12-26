document.addEventListener('DOMContentLoaded', () => {
    const logo = document.querySelector('.js-logo');

    logo.addEventListener('mouseenter', () => {
        logo.style.letterSpacing = '8px';
        logo.style.transition = '0.4s';
    });

    logo.addEventListener('mouseleave', () => {
        logo.style.letterSpacing = '3px';
    });
});