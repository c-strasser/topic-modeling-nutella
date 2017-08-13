import re
from gensim.models.ldamodel import LdaModel


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
        formatted_results = TopicModeler.reformat_results(unformatted_results)
        return formatted_results

    @staticmethod
    def reformat_results(results):
        reformatted_results = ''
        for index_topic, topic_results in results:
            results_all_keywords = TopicModeler.reformat_topics_results(topic_results)
            result_topic = 'Topic ' + str(index_topic + 1) + ': \n' + results_all_keywords
            reformatted_results = reformatted_results + result_topic
        return reformatted_results

    @staticmethod
    def reformat_topics_results(topic_results):
        split_between_keywords_marker = re.compile('.\+.')
        keywords_groups = re.split(split_between_keywords_marker, topic_results)
        reformatted_results = ''
        for group in keywords_groups:
            results_keyword = TopicModeler.reformat_keyword_results(group)
            reformatted_results = reformatted_results + results_keyword
        reformatted_results = reformatted_results + '\n'
        return reformatted_results

    @staticmethod
    def reformat_keyword_results(keyword):
        split_between_weights_and_key_marker = re.compile('\*')
        weight, keyword = re.split(split_between_weights_and_key_marker, keyword)
        percentage_weight = round(float(weight) * 100, 3)
        string_results = '\t' + keyword + ': ' + str(percentage_weight) + '% \n'
        return string_results

    def evaluate_on_validation_corpus(self, validation_corpus):
        perplexity = self.model.log_perplexity(validation_corpus)
        return perplexity
