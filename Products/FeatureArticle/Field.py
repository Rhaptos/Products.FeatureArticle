from Products.Archetypes.public import ObjectField, Field

class LinkField(ObjectField):
    """A field for containing multiple fields."""

    _properties = Field._properties.copy()
    _properties.update({
        'type' : 'link',
        'default': {'title':'','url':''},
        'searchable': 0,
        })

from Products.Archetypes.Registry import registerField

registerField(LinkField,
              title='Link',
              description=('Used for storing links.',))

