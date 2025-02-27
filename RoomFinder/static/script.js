document.addEventListener('DOMContentLoaded', function() {
    // Auto-capitalize USN input
    const usnInput = document.getElementById('usn');
    if (usnInput) {
        usnInput.addEventListener('input', function(e) {
            this.value = this.value.toUpperCase();
        });
    }

    // Auto-dismiss only non-success alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-success)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});