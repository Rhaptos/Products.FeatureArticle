import AccessControl

from Products.Archetypes.public import BaseSchema, Schema
from Products.Archetypes.public import registerType
from Products.Archetypes.public import BaseContent
from Products.Archetypes.public import StringField, TextField, ImageField
from Products.Archetypes.public import StringWidget, TextAreaWidget, ImageWidget

from Products.CMFCore import permissions as CMFCorePermissions

from Products.FeatureArticle.Field import LinkField
from Products.FeatureArticle.Widget import LinkWidget

schema = BaseSchema + Schema((
    StringField('title',
                accessor='Title',
                required = 1,
                widget=StringWidget(label="Title",
                                    description='Article title',)
                ),
    StringField('name',
                required = 1,
                widget=StringWidget(label="Name",
                                    description='The name of the person being featured',)
                ),
    StringField('username',
                widget=StringWidget(label="Username",
                                    description='The userid of the person being featured',)
                ),
    TextField('description',
              accessor='Description',
              required = 1,
              widget=TextAreaWidget(label="Lead In",
                                    description='Lead in text for the article',)
              ),
    TextField('body',
              default_content_type = 'text/html',
              default_output_type = 'text/html',
              allowable_content_types = ('text/structured',
                                         'text/html',
                                         'text/plain',
                                         'text/plain-pre',),
              widget=TextAreaWidget(label="Body",
                                    description='The main body of the article',)
              ),
    ImageField('portrait',
                widget=ImageWidget(label="Portrait",
                                   description='Small portrait of article subject',)
               ),
    LinkField('seealso1',
              widget=LinkWidget(label="See also 1",
                                description='A link to go to',)
              ),
    LinkField('seealso2',
              widget=LinkWidget(label="See also 2",
                                description='Another link to go to',)
              ),
    ))

class FeatureArticle(BaseContent):
    """
    A featured article about a Connexions author
    """

    schema = schema
    security = AccessControl.ClassSecurityInfo()
    actions = (
               {'id': 'view',
                'title': 'View',
                'action': 'feature_view',
                'permissions': (CMFCorePermissions.View,)
                },
               {'id': 'edit',
                'title': 'Edit',
                'action': 'base_edit',
                'permissions': (CMFCorePermissions.ModifyPortalContent,)
                },
               {'id': 'metadata',
                'title': 'Properties',
                'action': 'base_metadata',
                'permissions': (CMFCorePermissions.ModifyPortalContent,)
                },
               {'id': 'references',
                'title': 'References',
                'action': 'reference_edit',
                'permissions': (CMFCorePermissions.ModifyPortalContent,)
                },
               )
    
    security.declareProtected(CMFCorePermissions.View, 'CookedBody')
    def CookedBody(self, stx_level='ignored'):
        """CMF compatibility method
        """
        return self.getText()


registerType(FeatureArticle,'FeatureArticle')
