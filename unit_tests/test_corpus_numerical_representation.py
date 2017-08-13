from unittest import TestCase
from gensim import corpora
from utils.corpus_numerical_representation import CorpusNumericalRepresentation as NumericalCorpus


class TestCorpusNumericalRepresentation(TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.text_corpus = [['nutella', 'bon', 'dessert', 'dessert'],
                            ['dessert', 'gras', 'fitgirl'],
                            ['poisson', 'recette']]

    def test_create_document_term_matrix_from_text_corpus(self):
        _, document_term_matrix = NumericalCorpus.build_from_text_corpus(self.text_corpus)
        print(document_term_matrix)
        self.assertIsInstance(document_term_matrix, list)

    def test_create_dictionary_from_text_corpus(self):
        dictionary = NumericalCorpus.create_mapping_words_to_id_from_text_corpus(self.text_corpus)
        self.assertIsInstance(dictionary, corpora.Dictionary)
