from unittest import TestCase
from gensim.models.ldamodel import LdaModel
from utils.topic_modeler import TopicModeler

class TestTopicModeler(TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.mapping_word2id = {'nutella': 0, 'bon': 1, 'dessert': 2, 'gras': 3,
                                'fitgirl': 4, 'poisson': 5, 'recette': 6}
        self.document_terms_matrix = [[(0, 1), (1, 1), (2, 2)], [(2, 1), (3, 1), (4, 1)], [(5, 1), (6, 1)]]
        self.number_topics = 2
        self.topic_modeler = TopicModeler((self.mapping_word2id, self.document_terms_matrix), self.number_topics)

    def test_train(self):
        model = self.topic_modeler.train(50)
        self.assertIsInstance(model, LdaModel)

    def test_get_most_important_topics_and_keywords(self):
        self.fail()

    def test_reformat_results(self):
        self.fail()

    def test_reformat_results_for_topic(self):
        self.fail()

    def test_evaluate_on_validation_corpus(self):
        self.fail()


