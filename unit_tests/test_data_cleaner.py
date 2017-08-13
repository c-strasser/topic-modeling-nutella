from unittest import TestCase
from utils.data_cleaner import DataCleaner
import os
import re


class TestDataCleaner(TestCase):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.cleaner = DataCleaner('french')
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.corpus_path = os.path.join(current_directory, 'example_data/raw_data.csv')

    def test_get_clean_documents_from_corpus_path(self):
        clean_documents = self.cleaner.get_clean_documents_from_corpus_path(self.corpus_path)
        print(clean_documents)

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
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        clean_documents = self.cleaner.clean_documents(documents)
        print(clean_documents)

    def test_clean_a_document(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        clean_document = self.cleaner.clean_a_document(documents[1])
        print(clean_document)

    def test_get_raw_textual_data_in_document(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        processed_tokens = self.cleaner.get_raw_textual_data_in_document(documents[1])
        print(processed_tokens)

    def test_get_raw_textual_data_in_token(self):
        token_1 = 'bonjour😋😋'
        token_2 = '#fitgirl'
        processed_token_1 = self.cleaner.get_raw_textual_data_in_token(token_1)
        processed_token_2 = self.cleaner.get_raw_textual_data_in_token(token_2)
        print(processed_token_1)
        print(processed_token_2)

    def test_remove_all_internet_related_element_from_token(self):
        token = '#fitgirl'
        actual_processed_token = self.cleaner.remove_all_internet_related_element_from_token(token)
        expected_processed_token = ' fitgirl'
        self.assertSequenceEqual(expected_processed_token, actual_processed_token)

    def test_remove_marker_from_token(self):
        expression = re.compile('@.*')
        token = 'ptn|@Lolas_DM'
        actual_processed_token = self.cleaner.remove_marker_from_token(expression, token)
        expected_processed_token = 'ptn| '
        self.assertSequenceEqual(expected_processed_token, actual_processed_token)

    def test_replace_emojis_by_name_in_token(self):
        token = 'bonjour😋😋'
        processed_token = self.cleaner.replace_emojis_by_name_in_token(token)
        print(processed_token)

    def test_get_important_lemmas_in_textual_data(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        processed_tokens = self.cleaner.get_raw_textual_data_in_document(documents[1])
        important_lemmas = self.cleaner.get_important_lemmas_in_textual_data(processed_tokens)
        print(important_lemmas)

    def test_get_tree_tags_of_textual_data(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        processed_tokens = self.cleaner.get_raw_textual_data_in_document(documents[1])
        tree_tags = self.cleaner.get_tree_tags_of_textual_data(processed_tokens)
        print(tree_tags)

    def test_remove_non_important_part_of_speech_in_tags(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        processed_tokens = self.cleaner.get_raw_textual_data_in_document(documents[1])
        tree_tags = self.cleaner.get_tree_tags_of_textual_data(processed_tokens)
        processed_tags = self.cleaner.remove_non_important_part_of_speech_in_tags(tree_tags)
        print(processed_tags)

    def test_get_lemmas_in_tags(self):
        documents = self.cleaner.get_raw_documents_from_corpus_path(self.corpus_path)
        processed_tokens = self.cleaner.get_raw_textual_data_in_document(documents[1])
        tree_tags = self.cleaner.get_tree_tags_of_textual_data(processed_tokens)
        lemmas = self.cleaner.get_lemmas_in_tags(tree_tags)
        print(lemmas)
