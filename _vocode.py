from dragonfly import *

from lib import *
from rules import *

__VERSION__ = "0.1"
grammars = []

print("")
print(">>> Vocode v%s now starting" % __VERSION__)

state = VimState()


#state.normal_grammar = ???
#state.insert_grammar = ???

def register_grammar(name, rules):
	gram = Grammar(name)
	print("Registering grammar %s" % name)
	for r in rules:
		print("Adding rule %s" % str(r))
		gram.add_rule(r)

	gram.load()

	global grammars
	grammars.append(gram)

class MetaRules(MappingRule):
	name = "meta"
	mapping = {
		'(lock Dragon | deactivate)':  Playback([(["go", "to", "sleep"], 0.0)])
			}
	extras = []
	defaults = {}

# Create our main grammar with rules
register_grammar("vocode_vim", [VimNormalRules(), VimInsertRules()])
register_grammar("vocode_meta", [MetaRules()])

def unload():
	global grammars

	print("Unloading Vocode...")

	for g in grammars:
		if g: g.unload()
		g = None

	grammars = []

	

