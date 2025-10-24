// Countdown Timer
function updateCountdown() {
    // Set the event date (YYYY, MM (0-11), DD, HH, MM, SS)
    const eventDate = new Date(Date.UTC(2025, 10, 15, 20, 0, 0)).getTime();
    const now = new Date().getTime();
    const distance = eventDate - now;

    // If the event has already happened
    if (distance <= 0) {
        // Set all counters to zero
        document.getElementById('days').textContent = '000';
        document.getElementById('hours').textContent = '00';
        document.getElementById('minutes').textContent = '00';
        document.getElementById('seconds').textContent = '00';
        
        // Clear the interval so the counter stops updating
        clearInterval(countdownTimer);
        return;
    }

    // Time calculations
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result
    document.getElementById('days').textContent = days.toString().padStart(2, '0');
    document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
    document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
    document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
}

// Initialize countdown only if elements exist
if (document.getElementById('days')) {
    // Run immediately to avoid initial delay
    updateCountdown();
    // Then update every second
    const countdownTimer = setInterval(updateCountdown, 1000);
}