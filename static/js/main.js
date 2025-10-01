document.addEventListener('DOMContentLoaded', function() {
    const progressCircles = document.querySelectorAll('.circular-progress');
    progressCircles.forEach(circle => {
        const score = circle.getAttribute('data-score');
        circle.style.setProperty('--score', score);
    });
});
