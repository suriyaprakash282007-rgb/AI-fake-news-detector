import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("🚀 Starting Model Training...")

# 1. Create a dataset (In a real project, this would be loaded from a CSV)
# We use a mix of real and fake news examples for training
data = {
    'text': [
        # FAKE NEWS EXAMPLES
        "BREAKING: Aliens found in Area 51, government confirms!",
        "You won't believe this miracle cure for all diseases!",
        "Secret society controls the world economy, insider reveals.",
        "Scientists admit climate change is a hoax created by the government.",
        "Pop star secretly an alien reptile, video proof inside!",
        "Lottery winner reveals secret hack to win every time.",
        "Doctors hate this one weird trick to lose 50 lbs in a day.",
        "NASA confirms Earth is actually flat, satellite images were faked.",
        "Government to ban all vegetables by 2025, sources say.",
        "Drinking bleach cures the common cold, verified by anonymous doctor.",
        "SHOCKING: The moon is a hologram projection.",
        "Celebrity admits to being a clone in leaked audio tape.",
        "Water turns frogs gay, massive cover-up exposed.",
        "Ancient civilization found living under Antarctica ice wall.",
        "Billionaires are planning to leave Earth tomorrow.",
        
        # REAL NEWS EXAMPLES
        "NASA launches new rover to explore Mars surface.",
        "Stock market closes higher as tech shares rally.",
        "Study finds regular exercise improves cardiovascular health.",
        "Government passes new infrastructure bill to improve roads.",
        "Researchers discover new species of butterfly in the Amazon.",
        "Climate change report indicates rising global temperatures.",
        "Local election results announced, voter turnout increases.",
        "World Health Organization updates guidelines on flu vaccination.",
        "Tech giant releases new smartphone with advanced camera features.",
        "Scientists express concern over melting polar ice caps.",
        "Inflation rates stabilize after months of economic volatility.",
        "Education board approves new curriculum for high schools.",
        "New public park opens in the city center next week.",
        "Museum announces exhibition of ancient Egyptian artifacts.",
        "International summit focuses on renewable energy solutions."
    ],
    'label': [
        # 0 = FAKE, 1 = REAL
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# 3. Create a Pipeline (TF-IDF + Logistic Regression)
# This matches the "Machine Learning Model" requirements
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_df=0.7)),
    ('clf', LogisticRegression(random_state=42))
])

# 4. Train the Model
print("🧠 Training the model (Logistic Regression)...")
pipeline.fit(X_train, y_train)

# 5. Evaluate
predictions = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# 6. Save the Model
model_filename = "fake_news_model.pkl"
joblib.dump(pipeline, model_filename)
print(f"💾 Model saved to {model_filename}")

print("\nExample Prediction:")
test_news = "Scientists discover water on Mars"
pred = pipeline.predict([test_news])[0]
prob = pipeline.predict_proba([test_news])[0]
print(f"News: '{test_news}'")
print(f"Result: {'Real' if pred == 1 else 'Fake'}")
print(f"Confidence: {max(prob) * 100:.2f}%")
