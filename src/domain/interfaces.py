from abc import ABC, abstractmethod
from typing import Iterable, Optional, Tuple
from .models import NewsArticle, SentimentResult

class NewsFetcher(ABC):
    @abstractmethod
    def fetch(self, query: str, from_iso: str, to_iso: str) -> Iterable[NewsArticle]:
        ...

class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text: str) -> SentimentResult:
        ...

class Loader(ABC):
    @abstractmethod
    def load_news(self, items: Iterable[Tuple[NewsArticle, Optional[SentimentResult]]]) -> int:
        ...
