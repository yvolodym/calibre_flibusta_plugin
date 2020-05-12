# -*- coding: utf-8 -*-

# https://github.com/kovidgoyal/calibre/blob/master/src/calibre/gui2/store/stores/litres_plugin.py
# https://github.com/kovidgoyal/calibre/blob/d6498bf8370e716ec47e22c6fe581a6b17983a5a/src/calibre/gui2/store/search_result.py
#

from __future__ import (unicode_literals, division, absolute_import, print_function)

store_version = 1  # Needed for dynamic plugin loading

__license__ = 'GPL 3'
__copyright__ = '2020, Eugen Vladimirski <kety@gmx.de>'
__docformat__ = 'restructuredtext en'

from calibre.gui2.store.basic_config import BasicStoreConfig
from calibre.gui2.store.opensearch_store import OpenSearchOPDSStore
from calibre.gui2.store.search_result import SearchResult

class FlibustaStore(BasicStoreConfig, OpenSearchOPDSStore):

    open_search_url = 'http://flibusta.net/opds-opensearch.xml'
    web_url = 'http://flibusta.net/'

    def search(self, query, max_results=10, timeout=60):
		#url = 'http://flibusta.is/opds/opensearch?searchTerm=%s&searchType=books' % quote_plus(query)
		#counter = max_results
		
        for s in OpenSearchOPDSStore.search(self, query, max_results, timeout):
            s.detail_item = 'http://flibusta.net/b/' + s.detail_item.split(':')[-1]
            s.price = '$0.00'
            s.drm = SearchResult.DRM_UNLOCKED
            yield s

    def get_details(self, search_result, timeout):
        search_result.drm = SearchResult.DRM_UNLOCKED
        search_result.formats = "FB2, EPUB, MOBI"
        search_result.downloads["FB2"] = search_result.detail_item + "/fb2"
        search_result.downloads["EPUB"] = search_result.detail_item + "/epub"
        search_result.downloads["MOBI"] = search_result.detail_item + "/mobi"
        return True
	
#    def create_search_result(self, data):
#		sRes = SearchResult()
#		sRes.drm = SearchResult.DRM_UNLOCKED
#		sRes.cover_data = 'http://opds-spec.org/thumbnail' . data.xpath('.//link[@rel="http://opds-spec.org/thumbnail"]/@href')
