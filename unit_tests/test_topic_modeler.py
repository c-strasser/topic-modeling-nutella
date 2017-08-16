from unittest import TestCase
from gensim.models.ldamodel import LdaModel
from utils.numerical_corpus import NumericalCorpus
from utils.topic_modeler import TopicModeler


class TestTopicModeler(TestCase):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.numerical_corpus = self.build_example_corpus()
        self.number_topics = 2
        self.topic_modeler = TopicModeler(self.numerical_corpus, self.number_topics)

    def test_train(self):
        self.topic_modeler.train(5)
        self.assertIsInstance(self.topic_modeler.model, LdaModel)

    def test_get_most_important_topics_and_keywords(self):
        self.topic_modeler.train(5)
        results = self.topic_modeler.get_most_important_topics_and_keywords(2)
        print(results)

    def test_display_results(self):
        self.topic_modeler.train(5)
        self.topic_modeler.display_results()

    def test_evaluate_on_validation_corpus(self):
        self.topic_modeler.train(5)
        perplexity = self.topic_modeler.evaluate_on_validation_corpus(self.numerical_corpus[1])
        print(perplexity)

    @staticmethod
    def build_example_corpus():
        text_corpus = [['nutella', 'bon', 'dessert', 'dessert'],
                       ['dessert', 'gras', 'fitgirl'],
                       ['poisson', 'recette']]
        numerical_corpus = NumericalCorpus.build_from_text_corpus(text_corpus)
        return numerical_corpus
