# 🛡️ AI Fake News Detector

A simple, student-friendly web application that analyzes news articles to detect potential fake news using text pattern analysis.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

## 🔗 Quick Access

**Want to open the app right away?**

1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python app.py` (or use `python start.py` for automatic browser opening)
3. **Click here to open:** 👉 [http://localhost:5000](http://localhost:5000) 👈

> 💡 **Pro Tip:** Run `python start.py` for automatic startup and browser opening!
> 
> 📱 **Multiple Ways to Access:** See [ACCESS_GUIDE.md](ACCESS_GUIDE.md) for all access options (mobile, public URL, etc.)

For detailed instructions, see [QUICK_START.md](QUICK_START.md)

## 📋 Features

- ✅ **Simple Text Analysis** - Paste any news article for instant analysis
- ✅ **Confidence Score** - Get a percentage indicating the likelihood of fake news
- ✅ **Detailed Breakdown** - See which indicators were found
- ✅ **Beautiful UI** - Modern, responsive design with Bootstrap
- ✅ **Fast & Lightweight** - No heavy ML models required

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (with Bootstrap 5)
- JavaScript (Vanilla JS)
- Font Awesome Icons

### Backend
- Python 3.8+
- Flask (Web Framework)
- Flask-CORS (Cross-Origin Support)

## 🚀 Quick Start

### 1. Clone/Download the Project

```bash
cd fake_news_detector
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Navigate to: **http://localhost:5000**

## 📁 Project Structure

```
fake_news_detector/
├── app.py                 # Flask backend & API
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML page
└── static/
    ├── style.css         # Custom CSS styles
    └── script.js         # Frontend JavaScript
```

## 🔍 How It Works

The detector analyzes news text by looking for:

### Fake News Indicators 🚩
- Sensational language ("BREAKING", "SHOCKING")
- Clickbait phrases ("You won't believe")
- Conspiracy markers ("They don't want you to know")
- Excessive punctuation (!!!)
- ALL CAPS text

### Credibility Indicators ✅
- Attribution phrases ("According to", "Research shows")
- Source citations ("Reuters", "Associated Press")
- Academic language ("Peer-reviewed", "Study finds")
- Official references ("Press release", "Official statement")

## 📊 API Endpoints

### POST `/api/analyze`
Analyze news text for authenticity.

**Request:**
```json
{
    "text": "Your news article text here..."
}
```

**Response:**
```json
{
    "prediction": "Likely Fake",
    "confidence": 75,
    "message": "Found 3 suspicious indicator(s)",
    "details": {
        "fake_indicators_found": ["breaking:", "!!!"],
        "credible_indicators_found": [],
        "excessive_punctuation": true,
        "excessive_caps": false
    }
}
```

### GET `/api/health`
Health check endpoint.

## 🎓 For Students

This project is perfect for:
- **College Projects** - Simple to understand and explain
- **AWS Deployment** - Can be easily hosted on EC2/Elastic Beanstalk
- **Resume Building** - Shows full-stack development skills
- **Learning** - Great introduction to Flask and REST APIs

## 🚀 AWS Deployment (Optional)

### Deploy to AWS EC2:

1. Launch an EC2 instance (Ubuntu)
2. SSH into the instance
3. Install Python and dependencies
4. Run the app with: `python app.py`
5. Configure security group to allow port 5000

### Deploy to AWS Elastic Beanstalk:

1. Install AWS EB CLI
2. Run `eb init` to initialize
3. Run `eb create` to deploy
4. Access via the provided URL

## 📝 Future Improvements

- [ ] Add ML-based detection (BERT, LSTM)
- [ ] Database for storing analysis history
- [ ] User authentication
- [ ] Browser extension
- [ ] API rate limiting

## 🤝 Contributing

Feel free to fork and improve this project!

## 📄 License

MIT License - Free for educational use

---

Made with ❤️ for students learning web development
