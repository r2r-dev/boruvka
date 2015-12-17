from src.utils.translator.BoruvkaTranslator import activate as translation
from src.utils.translator.BoruvkaTranslator import gettext as _
from tempita import HTMLTemplate


class BoruvkaBaseView(object):
    def __init__(self, template, language=None):
        if language:
            translation(language)

        self._template = HTMLTemplate.from_filename(template)

    # Probably not the best solution...
    def render(self):
        return self._template.substitute(self.__dict__)

    def __setattr__(self, key, value):
        if isinstance(value, basestring):
            value = _(value)
        return object.__setattr__(self, key, value)
