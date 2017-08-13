from gensim.models.ldamodel import LdaModel

class TopicModeler:


    def __init__(self, training_numerical_corpus, number_topics) -> None:
        super().__init__()
        self.numerical_corpus = training_numerical_corpus
        self.number_topics = number_topics
        self.model = None


    def train(self, number_passes):
        pass

    def get_most_important_topics_and_keywords(self, number_keywords):
        pass

    @staticmethod
    def reformat_results(results):
        pass

    @staticmethod
    def reformat_results_for_topic(results):
        pass

    def evaluate_on_validation_corpus(self, validation_corpus):
        pass