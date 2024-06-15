function toggleForms() {
    var loginForm = document.getElementById('loginForm');
    var registerForm = document.getElementById('registerForm');

    if (loginForm.style.display === 'none') {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    } else {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    }
}

let currentSlide = 0;

function moveSlider(direction) {
    const sliderWrapper = document.querySelector('.slider-wrapper');
    const totalSlides = document.querySelectorAll('.slider-item').length;
    
    currentSlide += direction;

    if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    } else if (currentSlide >= totalSlides) {
        currentSlide = 0;
    }

    const newTransform = -currentSlide * 100 + '%';
    sliderWrapper.style.transform = `translateX(${newTransform})`;
}