from gensim import corpora


class NumericalCorpus:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def build_from_text_corpus(text_corpus):
        mapping_word2id = NumericalCorpus.create_mapping_words_to_id_from_text_corpus(text_corpus)
        document_term_matrix = [mapping_word2id.doc2bow(document) for document in text_corpus]
        return mapping_word2id, document_term_matrix

    @staticmethod
    def create_mapping_words_to_id_from_text_corpus(text_corpus):
        mapping_word2id = corpora.Dictionary(text_corpus)
        return mapping_word2id
