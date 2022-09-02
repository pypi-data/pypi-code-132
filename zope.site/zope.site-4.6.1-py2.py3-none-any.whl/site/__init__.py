##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Local Component Architecture
"""

from zope.site.site import LocalSiteManager
from zope.site.site import SiteManagementFolder
from zope.site.site import SiteManagerAdapter
from zope.site.site import SiteManagerContainer
from zope.site.site import changeSiteConfigurationAfterMove
from zope.site.site import clearThreadSiteSubscriber
from zope.site.site import threadSiteSubscriber


__all__ = [
    'SiteManagerContainer',
    'SiteManagementFolder',
    'SiteManagerAdapter',
    'LocalSiteManager',
    'threadSiteSubscriber',
    'clearThreadSiteSubscriber',
    'changeSiteConfigurationAfterMove',
]


# BBB. Remove in Version 5.0
from zope.component import getNextUtility
from zope.component import queryNextUtility
from zope.deprecation import deprecated


getNextUtility = deprecated(
    getNextUtility,
    '``zope.site.getNextUtility`` is deprecated '
    'and will be removed in zope.site 5.0. '
    'Use it from ``zope.component`` instead.')
queryNextUtility = deprecated(
    queryNextUtility,
    '``zope.site.queryNextUtility`` is deprecated '
    'and will be removed in zope.site 5.0. '
    'Use it from ``zope.component`` instead.')
