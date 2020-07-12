import re
import string

from collections import Counter


class AutoCorrect(object):
    def __init__(self):
        try:
            words_from_corpus = self.fetch_words_from_corpus('./data/big.txt')
            self.vocabulary = list(words_from_corpus)
            words_counts = Counter(words_from_corpus)
            total_word_counts = float(sum(words_counts.values()))
            self.probabilities = {word: words_counts[word] / total_word_counts for word in words_counts.keys()}
        except FileNotFoundError:
            raise Exception('Could not open corpus file. Download from and store in the ')

    @staticmethod
    def fetch_words_from_corpus(file_name: str) -> set:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            words = []
            for line in lines:
                words += re.findall(r'\w+', line.lower())
        return set(words)

    @staticmethod
    def _split(word: str) -> list:
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]

    def _delete(self, word: str) -> list:
        return [l + r[1:] for l, r in self._split(word) if r]

    def _swap(self, word: str) -> list:
        return [l + r[1] + r[0] + r[2:] for l, r in self._split(word) if len(r) > 1]

    def _replace(self, word: str) -> list:
        letters = string.ascii_lowercase
        return [l + c + r[1:] for l, r in self._split(word) if r for c in letters]

    def _insert(self, word: str) -> list:
        letters = string.ascii_lowercase
        return [l + c + r for l, r in self._split(word) for c in letters]

    def _level_one_edits(self, word: str) -> set:
        return set(self._delete(word) + self._swap(word) + self._replace(word) + self._insert(word))

    def _level_two_edits(self, word: str) -> set:
        return set(e2 for e1 in self._level_one_edits(word) for e2 in self._level_one_edits(e1))

    def check(self, word: str) -> list:
        if word in self.vocabulary:
            return [{'word': word, 'probability': 1}]

        suggestions = self._level_one_edits(word) or self._level_two_edits(word) or [word]
        best_guesses = [w for w in suggestions if w in self.vocabulary]
        return sorted([{'word': w, 'probability': self.probabilities[w]} for w in best_guesses], key=lambda tup: tup['probability'], reverse=True)

