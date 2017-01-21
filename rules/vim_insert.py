from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape':  Key("escape")
		}
	extras = []
	defaults = {}

	def enter_normal(action):
		action.execute()
		#global listeners
		#for l in listeners:
		#	l.handle_event("normal")
