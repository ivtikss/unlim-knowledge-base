document.addEventListener("DOMContentLoaded", function() {
    const emailInput = document.querySelector('input[type="email"]');
    if (emailInput) {
        emailInput.classList.add("email-input");
    }
});