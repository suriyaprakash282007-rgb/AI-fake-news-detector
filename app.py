from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Fake news indicators
FAKE_INDICATORS = [
    r'\bBREAKING\b',
    r'\bSHOCKING\b',
    r'\bUNBELIEVABLE\b',
    r'\bYOU WON\'T BELIEVE\b',
    r'\bTHEY DON\'T WANT YOU TO KNOW\b',
    r'\bCOVER[\-\s]?UP\b',
    r'\bCONSPIRACY\b',
    r'\bWAKE UP\b',
]

# Credibility indicators
CREDIBLE_INDICATORS = [
    r'\bACCORDING TO\b',
    r'\bRESEARCH SHOWS\b',
    r'\bSTUDY FINDS\b',
    r'\bREUTERS\b',
    r'\bASSOCIATED PRESS\b',
    r'\bAP NEWS\b',
    r'\bPEER[\-\s]?REVIEWED\b',
    r'\bPRESS RELEASE\b',
    r'\bOFFICIAL STATEMENT\b',
    r'\bSOURCE:\b',
]


def analyze_text(text):
    """
    Analyze text for fake news indicators.
    
    Args:
        text (str): The news article text to analyze
        
    Returns:
        dict: Analysis results with prediction, confidence, and details
    """
    text_upper = text.upper()
    
    # Find fake indicators
    fake_found = []
    for pattern in FAKE_INDICATORS:
        matches = re.findall(pattern, text_upper, re.IGNORECASE)
        if matches:
            fake_found.extend([m.lower() for m in matches])
    
    # Find credible indicators
    credible_found = []
    for pattern in CREDIBLE_INDICATORS:
        matches = re.findall(pattern, text_upper, re.IGNORECASE)
        if matches:
            credible_found.extend([m.lower() for m in matches])
    
    # Check for excessive punctuation
    excessive_punctuation = bool(re.search(r'[!?]{3,}', text))
    if excessive_punctuation:
        fake_found.append('excessive punctuation')
    
    # Check for excessive caps (more than 30% of text in caps)
    alpha_chars = [c for c in text if c.isalpha()]
    if alpha_chars:
        caps_ratio = sum(1 for c in alpha_chars if c.isupper()) / len(alpha_chars)
        excessive_caps = caps_ratio > 0.3
    else:
        excessive_caps = False
    
    if excessive_caps:
        fake_found.append('excessive capitals')
    
    # Calculate confidence score
    fake_score = len(set(fake_found))
    credible_score = len(set(credible_found))
    
    # Determine prediction
    if fake_score > credible_score:
        prediction = "Likely Fake"
        confidence = min(50 + (fake_score * 10), 95)
    elif credible_score > fake_score:
        prediction = "Likely Credible"
        confidence = min(50 + (credible_score * 10), 95)
    else:
        prediction = "Uncertain"
        confidence = 50
    
    # Create message
    if fake_score > 0:
        message = f"Found {fake_score} suspicious indicator(s)"
    elif credible_score > 0:
        message = f"Found {credible_score} credibility indicator(s)"
    else:
        message = "No strong indicators found"
    
    return {
        'prediction': prediction,
        'confidence': confidence,
        'message': message,
        'details': {
            'fake_indicators_found': list(set(fake_found)),
            'credible_indicators_found': list(set(credible_found)),
            'excessive_punctuation': excessive_punctuation,
            'excessive_caps': excessive_caps
        }
    }


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to analyze news text.
    
    Expected JSON: {"text": "news article text"}
    Returns: Analysis results
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        if len(text) < 10:
            return jsonify({'error': 'Text is too short for analysis'}), 400
        
        result = analyze_text(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'AI Fake News Detector',
        'version': '1.0.0'
    })


if __name__ == '__main__':
    # Debug mode disabled for security - use environment variable to enable in development
    # Set FLASK_DEBUG=1 environment variable for debugging during development
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
