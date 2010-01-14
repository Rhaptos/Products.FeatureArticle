from Products.Archetypes.Widget import TypesWidget

class LinkWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "linkwidget",
        })

    def process_form(self, instance, field, form, empty_marker=None, emptyReturnsMarker=False):
        value = form.get(field.getName(), empty_marker)
        if value is empty_marker:
            return empty_marker
        if emptyReturnsMarker and value == '':
            return empty_marker
        
        kwargs = {}
        return value, kwargs

try:
  from Products.Archetypes.Registry import registerWidget

  registerWidget(LinkWidget,
                 title='Link',
                 description='Used with a LinkField, can display any of a number of widgets.',
                 used_for=('Products.FeatureArticle.Field.LinkField',)
                 )
except ImportError:
  pass # this is expected for Archetypes pre-1.2
