from browser import document
from browser.template import Template

Template(document["greet"]).render(name="Bernard Iorver")