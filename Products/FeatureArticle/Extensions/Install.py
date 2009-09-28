from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.FeatureArticle.config import *
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import CMFCorePermissions
from Products.CMFCore.Expression import Expression
from StringIO import StringIO

import zLOG
def log(msg, severity=zLOG.INFO):
    zLOG.LOG("FeatureArticle: Install", severity, msg)

def setProp(tool, prop, value):
    #log("Setting property [%s , %s]" % (prop, value))
    try:
        tool._delProperty(prop)
    except: pass
    tool._setProperty(prop, value)

def install(self):
    try:
        out = StringIO()
        print >> out, "Starting FeatureArticle install"
        log("Starting FeatureArticle install")

        log("...installing types")
        installTypes(self, out,
                     listTypes(PROJECTNAME),
                     PROJECTNAME)

        # New 'FeedbackFolder' on 'PloneFolder'
        self.portal_types.manage_addTypeInformation(id='FeedbackFolder',
                                                    add_meta_type="Factory-based Type Information",
                                                    typeinfo_name="CMFPlone: Plone Folder")
        ff = getattr(self.portal_types, 'FeedbackFolder')
        for a in ff._actions:
            if a.id == 'view':
                a.action = Expression('feedbackfolder_view')

        ff._p_changed = 1
        ff.filter_content_types = 1
        ff.allowed_content_types = ('UserFeedback')

        log("...installing subsksins")
        install_subskin(self, out, GLOBALS)

    except Exception, e:
        log(e)
        print >> out, "Error: %s" % e
    else:
        log("Successful!")
        print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()
