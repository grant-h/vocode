from dragonfly import dictation
from dragonfly import dictation
from dragonfly import *
from 
from 
# modes
# 0 - normal
# 1 - insert
# 2 - visual
mode = 0

grammar = grammar("vim_example")

ex_rule = mappingrule(
		name="insert",
		mapping={
			 "fork": key("test")
			}
	)

grammar.add_rule(ex_rule)
arammacap.add_rule(ex_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = none




















































print a greeting for a lawn
