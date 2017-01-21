from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape':  Key("escape")
			}
	extras = []
	defaults = {}
