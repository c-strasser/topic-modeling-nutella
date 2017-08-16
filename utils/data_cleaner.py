import re
import unicodedata
import treetaggerwrapper


class DataCleaner:

    def __init__(self, language) -> None:
        super().__init__()
        self.language = language
        self.document_marker = re.compile('^.?\d+\|')
        self.list_internet_related_markers
        self.non_important_part_of_speech_tags = ['ADV', 'DET:ART', 'DET:POS', 'INT', 'KON', 'NUM', 'PRO', 'PRO:DEM',
                                                  'PRO:IND', 'PRO:PER', 'PRO:POS', 'PRO:POS', 'PRO:REL', 'PRP',
                                                  'PRP:det', 'PUN', 'PUN:cit', 'SENT', 'SYM']
        self.stop_lemmas = ['être', 'avoir', 'suivre|être']
        self.begin_unicode_index_emojis = ord("\U0001F300")
        self.end_unicode_index_emojis = ord("\U0001FFFF")
        self.tree_tagger_directory = '/home/thales/Documents/camille/publicis/tree_tagger'

    @property
    def list_internet_related_markers(self):
        calling_user_marker = re.compile('@.*')
        hashtag_marker = re.compile('#')
        url_marker = re.compile('http.*')
        html_marker = re.compile('<.*>')
        next_tag_marker = re.compile('\|')
        return [calling_user_marker, hashtag_marker, url_marker, html_marker, next_tag_marker]

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
        processed_tokens = [self.get_raw_textual_data_in_token(token) for token in tokens]
        return processed_tokens

    def get_raw_textual_data_in_token(self, token):
        processed_token = self.remove_all_internet_related_element_from_token(token)
        processed_token = self.replace_emojis_by_name_in_token(processed_token)
        return processed_token

    def remove_all_internet_related_element_from_token(self, token):
        for expression in self.list_internet_related_markers:
            token = self.remove_marker_from_token(expression, token)
        return token

    @staticmethod
    def remove_marker_from_token(internet_marker, token):
        processed_token = re.sub(internet_marker, ' ', token)
        return processed_token

    def replace_emojis_by_name_in_token(self, token):
        for unicode_index_of_character in range(self.begin_unicode_index_emojis, self.end_unicode_index_emojis):
            character_name = ' ' + unicodedata.name(chr(unicode_index_of_character), "NOTHING").lower() + ' '
            token = token.replace(chr(unicode_index_of_character), character_name)
        return token

    def get_important_lemmas_in_textual_data(self, textual_data):
        tree_tags = self.get_tree_tags_of_textual_data(textual_data)
        important_tree_tags = self.remove_non_important_part_of_speech_in_tags(tree_tags)
        important_lemmas = self.get_lemmas_in_tags(important_tree_tags)
        return important_lemmas

    def get_tree_tags_of_textual_data(self, textual_data):
        tree_tagger = treetaggerwrapper.TreeTagger(TAGLANG=self.language[:2], TAGDIR=self.tree_tagger_directory)
        tags = tree_tagger.tag_text(textual_data)
        return treetaggerwrapper.make_tags(tags)

    def remove_non_important_part_of_speech_in_tags(self, tags):
        important_tags = []
        for tag in tags:
            if isinstance(tag, treetaggerwrapper.Tag):
                if tag[1] not in self.non_important_part_of_speech_tags:
                    if tag[2] not in self.stop_lemmas:
                        important_tags.append(tag)
        return important_tags

    @staticmethod
    def get_lemmas_in_tags(tags):
        lemmas = [re.split('\|', tag[2].lower())[0] for tag in tags]
        return lemmas
