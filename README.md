Weather Report Sentiment Analyzer

https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/License-MIT-green
https://img.shields.io/badge/Powered%2520by-Transformers-orange

A Python tool that analyzes sentiment in weather reports using state-of-the-art NLP models. This application classifies weather forecasts as positive or negative and provides confidence scores for each sentiment category.
Features

    📊 Sentiment analysis of weather reports (POSITIVE/NEGATIVE)

    🔢 Confidence percentages for both sentiment categories

    ✨ Text cleaning and preprocessing

    📈 Detailed sentiment breakdown

    💻 Interactive command-line interface

    ⚡ Fast inference using DistilBERT model

Installation

    Clone the repository:

bash

git clone https://github.com/GTVSOFT/Weather-Report-Sentiment-Analyze.git
cd Weather-Report-Sentiment-Analyze

    Install dependencies:

bash

pip install -r requirements.txt

Usage
Command Line Interface
bash

python weather_sentiment.py

Then enter or paste your weather report text. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when finished.
Programmatic Usage
python

from weather_sentiment import WeatherSentimentAnalyzer

analyzer = WeatherSentimentAnalyzer()
report = "Sunny skies with a gentle breeze expected throughout the day. Perfect weather for outdoor activities."

result = analyzer.analyze(report)
print(f"Primary Sentiment: {result['sentiment']}")
print(f"Confidence: {result['confidence']:.2%}")

Example Output
text

🌤️ Weather Report Sentiment Analyzer 🌩️
Enter/Paste weather reports (Ctrl+D/Ctrl+Z to finish):
Severe thunderstorms expected tonight with possible hail and damaging winds.
Residents should take precautions and stay indoors.

📊 Analysis Results:
📝 Report: Severe thunderstorms expected tonight with possible hail and damaging winds Residents should take prec...
🎭 Primary Sentiment: NEGATIVE
✅ Confidence: 98.76%

📈 Detailed Scores:
- Negative: 98.76%
- Positive: 1.24%

API Response Structure

The analyze() method returns a dictionary with:
python

{
    "report": "Cleaned text of the weather report",
    "sentiment": "PRIMARY_SENTIMENT",  # Either 'POSITIVE' or 'NEGATIVE'
    "confidence": 0.9876,             # Confidence score of primary sentiment
    "all_scores": {
        "NEGATIVE": 0.9876,
        "POSITIVE": 0.0124
    }
}

Dependencies

    Python 3.8+

    transformers==4.41.2

    torch==2.3.0

Model Information

Uses the distilbert-base-uncased-finetuned-sst-2-english model from Hugging Face Transformers:

    Distilled version of BERT

    Fine-tuned on Stanford Sentiment Treebank (SST-2)

    97% accuracy on SST-2 test set

    Lightweight and fast inference

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

    Fork the repository

    Create your feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -am 'Add some feature')

    Push to the branch (git push origin feature/your-feature)

    Open a pull request

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author :Amos Meremu

GitHub: GTVSOFT

Project Repository: https://github.com/GTVSOFT/Weather-Report-Sentiment-Analyze

Enjoy analyzing weather sentiments! 🌞⛅🌧️⛈️
