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


    def test_get_clean_documents_from_corpus_path(self):
        self.fail()

    def test_get_raw_documents_from_corpus_path(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        actual_number_documents = len(documents)
        expected_number_documents = 2
        self.assertEqual(expected_number_documents, actual_number_documents)

    def test_get_raw_corpus_from_path(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        actual_number_lines = len(raw_corpus)
        expected_number_lines = 44
        self.assertEquals(expected_number_lines, actual_number_lines)

    def test_split_raw_corpus_into_documents(self):
        raw_corpus = self.cleaner.get_raw_corpus_from_path(self.corpus_path)
        documents = self.cleaner.split_raw_corpus_into_documents(raw_corpus)
        actual_number_documents = len(documents)
        expected_number_documents = 2
        self.assertEqual(expected_number_documents, actual_number_documents)

    def test_clean_documents(self):
        self.fail()

    def test_clean_a_document(self):
        self.fail()

    def test_get_raw_textual_data_in_document(self):
        self.fail()

    def test_remove_internet_related_elements_from_tokens(self):
        self.fail()

    def test_replace_emojis_by_name_in_tokens(self):
        self.fail()

    def test_get_important_lemmas_in_textual_data(self):
        self.fail()

    def test_get_tree_tags_of_textual_data(self):
        self.fail()

    def test_remove_non_important_part_of_speech_in_tags(self):
        self.fail()

    def test_get_lemmas_in_tags(self):
        self.fail()
