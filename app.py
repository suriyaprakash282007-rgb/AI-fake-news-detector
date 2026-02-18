from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Fake news indicators
FAKE_INDICATORS = [
    r'\bbreaking\b',
    r'\bshocking\b',
    r'\bunbelievable\b',
    r'\byou won\'t believe\b',
    r'\bthey don\'t want you to know\b',
    r'\bthe truth they\'re hiding\b',
    r'\bwhat they aren\'t telling you\b',
    r'\bexperts are stunned\b',
    r'\bthis will blow your mind\b',
]

# Credibility indicators
CREDIBLE_INDICATORS = [
    r'\baccording to\b',
    r'\bresearch shows\b',
    r'\bstudy finds\b',
    r'\breuters\b',
    r'\bassociated press\b',
    r'\bpeer-reviewed\b',
    r'\bpress release\b',
    r'\bofficial statement\b',
    r'\bexperts say\b',
]

def analyze_text(text):
    """
    Analyze text for fake news indicators.
    
    Args:
        text (str): The news article text to analyze
        
    Returns:
        dict: Analysis results with prediction, confidence, and details
    """
    if not text or len(text.strip()) < 10:
        return {
            "prediction": "Insufficient Data",
            "confidence": 0,
            "message": "Text too short to analyze",
            "details": {
                "fake_indicators_found": [],
                "credible_indicators_found": [],
                "excessive_punctuation": False,
                "excessive_caps": False
            }
        }
    
    text_lower = text.lower()
    
    # Find fake news indicators
    fake_found = []
    for pattern in FAKE_INDICATORS:
        matches = re.findall(pattern, text_lower, re.IGNORECASE)
        if matches:
            fake_found.extend(matches)
    
    # Find credible indicators
    credible_found = []
    for pattern in CREDIBLE_INDICATORS:
        matches = re.findall(pattern, text_lower, re.IGNORECASE)
        if matches:
            credible_found.extend(matches)
    
    # Check for excessive punctuation
    exclamation_count = text.count('!')
    question_count = text.count('?')
    excessive_punctuation = exclamation_count > 3 or question_count > 3
    
    # Check for excessive caps
    words = text.split()
    if len(words) > 0:
        caps_count = sum(1 for word in words if len(word) > 3 and word.isupper())
        excessive_caps = caps_count > len(words) * 0.2  # More than 20% caps
    else:
        excessive_caps = False
    
    # Calculate confidence score
    fake_score = len(fake_found) * 15
    if excessive_punctuation:
        fake_score += 10
    if excessive_caps:
        fake_score += 15
    
    credible_score = len(credible_found) * 15
    
    # Net score (higher = more fake)
    net_score = fake_score - credible_score
    confidence = min(max(50 + net_score, 0), 100)
    
    # Determine prediction
    if confidence >= 65:
        prediction = "Likely Fake"
        message = f"Found {len(fake_found)} suspicious indicator(s)"
    elif confidence <= 35:
        prediction = "Likely Credible"
        message = f"Found {len(credible_found)} credibility indicator(s)"
    else:
        prediction = "Uncertain"
        message = "Mixed signals detected"
    
    return {
        "prediction": prediction,
        "confidence": int(confidence),
        "message": message,
        "details": {
            "fake_indicators_found": list(set(fake_found)),
            "credible_indicators_found": list(set(credible_found)),
            "excessive_punctuation": excessive_punctuation,
            "excessive_caps": excessive_caps
        }
    }

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analyze news text for fake news indicators.
    
    Request JSON:
        {
            "text": "News article text..."
        }
        
    Response JSON:
        {
            "prediction": "Likely Fake" | "Likely Credible" | "Uncertain",
            "confidence": 0-100,
            "message": "Description",
            "details": {...}
        }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                "error": "Missing 'text' field in request"
            }), 400
        
        text = data['text']
        result = analyze_text(text)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            "error": f"Analysis failed: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "AI Fake News Detector",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    import os
    # Debug mode should be disabled in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 'yes')
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
