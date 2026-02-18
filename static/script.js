/**
 * AI Fake News Detector - Frontend JavaScript
 * Handles API calls and UI updates
 */

// DOM Elements
// Inputs
const newsInput = document.getElementById('newsInput');
const imageInput = document.getElementById('imageInput');
const audioInput = document.getElementById('audioInput');
const videoInput = document.getElementById('videoInput');
const aiContentInput = document.getElementById('aiContentInput');
const aiContentType = document.getElementById('aiContentType');
const deepAnalysis = document.getElementById('deepAnalysis');

// Media Text Inputs (for context/description)
const imageText = document.getElementById('imageText');
const audioText = document.getElementById('audioText');
const videoText = document.getElementById('videoText');

// Controls
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const loadingSpinner = document.getElementById('loadingSpinner');

// Results
const resultCard = document.getElementById('resultCard');
const resultHeader = document.getElementById('resultHeader');
const predictionBadge = document.getElementById('predictionBadge');
const confidenceBar = document.getElementById('confidenceBar');
const confidenceText = document.getElementById('confidenceText');
const messageAlert = document.getElementById('messageAlert');
const messageText = document.getElementById('messageText');
const detailsBody = document.getElementById('detailsBody');

// API Base URLs
const API_URL_TEXT = '/api/analyze/text';
const API_URL_MEDIA = '/api/analyze/media';
const API_URL_AI = '/api/analyze/ai-detection';

/**
 * Handle Tab Switching to update active input type context
 */
let currentType = 'text';

document.querySelectorAll('button[data-bs-toggle="tab"]').forEach(tab => {
    tab.addEventListener('shown.bs.tab', (event) => {
        // Use the ID format "type-tab" (e.g., text-tab, image-tab)
        currentType = event.target.id.replace('-tab', '');
        hideResult();
        
        // Update Button Text
        let typeName = currentType.charAt(0).toUpperCase() + currentType.slice(1);
        analyzeBtn.innerHTML = `<i class="fas fa-search me-2"></i>Analyze ${typeName}`;
    });
});

/**
 * File Preview Handlers
 */
if (imageInput) {
    imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const preview = document.getElementById('imagePreview');
                preview.querySelector('img').src = e.target.result;
                preview.classList.remove('d-none');
            }
            reader.readAsDataURL(file);
        }
    });
}

if (audioInput) {
    audioInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const url = URL.createObjectURL(file);
            const preview = document.getElementById('audioPreview');
            preview.querySelector('audio').src = url;
            preview.classList.remove('d-none');
        }
    });
}

if (videoInput) {
    videoInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const url = URL.createObjectURL(file);
            const preview = document.getElementById('videoPreview');
            preview.querySelector('video').src = url;
            preview.classList.remove('d-none');
        }
    });
}

/**
 * Main Analysis Function
 */
async function analyzeContent() {
    showLoading(true);
    hideResult();
    
    try {
        let response;
        
        if (currentType === 'text') {
            const text = newsInput.value.trim();
            if (text.length < 20) {
                throw new Error('Please enter at least 20 characters for text analysis.');
            }
            
            response = await fetch(API_URL_TEXT, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            
        } else if (currentType === 'ai') {
            // AI Detection Analysis
            const content = aiContentInput ? aiContentInput.value.trim() : '';
            if (content.length < 50) {
                throw new Error('Please enter at least 50 characters for accurate AI detection.');
            }
            
            const contentType = aiContentType ? aiContentType.value : 'text';
            const deepMode = deepAnalysis ? deepAnalysis.checked : true;
            
            response = await fetch(API_URL_AI, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    content: content,
                    content_type: contentType,
                    deep_analysis: deepMode
                })
            });
            
        } else {
            // Handle Media Uploads
            const formData = new FormData();
            let fileInput;
            let contextText = '';
            
            if (currentType === 'image') {
                fileInput = imageInput;
                contextText = imageText ? imageText.value.trim() : '';
            } else if (currentType === 'audio') {
                fileInput = audioInput;
                contextText = audioText ? audioText.value.trim() : '';
            } else if (currentType === 'video') {
                fileInput = videoInput;
                contextText = videoText ? videoText.value.trim() : '';
            }
            
            if (!fileInput || !fileInput.files[0]) {
                throw new Error(`Please upload a ${currentType} file first.`);
            }
            
            formData.append('file', fileInput.files[0]);
            formData.append('type', currentType);
            formData.append('context', contextText);
            
            response = await fetch(API_URL_MEDIA, {
                method: 'POST',
                body: formData
            });
        }
        
        if (!response.ok) throw new Error(`Server Error: ${response.status}`);
        
        const data = await response.json();
        // Check for specific API error
        if (data.error) throw new Error(data.error);
        if (data.prediction === 'Invalid') throw new Error(data.message);
        
        displayResult(data);
        
    } catch (error) {
        showError(error.message);
    } finally {
        showLoading(false);
    }
}

// Update Listeners
analyzeBtn.addEventListener('click', analyzeContent);

/**
 * Display the analysis result 
 * (Updated to handle varied detail structures including AI detection)
 */
function displayResult(data) {
    const prediction = data.prediction;
    const confidence = data.confidence;
    const message = data.message;
    const details = data.details || {};
    
    // Determine styling based on prediction
    let badgeClass, barClass, headerClass, alertClass, icon;
    
    if (prediction.includes('Real') || prediction.includes('Human')) {
        badgeClass = prediction.includes('Human') ? 'badge-human' : 'badge-real';
        barClass = 'progress-bar-real';
        headerClass = prediction.includes('Human') ? 'result-header-human' : 'result-header-real';
        alertClass = 'alert-real';
        icon = prediction.includes('Human') ? '<i class="fas fa-user me-2"></i>' : '<i class="fas fa-check-circle me-2"></i>';
    } else if (prediction.includes('Fake') || prediction.includes('AI-Generated')) {
        badgeClass = prediction.includes('AI') ? 'badge-ai' : 'badge-fake';
        barClass = prediction.includes('AI') ? 'progress-bar-ai' : 'progress-bar-fake';
        headerClass = prediction.includes('AI') ? 'result-header-ai' : 'result-header-fake';
        alertClass = prediction.includes('AI') ? 'alert-ai' : 'alert-fake';
        icon = prediction.includes('AI') ? '<i class="fas fa-robot me-2"></i>' : '<i class="fas fa-times-circle me-2"></i>';
    } else {
        badgeClass = 'badge-uncertain';
        barClass = 'progress-bar-uncertain';
        headerClass = 'result-header-uncertain';
        alertClass = 'alert-uncertain';
        icon = '<i class="fas fa-question-circle me-2"></i>';
    }
    
    // Update prediction badge
    predictionBadge.className = `badge fs-4 px-4 py-3 ${badgeClass}`;
    predictionBadge.innerHTML = icon + prediction;
    
    // Update result header
    resultHeader.className = `card-header ${headerClass}`;
    
    // Animate confidence bar
    confidenceBar.className = `progress-bar progress-bar-striped progress-bar-animated ${barClass}`;
    confidenceBar.style.width = '0%';
    setTimeout(() => {
        confidenceBar.style.width = `${confidence}%`;
        confidenceText.textContent = `${confidence}%`;
    }, 100);
    
    // Update message alert
    messageAlert.className = `alert ${alertClass}`;
    messageText.textContent = message;
    
    // Build details HTML dynamically
    let detailsHTML = '';
    
    // Add AI vs Human score meter if available
    if (details.ai_score !== undefined && details.human_score !== undefined) {
        detailsHTML += `
        <div class="ai-score-meter">
            <span class="score-label ai"><i class="fas fa-robot me-1"></i>AI: ${details.ai_score}%</span>
            <div class="score-bar">
                <div class="score-bar-fill ai" style="width: ${details.ai_score}%"></div>
            </div>
            <span class="score-label human"><i class="fas fa-user me-1"></i>Human: ${details.human_score}%</span>
        </div>
        <div class="mb-3">
            <small class="text-muted">
                <i class="fas fa-info-circle me-1"></i>
                Content Type: <strong>${details.content_type || 'text'}</strong> | 
                AI Patterns: <strong>${details.ai_patterns_found || 0}</strong> | 
                Human Patterns: <strong>${details.human_patterns_found || 0}</strong>
            </small>
        </div>`;
    }
    
    detailsHTML += '<ul class="details-list">';
    
    // Handle Text Details
    if (details.fake_indicators_found?.length) {
        detailsHTML += `<li class="indicator-fake"><strong>Suspicious Terms:</strong> <br>${details.fake_indicators_found.join(', ')}</li>`;
    }
    if (details.credible_indicators_found?.length) {
        detailsHTML += `<li class="indicator-credible"><strong>Credible Terms:</strong> <br>${details.credible_indicators_found.join(', ')}</li>`;
    }
    
    // Handle Media Details (Generic key-value display)
    if (details.analysis_points) {
        details.analysis_points.forEach(point => {
             // Check if it's a separator line
             if (point.startsWith('---')) {
                 detailsHTML += `<li class="separator-item"><strong>${point.replace(/---/g, '').trim()}</strong></li>`;
             } else {
                 // Determine class based on emoji/icon in the point
                 let itemClass = 'indicator-neutral';
                 if (point.includes('🚨') || point.includes('⚠️') || point.includes('🤖')) {
                     itemClass = prediction.includes('AI') ? 'indicator-ai' : 'indicator-fake';
                 } else if (point.includes('✅') || point.includes('👤')) {
                     itemClass = 'indicator-credible';
                 } else if (prediction.includes('Fake') || prediction.includes('AI')) {
                     itemClass = prediction.includes('AI') ? 'indicator-ai' : 'indicator-fake';
                 } else if (prediction.includes('Real') || prediction.includes('Human')) {
                     itemClass = 'indicator-credible';
                 }
                 
                 detailsHTML += `<li class="${itemClass}">
                    <i class="fas fa-microchip me-2"></i>${point}
                </li>`;
             }
        });
    }
    
    detailsHTML += '</ul>';
    
    // Handle Detailed Reasons (for fake media detection)
    if (details.detailed_reasons && details.detailed_reasons.length > 0) {
        detailsHTML += `
        <div class="detailed-reasons-section mt-4">
            <h6 class="text-danger mb-3">
                <i class="fas fa-exclamation-triangle me-2"></i>Detailed Analysis Report
            </h6>
            <div class="accordion" id="reasonsAccordion">
        `;
        
        details.detailed_reasons.forEach((reason, index) => {
            detailsHTML += `
            <div class="accordion-item reason-card">
                <h2 class="accordion-header">
                    <button class="accordion-button ${index > 0 ? 'collapsed' : ''}" type="button" 
                            data-bs-toggle="collapse" data-bs-target="#reason${index}">
                        <i class="fas fa-search-minus me-2 text-danger"></i>
                        <strong>${reason.title}</strong>
                    </button>
                </h2>
                <div id="reason${index}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" 
                     data-bs-parent="#reasonsAccordion">
                    <div class="accordion-body">
                        <div class="explanation-box mb-3">
                            <h6 class="text-primary"><i class="fas fa-info-circle me-1"></i> Why This Matters:</h6>
                            <p class="mb-0">${reason.explanation}</p>
                        </div>
                        <div class="technical-box">
                            <h6 class="text-secondary"><i class="fas fa-cog me-1"></i> Technical Details:</h6>
                            <code class="technical-code">${reason.technical}</code>
                        </div>
                    </div>
                </div>
            </div>
            `;
        });
        
        detailsHTML += `</div></div>`;
    }
    
    // Handle specific text heuristic details
    if (details.excessive_punctuation) {
        detailsHTML += `<div class="alert alert-warning mt-3"><i class="fas fa-exclamation me-2"></i><strong>Excessive Punctuation:</strong> Sensationalism detected.</div>`;
    }
    if (details.excessive_caps) {
        detailsHTML += `<div class="alert alert-warning mt-3"><i class="fas fa-font me-2"></i><strong>Excessive Caps:</strong> Aggressive styling detected.</div>`;
    }

    // Default "None found"
    if (detailsHTML === '<ul class="details-list">') {
         detailsHTML += `<li><i class="fas fa-info-circle me-2"></i>No specific anomalies detected.</li>`;
    }

    detailsHTML += '</ul>';
    detailsBody.innerHTML = detailsHTML;
    
    // Show result card
    resultCard.classList.remove('d-none');
}

/**
 * Show error message
 */
function showError(message) {
    const data = {
        prediction: 'Error',
        confidence: 0,
        message: message,
        details: {}
    };
    
    predictionBadge.className = 'badge fs-4 px-4 py-3 badge-error';
    predictionBadge.innerHTML = '<i class="fas fa-exclamation-triangle me-2"></i>Error';
    
    resultHeader.className = 'card-header bg-secondary text-white';
    
    confidenceBar.style.width = '0%';
    confidenceText.textContent = '0%';
    
    messageAlert.className = 'alert alert-secondary';
    messageText.textContent = message;
    
    detailsBody.innerHTML = '<p class="text-muted mb-0">No analysis details available.</p>';
    
    resultCard.classList.remove('d-none');
}

/**
 * Show/hide loading spinner
 */
function showLoading(show) {
    if (show) {
        loadingSpinner.classList.remove('d-none');
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
    } else {
        loadingSpinner.classList.add('d-none');
        analyzeBtn.disabled = false;
        let typeName = currentType.charAt(0).toUpperCase() + currentType.slice(1);
        analyzeBtn.innerHTML = `<i class="fas fa-search me-2"></i>Analyze ${typeName}`;
    }
}

/**
 * Hide result card
 */
function hideResult() {
    resultCard.classList.add('d-none');
}

/**
 * Clear all inputs and results
 */
function clearAll() {
    if(newsInput) newsInput.value = '';
    if(imageInput) imageInput.value = '';
    if(audioInput) audioInput.value = '';
    if(videoInput) videoInput.value = '';
    if(aiContentInput) aiContentInput.value = '';
    
    // Clear text context fields
    if(imageText) imageText.value = '';
    if(audioText) audioText.value = '';
    if(videoText) videoText.value = '';
    
    // Reset AI detection options
    if(aiContentType) aiContentType.selectedIndex = 0;
    if(deepAnalysis) deepAnalysis.checked = true;
    
    const imgPreview = document.getElementById('imagePreview');
    if(imgPreview) imgPreview.classList.add('d-none');
    
    const audioPreview = document.getElementById('audioPreview');
    if(audioPreview) audioPreview.classList.add('d-none');
    
    const videoPreview = document.getElementById('videoPreview');
    if(videoPreview) videoPreview.classList.add('d-none');
    
    hideResult();
    if(newsInput && currentType === 'text') newsInput.focus();
}

// Event Listeners
clearBtn.addEventListener('click', clearAll);

// Allow Enter + Ctrl to submit for text
if(newsInput) {
    newsInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && e.ctrlKey && currentType === 'text') {
            analyzeContent();
        }
    });
}

// Console message for developers
console.log('%c🛡️ GPT-5.2-Codex Active', 'font-size: 20px; font-weight: bold; color: #4361ee;');
console.log('%cMulti-Modal Neural Engine Initialized...', 'color: #666;');
