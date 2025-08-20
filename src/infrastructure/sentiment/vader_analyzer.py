from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ...domain.models import SentimentResult

class VaderAnalyzer:
    def __init__(self):
        self._analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> SentimentResult:
        scores = self._analyzer.polarity_scores(text or "")
        comp = scores.get("compound", 0.0)
        if comp >= 0.05:
            label = "pos"
        elif comp <= -0.05:
            label = "neg"
        else:
            label = "neu"
        return SentimentResult(label=label, score=float(comp))
