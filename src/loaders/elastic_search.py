import os
from elasticsearch import Elasticsearch


class ElasticSearchDb:
    _db: Elasticsearch

    def loader(self):
        _es_host = os.environ.get("ES_HOST")
        _es_port = os.environ.get("ES_PORT")
        _es_api_key = os.environ.get("ES_API_KEY")
        _connection_string = 'htt://' + _es_host + ':' + str(_es_port)
        self._db = Elasticsearch(hosts=_connection_string, api_key=_es_api_key)
        if not self._db.ping():
            raise ValueError("Es connection failed")
        pass

    @property
    def context(self) -> Elasticsearch:
        return self._db
        pass


elastic_search_db = ElasticSearchDb()
