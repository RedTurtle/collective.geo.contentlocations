from zope.i18nmessageid import MessageFactory
import config

ContentLocationsMessageFactory = MessageFactory(config.PROJECTNAME)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
