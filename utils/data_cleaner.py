import re

class DataCleaner:
    def __init__(self, language) -> None:
        super().__init__()
        self.language = language
        self.document_marker = re.compile('^.?\d+\|')

    def get_clean_corpus_from_path(self, corpus_path):
        pass

    def get_raw_corpus_from_path(self, corpus_path):
        with open(corpus_path, encoding='utf-8') as file:
            corpus = file.readlines()
        return corpus

    def split_raw_corpus_into_documents(self, raw_corpus):
        documents = []
        current_document = raw_corpus[0]
        for line in raw_corpus[1:]:
            if re.match(self.document_marker, line):
                # Removes document marker from first line of document
                line = re.split(self.document_marker, line)[1]
                documents.append(current_document)
                current_document = line
            else:
                current_document = current_document + line
        documents.append(current_document)
        return documents



    def clean_documents(self, documents):
        pass


    def clean_a_document(self, document):
        pass

    def escape_html_characters_in_words(self, words):
        pass

    def decode_words(self, words):
        pass

    def remove_punctuation_in_list_words(self, words):
        pass

    def remove_stop_words_in_list_words(self, words):
        pass

    def replace_emojis_by_description_in_words(self, words):
        pass

    def lemmatize_words(self, list_words):
        pass

    def remove_url_in_words(self, words):
        pass

    def concatenate_remaining_words(self, words):
        pass


