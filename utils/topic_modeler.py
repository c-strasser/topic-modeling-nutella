from gensim.models.ldamodel import LdaModel
import pyLDAvis.gensim


class TopicModeler:

    def __init__(self, training_numerical_corpus, number_topics) -> None:
        super().__init__()
        self.numerical_corpus = training_numerical_corpus
        self.number_topics = number_topics
        self.model = None

    def train(self, number_passes):
        mapping_word2id, document_terms_matrix = self.numerical_corpus
        model = LdaModel(document_terms_matrix, num_topics=self.number_topics,
                         id2word=mapping_word2id, passes=number_passes)
        self.model = model

    def get_most_important_topics_and_keywords(self, number_keywords):
        unformatted_results = self.model.print_topics(num_topics=self.number_topics, num_words=number_keywords)
        return unformatted_results

    def display_results(self):
        mapping_word2id, document_terms_matrix = self.numerical_corpus
        data_to_display = pyLDAvis.gensim.prepare(self.model, document_terms_matrix, mapping_word2id)
        pyLDAvis.display(data_to_display)

    def evaluate_on_validation_corpus(self, validation_corpus):
        perplexity = self.model.log_perplexity(validation_corpus)
        return perplexity
