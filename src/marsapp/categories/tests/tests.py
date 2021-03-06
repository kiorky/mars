#-*- coding: utf-8 -*-
import zope.component.testing
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite, DocFileSuite

def tearDown(test):
    zope.component.testing.tearDown(test)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTests((
        DocFileSuite('storage.txt',
                     tearDown=tearDown,
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
        ),
    ))
    return suite
