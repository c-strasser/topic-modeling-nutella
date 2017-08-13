import re
import treetaggerwrapper

class DataCleaner:
    def __init__(self, language) -> None:
        super().__init__()
        self.language = language
        self.document_marker = re.compile('^.?\d+\|')

    def get_clean_documents_from_corpus_path(self, corpus_path):
        raw_documents = self.get_raw_documents_from_corpus_path(corpus_path)
        clean_documents = self.clean_documents(raw_documents)
        return clean_documents

    def get_raw_documents_from_corpus_path(self, corpus_path):
        corpus = self.get_raw_corpus_from_path(corpus_path)
        raw_documents = self.split_raw_corpus_into_documents(corpus)
        return raw_documents

    @staticmethod
    def get_raw_corpus_from_path(corpus_path):
        with open(corpus_path, encoding='utf-8') as file:
            corpus = file.readlines()
        return corpus

    @staticmethod
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
        clean_documents = [self.clean_a_document(document) for document in documents]
        return clean_documents

    def clean_a_document(self, document):
        raw_textual_data = self.get_raw_textual_data_in_document(document)
        important_lemmas = self.get_important_lemmas_in_textual_data(raw_textual_data)
        return important_lemmas


    def get_raw_textual_data_in_document(self, document):
        tokens = document.split()
        tokens = self.remove_internet_related_elements_from_tokens(tokens)
        tokens = self.replace_emojis_by_name_in_tokens(tokens)
        return tokens

    def remove_internet_related_elements_from_tokens(self, tokens):
        pass

    def replace_emojis_by_name_in_tokens(self, tokens):
        pass

    def get_important_lemmas_in_textual_data(self, textual_data):
        tree_tags = self.get_tree_tags_of_textual_data(textual_data)
        important_tree_tags = self.remove_non_important_part_of_speech_in_tags(tree_tags)
        important_lemmas = self.get_lemmas_in_tags(important_tree_tags)
        return important_lemmas

    def get_tree_tags_of_textual_data(self, textual_data):
        pass


    def remove_non_important_part_of_speech_in_tags(self, tags):
        pass

    def get_lemmas_in_tags(self, tags):
        pass