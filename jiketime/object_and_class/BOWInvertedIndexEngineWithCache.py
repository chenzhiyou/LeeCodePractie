from jiketime.object_and_class.BOWInvertedIndexEngine import BOWInvertedIndexEngine
from jiketime.object_and_class.LRUCache import LRUCache
from jiketime.object_and_class.search_engine_base import main


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)
        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)
        return result


search_engine = BOWInvertedIndexEngineWithCache
main(search_engine)
