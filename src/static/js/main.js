/**
 * DevOps Demo App - Main JavaScript
 * =================================
 * Handles client-side interactivity and real-time updates.
 */

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 DevOps Demo App initialized');
    
    // Initialize features
    initLiveTime();
    initCardAnimations();
    initHealthCheck();
});

/**
 * Live Server Time Update
 * Updates the server time display every second
 */
function initLiveTime() {
    const timeElement = document.getElementById('server-time');
    if (!timeElement) return;
    
    function updateTime() {
        const now = new Date();
        const formatted = now.toISOString().slice(0, 19).replace('T', ' ');
        timeElement.textContent = formatted;
    }
    
    // Update every second
    setInterval(updateTime, 1000);
}

/**
 * Card Hover Animations
 * Adds subtle parallax effect on card hover
 */
function initCardAnimations() {
    const cards = document.querySelectorAll('.info-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px) scale(1.01)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

/**
 * Health Check Indicator
 * Periodically checks the health endpoint
 */
function initHealthCheck() {
    const statusBadge = document.querySelector('.status-badge');
    if (!statusBadge) return;
    
    async function checkHealth() {
        try {
            const response = await fetch('/health');
            const data = await response.json();
            
            if (data.status === 'healthy') {
                statusBadge.classList.remove('unhealthy');
                statusBadge.classList.add('healthy');
            } else {
                statusBadge.classList.remove('healthy');
                statusBadge.classList.add('unhealthy');
            }
        } catch (error) {
            console.error('Health check failed:', error);
            statusBadge.classList.remove('healthy');
            statusBadge.classList.add('unhealthy');
        }
    }
    
    // Check health every 30 seconds
    setInterval(checkHealth, 30000);
}

/**
 * Utility: Format date/time
 */
function formatDateTime(date) {
    return date.toLocaleString('en-US', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    });
}

/**
 * Utility: Copy to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log('Copied to clipboard:', text);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}
