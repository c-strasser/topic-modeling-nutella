from unittest import TestCase
from utils.data_cleaner import DataCleaner
import pandas as pd
import os
from nltk.corpus import stopwords

class TestDataCleaner(TestCase):


    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.cleaner = DataCleaner('french')
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.corpus_path = os.path.join(current_directory, 'example_data/raw_data.csv')

    def test_get_clean_corpus_from_path(self):
        self.fail()

    def test_get_raw_corpus_from_path(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        actual_number_lines = len(raw_corpus)
        expected_number_lines = 44
        print(raw_corpus)
        self.assertEquals(expected_number_lines, actual_number_lines)

    def test_split_raw_corpus_into_documents(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        documents = self.cleaner.split_raw_corpus_into_documents(raw_corpus)
        actual_number_documents = len(documents)
        expected_number_documents = 2
        print(documents[0])
        print(documents[1])
        self.assertEqual(expected_number_documents, actual_number_documents)

    def test_clean_documents(self):
        self.fail()

    def test_clean_a_document(self):
        self.fail()

    def test_split_document_into_words(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        documents = self.cleaner.split_raw_corpus_into_documents(raw_corpus)
        words = self.cleaner.split_document_into_words(documents[1])
        print(words)
        print(len(words))

    def test_escape_html_characters_in_words(self):
        words = ['je', '<em>', 'mange', '</em>']
        actual_words_without_html = self.cleaner.escape_html_characters_in_words(words)
        expected_words_without_html = ['je', 'mange']
        self.assertListEqual(expected_words_without_html, actual_words_without_html)


    def test_remove_punctuation_in_list_words(self):
        words = self.build_words_example()
        processed_words = self.cleaner.remove_punctuation_in_list_words(words)
        print(processed_words)


    def test_remove_stop_words_in_list_words(self):
        words = self.build_words_example()
        processed_words = self.cleaner.remove_stop_words_in_list_words(words)
        print(processed_words)

    def test_replace_emojis_by_description_in_words(self):
        self.fail()

    def test_lemmatize_words(self):
        words = self.build_words_example()
        words = self.cleaner.remove_punctuation_in_list_words(words)
        words = self.cleaner.remove_stop_words_in_list_words(words)
        processed_words = self.cleaner.lemmatize_words(words)
        print(processed_words)

    def test_remove_url_in_words(self):
        self.fail()

    def test_concatenate_remaining_words(self):
        self.fail()


    def build_words_example(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        documents = self.cleaner.split_raw_corpus_into_documents(raw_corpus)
        words = self.cleaner.split_document_into_words(documents[1])
        return words

    def test_stop_words(self):
        print(stopwords.words('french'))