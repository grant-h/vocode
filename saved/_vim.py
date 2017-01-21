from dragonfly import *

# modes
# 0 - normal
# 1 - insert
# 2 - visual
mode = 0

grammar = Grammar("vim_example")

ex_rule = MappingRule(
		name="insert",
		mapping={
			 "insert mode": Key("I"),
			 "select all text": Key("g, g, V, G"),
			 "undo": Key("u"),
			 "redo": Key("c-r"),
			 "escape" : Key("escape"),
			 "end command" : Key("escape")
			}
	)

grammar.add_rule(ex_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

