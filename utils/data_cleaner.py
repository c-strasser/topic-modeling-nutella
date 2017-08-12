class DataCleaner:
    def __init__(self, language) -> None:
        super().__init__()
        self.language = language

    def get_clean_corpus_from_path(self, corpus_path):
        pass

    def get_raw_corpus_from_path(self, corpus_path):
        pass

    def split_raw_corpus_into_documents(self, raw_corpus):
        pass

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


