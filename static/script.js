// AI Fake News Detector - Frontend JavaScript

// DOM Elements
const analyzeForm = document.getElementById('analyzeForm');
const newsText = document.getElementById('newsText');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultsCard = document.getElementById('resultsCard');
const loadingSpinner = document.getElementById('loadingSpinner');
const analyzeAnotherBtn = document.getElementById('analyzeAnotherBtn');

// Result elements
const prediction = document.getElementById('prediction');
const confidenceBar = document.getElementById('confidenceBar');
const confidenceText = document.getElementById('confidenceText');
const resultMessage = document.getElementById('resultMessage');
const resultHeader = document.getElementById('resultHeader');
const fakeIndicators = document.getElementById('fakeIndicators');
const credibleIndicators = document.getElementById('credibleIndicators');
const additionalFlags = document.getElementById('additionalFlags');

// Form submission handler
analyzeForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const text = newsText.value.trim();
    
    // Validation
    if (!text) {
        showError('Please enter some text to analyze');
        return;
    }
    
    if (text.length < 10) {
        showError('Text is too short. Please enter at least 10 characters.');
        return;
    }
    
    // Show loading state
    showLoading();
    
    try {
        // Make API request
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        // Display results
        displayResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        showError('An error occurred during analysis. Please try again.');
        hideLoading();
    }
});

// Analyze Another button handler
analyzeAnotherBtn.addEventListener('click', () => {
    resetForm();
});

// Display results function
function displayResults(data) {
    hideLoading();
    
    // Set prediction
    prediction.textContent = data.prediction;
    
    // Set prediction color
    prediction.className = '';
    if (data.prediction.includes('Fake')) {
        prediction.classList.add('text-danger');
        resultHeader.className = 'card-header bg-danger text-white';
    } else if (data.prediction.includes('Credible')) {
        prediction.classList.add('text-success');
        resultHeader.className = 'card-header bg-success text-white';
    } else {
        prediction.classList.add('text-warning');
        resultHeader.className = 'card-header bg-warning';
    }
    
    // Set confidence bar
    confidenceBar.style.width = `${data.confidence}%`;
    confidenceBar.setAttribute('aria-valuenow', data.confidence);
    confidenceText.textContent = `${data.confidence}% Confidence`;
    
    // Set confidence bar color
    confidenceBar.className = 'progress-bar';
    if (data.confidence >= 70) {
        if (data.prediction.includes('Fake')) {
            confidenceBar.classList.add('bg-danger');
        } else {
            confidenceBar.classList.add('bg-success');
        }
    } else {
        confidenceBar.classList.add('bg-warning');
    }
    
    // Set message
    resultMessage.textContent = data.message;
    resultMessage.className = 'alert';
    if (data.prediction.includes('Fake')) {
        resultMessage.classList.add('alert-danger');
    } else if (data.prediction.includes('Credible')) {
        resultMessage.classList.add('alert-success');
    } else {
        resultMessage.classList.add('alert-warning');
    }
    
    // Display fake indicators
    fakeIndicators.innerHTML = '';
    if (data.details.fake_indicators_found && data.details.fake_indicators_found.length > 0) {
        data.details.fake_indicators_found.forEach(indicator => {
            const li = document.createElement('li');
            li.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${escapeHtml(indicator)}`;
            fakeIndicators.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.innerHTML = '<i class="fas fa-check"></i> None found';
        li.style.color = '#6c757d';
        fakeIndicators.appendChild(li);
    }
    
    // Display credible indicators
    credibleIndicators.innerHTML = '';
    if (data.details.credible_indicators_found && data.details.credible_indicators_found.length > 0) {
        data.details.credible_indicators_found.forEach(indicator => {
            const li = document.createElement('li');
            li.innerHTML = `<i class="fas fa-check-circle"></i> ${escapeHtml(indicator)}`;
            credibleIndicators.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.innerHTML = '<i class="fas fa-times"></i> None found';
        li.style.color = '#6c757d';
        credibleIndicators.appendChild(li);
    }
    
    // Display additional flags
    additionalFlags.innerHTML = '';
    const flags = [];
    
    if (data.details.excessive_punctuation) {
        flags.push('Excessive punctuation detected');
    }
    
    if (data.details.excessive_caps) {
        flags.push('Excessive capitalization detected');
    }
    
    if (flags.length > 0) {
        flags.forEach(flag => {
            const li = document.createElement('li');
            li.innerHTML = `<i class="fas fa-flag text-warning"></i> ${escapeHtml(flag)}`;
            additionalFlags.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.innerHTML = '<i class="fas fa-check"></i> None';
        li.style.color = '#6c757d';
        additionalFlags.appendChild(li);
    }
    
    // Show results card
    resultsCard.classList.remove('d-none');
    
    // Scroll to results
    resultsCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Show loading state
function showLoading() {
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
    resultsCard.classList.add('d-none');
    loadingSpinner.classList.remove('d-none');
}

// Hide loading state
function hideLoading() {
    analyzeBtn.disabled = false;
    analyzeBtn.innerHTML = '<i class="fas fa-search"></i> Analyze Article';
    loadingSpinner.classList.add('d-none');
}

// Show error message
function showError(message) {
    alert(message);
}

// Reset form
function resetForm() {
    newsText.value = '';
    resultsCard.classList.add('d-none');
    newsText.focus();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Add enter key handler for textarea (Ctrl+Enter to submit)
newsText.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        analyzeForm.dispatchEvent(new Event('submit'));
    }
});

// Focus on textarea when page loads
window.addEventListener('load', () => {
    newsText.focus();
});
