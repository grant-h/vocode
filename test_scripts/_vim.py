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
			 "insert mode": Key("i"),

			 "select all [text]": Key("g, g, V, G"),
			 "undo": Key("u"),
			 "redo": Key("c-r"),
			 "escape" : Key("escape"),
			 "end command" : Key("escape"),

			 "bottom" : Key("G"),
			 "top" : Key("g,g"),
			 "enter": Key("\n"),
			 "next": Key("down,fn,left "),
			 "end" : Key("fn,right"),

			 "parns":        Text("()") + Key("left"),
			 "brax":           Text("[]") + Key("left"),
			 "curly":          Text("{}") + Key("left"),
			 "angle":          Text("<>") + Key("left")
			 
			}
	)

grammar.add_rule(ex_rule)

grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

