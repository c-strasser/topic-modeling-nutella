from gensim import corpora


class CorpusNumericalRepresentation:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def create_document_term_matrix_from_text_corpus(text_corpus):
        dictionary = CorpusNumericalRepresentation.create_dictionary_from_text_corpus(text_corpus)
        document_term_matrix = [dictionary.doc2bow(document) for document in text_corpus]
        return document_term_matrix

    @staticmethod
    def create_dictionary_from_text_corpus(text_corpus):
        dictionary = corpora.Dictionary(text_corpus)
        print('Indices of words in corpus are: \n')
        print(dictionary.token2id)
        return dictionary
