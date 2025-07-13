document.addEventListener('DOMContentLoaded', function() {
    // Show all alerts
    const alerts = document.querySelectorAll('.custom-alert');
    alerts.forEach(alert => {
        alert.classList.add('show');
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            hideAlert(alert);
        }, 5000);
    });
    
    // Close button functionality
    document.querySelectorAll('.custom-alert-close').forEach(button => {
        button.addEventListener('click', function() {
            const alert = this.closest('.custom-alert');
            hideAlert(alert);
        });
    });
    
    function hideAlert(alert) {
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-100%)';
        
        // Remove element after animation completes
        setTimeout(() => {
            alert.remove();
        }, 600);
    }
});