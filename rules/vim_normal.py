from dragonfly import *

class VimNormalRules(MappingRule):
	name = "vim_normal"
	mapping = {
		'insert':  Key("i")
			}
	extras = []
	defaults = {}
