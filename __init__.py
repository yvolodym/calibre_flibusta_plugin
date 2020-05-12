# -*- coding: utf-8 -*-

from __future__ import (unicode_literals, division, absolute_import, print_function)

__license__ = 'GPL 3'
__copyright__ = '2020, Eugen Vladimirski <kety@gmx.de>'
__docformat__ = 'restructuredtext en'

from calibre.customize import StoreBase

class FlibustaStore(StoreBase):
    name = 'Флибуста'
    description = _('Книжное братство')
    actual_plugin = 'calibre_plugins.store_flibusta.flibusta:FlibustaStore'
