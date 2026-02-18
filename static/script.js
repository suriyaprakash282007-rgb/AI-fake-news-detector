// AI Fake News Detector - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('analyzeForm');
    const newsText = document.getElementById('newsText');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resultsCard = document.getElementById('resultsCard');

    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const text = newsText.value.trim();
        
        if (text.length < 10) {
            alert('Please enter at least 10 characters for analysis.');
            return;
        }
        
        // Show loading state
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Analyzing...';
        
        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text })
            });
            
            if (!response.ok) {
                throw new Error('Analysis failed');
            }
            
            const result = await response.json();
            displayResults(result);
            
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during analysis. Please try again.');
        } finally {
            // Reset button state
            analyzeBtn.disabled = false;
            analyzeBtn.innerHTML = '<i class="fas fa-search"></i> Analyze Article';
        }
    });
    
    // Display results function
    function displayResults(result) {
        const { prediction, confidence, message, details } = result;
        
        // Show results card with animation
        resultsCard.style.display = 'block';
        resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        
        // Update prediction text
        const predictionText = document.getElementById('predictionText');
        predictionText.textContent = prediction;
        
        // Set color based on prediction
        predictionText.className = '';
        if (prediction === 'Likely Fake') {
            predictionText.classList.add('fake');
        } else if (prediction === 'Likely Credible') {
            predictionText.classList.add('credible');
        } else {
            predictionText.classList.add('uncertain');
        }
        
        // Update confidence bar
        const confidenceBar = document.getElementById('confidenceBar');
        const confidenceText = document.getElementById('confidenceText');
        
        confidenceBar.style.width = confidence + '%';
        confidenceBar.setAttribute('aria-valuenow', confidence);
        confidenceText.textContent = confidence + '% Confidence';
        
        // Set progress bar color based on confidence
        confidenceBar.className = 'progress-bar';
        if (confidence >= 65) {
            confidenceBar.classList.add('bg-danger');
        } else if (confidence <= 35) {
            confidenceBar.classList.add('bg-success');
        } else {
            confidenceBar.classList.add('bg-warning');
        }
        
        // Update message
        document.getElementById('messageText').textContent = message;
        
        // Update header color
        const resultsHeader = document.getElementById('resultsHeader');
        resultsHeader.className = 'card-header';
        if (confidence >= 65) {
            resultsHeader.classList.add('bg-danger', 'text-white');
        } else if (confidence <= 35) {
            resultsHeader.classList.add('bg-success', 'text-white');
        } else {
            resultsHeader.classList.add('bg-warning', 'text-dark');
        }
        
        // Display fake indicators
        const fakeIndicatorsList = document.getElementById('fakeIndicatorsList');
        fakeIndicatorsList.innerHTML = '';
        
        if (details.fake_indicators_found && details.fake_indicators_found.length > 0) {
            details.fake_indicators_found.forEach(indicator => {
                const li = document.createElement('li');
                li.textContent = indicator;
                fakeIndicatorsList.appendChild(li);
            });
        } else {
            fakeIndicatorsList.innerHTML = '<li class="text-muted">None detected</li>';
        }
        
        // Display credible indicators
        const credibleIndicatorsList = document.getElementById('credibleIndicatorsList');
        credibleIndicatorsList.innerHTML = '';
        
        if (details.credible_indicators_found && details.credible_indicators_found.length > 0) {
            details.credible_indicators_found.forEach(indicator => {
                const li = document.createElement('li');
                li.textContent = indicator;
                credibleIndicatorsList.appendChild(li);
            });
        } else {
            credibleIndicatorsList.innerHTML = '<li class="text-muted">None detected</li>';
        }
        
        // Display punctuation status
        const punctuationStatus = document.getElementById('punctuationStatus');
        if (details.excessive_punctuation) {
            punctuationStatus.innerHTML = '<i class="fas fa-times-circle text-danger"></i> Yes';
        } else {
            punctuationStatus.innerHTML = '<i class="fas fa-check-circle text-success"></i> No';
        }
        
        // Display caps status
        const capsStatus = document.getElementById('capsStatus');
        if (details.excessive_caps) {
            capsStatus.innerHTML = '<i class="fas fa-times-circle text-danger"></i> Yes';
        } else {
            capsStatus.innerHTML = '<i class="fas fa-check-circle text-success"></i> No';
        }
    }
});
