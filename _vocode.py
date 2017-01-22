from dragonfly import *

import logging

from lib import *
from rules import *
from knowledge import *

__VERSION__ = "0.1"
grammars = []

print("")
print(">>> Vocode v%s now starting" % __VERSION__)

logging.getLogger("vimstate").setLevel(logging.INFO)

state = VimState()

normal_rules = VimNormalRules()
normal_rules.parent = state

insert_rules = VimInsertRules()
insert_rules.parent = state

common_rules = VimCommonRules()
python_rules = PythonRules()

# Associate grammars with Vim states
state.grammars['NORMAL'] += [normal_rules, common_rules]
state.grammars['INSERT'] += [insert_rules, python_rules, common_rules]

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
		'(lock Dragon | deactivate | sleep | shut up)':  Playback([(["go", "to", "sleep"], 0.0)])
			}
	extras = []
	defaults = {}

# Create our main grammar with rules
register_grammar("vocode_vim", [normal_rules, insert_rules, common_rules])
register_grammar("vocode_meta", [MetaRules()])
register_grammar("vocode_lang", [python_rules])

# MUST be called last
normal_rules.disable()
insert_rules.disable()
common_rules.disable()
python_rules.disable()
state.init()

def unload():
	global grammars

	print("Unloading Vocode...")

	for g in grammars:
		if g: g.unload()
		g = None

	grammars = []
