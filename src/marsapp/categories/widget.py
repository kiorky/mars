#-*- coding: utf-8 -*-
#from Acquisition import aq_base, aq_inner, aq_parent
from zope.component import getMultiAdapter
#from Products.Five.browser import BrowserView
#from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Registry import registerWidget

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget as BReferenceBrowserWidget

class ReferenceBrowserWidget(BReferenceBrowserWidget):
    _properties = BReferenceBrowserWidget._properties.copy()
    _properties.update({
        'macro': 'marsrefbrowser',
        'image_portal_types':['Image',],
        'image_method':'image_thumb', 
        'popup_name' : 'mars_refpopup',
    })

class MarscatWidget(BReferenceBrowserWidget):
    _properties = BReferenceBrowserWidget._properties.copy()
    _properties.update({
        'macro': 'marscats4browser',
        'image_portal_types':['Image',],
        'image_method':'image_thumb',  
        'popup_name' : 'mars_catpopup',
        'restrict_browsing_to_startup_directory': True,
        })

registerWidget(MarscatWidget,
    title='Mars Categories Browser',
    description=('Reference widget that allows you to browse or'
                 'search the portal for categories to refer to.'),
    used_for=('Products.marscats.Field.MarscatField',)
    )



registerWidget(ReferenceBrowserWidget,
           title='Reference Browser',
               description=('Reference widget that allows you to browse or '
                            'search the portal for objects to refer to.'),
               used_for=('Products.Archetypes.Field.ReferenceField',)
               ) 


