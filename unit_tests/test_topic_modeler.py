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

    def test_reformat_results(self):
        results = [(0, '0.168*health + 0.083*sugar + 0.072*bad'), (1, '0.061*consume + 0.050*drive + 0.050*sister')]
        reformatted_results = self.topic_modeler.reformat_results(results)
        print(reformatted_results)

    def test_reformat_results_for_topic(self):
        results_topic = '0.168*health + 0.083*sugar + 0.072*bad'
        reformatted_results = self.topic_modeler.reformat_topics_results(results_topic)
        print(reformatted_results)

    def test_reformat_results_for_keyword(self):
        results_keyword = '0.168*health'
        reformatted_results = self.topic_modeler.reformat_keyword_results(results_keyword)
        print(reformatted_results)

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
