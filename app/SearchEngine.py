from collections import defaultdict
from math import log
import string
import os
import json

def update_url_scores(old: dict[str, float], new: dict[str, float]) -> None:
    for url, score in new.items():
        if url in old:
            old[url] += score
        else:
            old[url] = score
    return old

def normalize_string(input_string: str) -> str:
    translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    string_without_punc = input_string.translate(translation_table)
    string_without_double_spaces = ' '.join(string_without_punc.split())
    return string_without_double_spaces.lower()


class SearchEngine:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self._index: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self._documents: dict[str, dict[str, str]] = {}
        self.k1 = k1
        self.b = b

    @property
    def posts(self) -> list[str]:
        return list(self._documents.keys())

    @property
    def number_of_documents(self) -> int:
        return len(self._documents)

    @property
    def avdl(self) -> float:
        return sum(len(d['content']) for d in self._documents.values()) / len(self._documents)

    def idf(self, kw: str) -> float:
        N = self.number_of_documents
        n_kw = len(self.get_urls(kw))
        return log((N - n_kw + 0.5) / (n_kw + 0.5) + 1)

    def bm25(self, kw: str) -> dict[str, float]:
        result = {}
        idf_score = self.idf(kw)
        avdl = self.avdl
        for url, freq in self.get_urls(kw).items():
            numerator = freq * (self.k1 + 1)
            denominator = freq + self.k1 * (
                1 - self.b + self.b * len(self._documents[url]['content']) / avdl
            )
            result[url] = idf_score * numerator / denominator
        return result

    def search(self, query: str) -> list[dict]:
        keywords = normalize_string(query).split(" ")
        url_scores: dict[str, float] = {}
        for kw in keywords:
            kw_urls_score = self.bm25(kw)
            url_scores = update_url_scores(url_scores, kw_urls_score)

        results = []
        for url, score in url_scores.items():
            if url in self._documents:
                title = self._documents[url]['title']
                content = self._documents[url]['content']
                results.append({
                    'url': url,
                    'score': score,
                    'title': title,
                    'content': content
                })
        return results


    def index(self, url: str, title: str, content: str) -> None:
        self._documents[url] = {"title": title, "content": content}
        words = normalize_string(f"{title} {content}").split(" ")
        for word in words:
            self._index[word][url] += 1

    def bulk_index(self, documents: list[tuple[str, str, str]]):
        for url, title, content in documents:
            self.index(url, title, content)

    def get_urls(self, keyword: str) -> dict[str, int]:
        keyword = normalize_string(keyword)
        return self._index[keyword]
    
    def index_json_files(self, json_folder: str):
        documents = []
        for json_file in os.listdir(json_folder):
            if json_file.endswith(".json"):
                with open(os.path.join(json_folder, json_file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    if isinstance(data, list):
                        for item in data:
                            url = item['url']
                            title = item['title']  
                            content = item['content']
                            documents.append((url, title, content))
                    else:
                        url = data['url']
                        title = data['title']  
                        content = data['content']
                        documents.append((url, title, content))

        self.bulk_index(documents)