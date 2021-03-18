from jiketime.object_and_class.search_engine_base import SearchEngineBase, main


class SimpleEngin(SearchEngineBase):
    def __init__(self):
        super(SimpleEngin, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


if __name__ == '__main__':
    search_engine = SimpleEngin()
    main(search_engine)

