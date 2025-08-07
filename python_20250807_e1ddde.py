# weather_sentiment.py
from transformers import pipeline
import re

class WeatherSentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            top_k=None
        )
    
    def clean_text(self, text):
        """Clean weather report text"""
        text = re.sub(r'[^\w\s.,;!?]', '', text)  # Remove special chars
        text = re.sub(r'\s+', ' ', text).strip()   # Remove extra spaces
        return text
    
    def analyze(self, report):
        """Analyze sentiment of a weather report"""
        if not report.strip():
            return {"error": "Empty report provided"}
        
        cleaned_report = self.clean_text(report)
        results = self.classifier(cleaned_report)[0]
        
        # Find the highest confidence sentiment
        primary_sentiment = max(results, key=lambda x: x['score'])
        
        return {
            "report": cleaned_report,
            "sentiment": primary_sentiment['label'],
            "confidence": round(primary_sentiment['score'], 4),
            "all_scores": {res['label']: round(res['score'], 4) for res in results}
        }

if __name__ == "__main__":
    analyzer = WeatherSentimentAnalyzer()
    
    print("🌤️ Weather Report Sentiment Analyzer 🌩️")
    print("Enter/Paste weather reports (Ctrl+D/Ctrl+Z to finish):")
    
    reports = []
    try:
        while True:
            line = input()
            reports.append(line)
    except EOFError:
        pass
    
    full_report = " ".join(reports)
    
    if not full_report.strip():
        print("\n❌ No input provided!")
    else:
        result = analyzer.analyze(full_report)
        print("\n📊 Analysis Results:")
        print(f"📝 Report: {result['report'][:100]}...")
        print(f"🎭 Primary Sentiment: {result['sentiment']}")
        print(f"✅ Confidence: {result['confidence']:.2%}")
        print("\n📈 Detailed Scores:")
        for sentiment, score in result['all_scores'].items():
            print(f"- {sentiment.capitalize()}: {score:.2%}")