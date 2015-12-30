from src.utils.translator.BoruvkaTranslator import activate as translation
from src.utils.translator.BoruvkaTranslator import gettext as _
from tempita import HTMLTemplate


class BoruvkaBaseView(object):
    def __init__(self, template, language=None):
        if language:
            translation(language)

        self._page = HTMLTemplate.from_filename(template)

    # Probably not the best solution...
    def render(self):
        return self._page.substitute(self.__dict__)

    # TODO: do not translate keys starting with "_"
    def __setattr__(self, key, value):
        if isinstance(value, basestring):
            value = _(value)
        return object.__setattr__(self, key, value)
