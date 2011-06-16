import AccessControl

from Products.Archetypes.public import BaseSchema, Schema
from Products.Archetypes.public import registerType
from Products.Archetypes.public import BaseContent
from Products.Archetypes.public import StringField, TextField, ImageField, BooleanField
from Products.Archetypes.public import StringWidget, TextAreaWidget, ImageWidget, SelectionWidget, BooleanWidget
from Products.Archetypes.public import DisplayList

from Products.CMFCore import permissions as CMFCorePermissions
from countries import LOCATIONS

REFERRERS = DisplayList((
    ('search', 'Search Engine'),
    ('person', 'Individual "word-of-mouth"'),
    ('article', 'Published Article'),
    ('conference', 'Conference Presentation'),
    ('other', 'Other'),
    ))

schema = BaseSchema + Schema((
    StringField('title',
                required = 1,
                accessor='Title',
                widget=StringWidget(label="Name",
                                    description='The name of the person being featured',)
                ),
    StringField('email',
                widget=StringWidget(label="Email",
                                    description="User's email address",)
                ),
    StringField('location',
                vocabulary=LOCATIONS,
                widget=SelectionWidget(label="Location",
                                       description="Where is the user from?",)
                ),
    StringField('occupation',
                widget=StringWidget(label="Occupation",
                                    description="What is your occupation?",)
                ),
    StringField('referrer',
                vocabulary=REFERRERS,
                widget=SelectionWidget(label="Referrer",
                                       description="How did you hear about Connexions?",)
                ),
    TextField('description',
              required = 1,
              default_content_type = 'text/html',
              default_output_type = 'text/html',
              widget=TextAreaWidget(label="Comment",
                                    description='Your feedback about Connexions (html is allowed)',)
              ),
    ImageField('portrait',
                widget=ImageWidget(label="Portrait",
                                   description='Feel free to include a small portrait of yourself',)
               ),
    
    BooleanField('quote_permission',
                 default=1,
                 widget=BooleanWidget(label="Will you allow Connexions to display a quote from your feedback on the Web site?",
                                      description="Allow Connexions to display a quote from their feedback on the Web site?",)
                 ),
    BooleanField('name_permission',
                 default=1,
                 widget=BooleanWidget(label="Will you allow Connexions to display your name alongside your feedback?",
                                      description="Allow Connexions to use your name along with your feedback?",)
                 ),
    BooleanField('image_permission',
                 default=1,
                 widget=BooleanWidget(label="Will you allow Connexions to display your portrait alongside your feedback?",
                                             description="Allow Connexions to display your picture along with your feedback?",)
                 ),
    ))

class UserFeedback(BaseContent):
    """
    Feedback from Connexions user
    """

    schema = schema
    security = AccessControl.ClassSecurityInfo()
    actions = (
               {'id': 'view',
                'title': 'View',
                'action': 'feedback_view',
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


registerType(UserFeedback,'FeatureArticle')
