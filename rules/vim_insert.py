from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape | normal mode':  Key("escape")
		}
	extras = []
	defaults = {}

	def _process_recognition(self, value, extras):
		print("INST: %s" % value._action._spec)
		if value._action._spec == "escape":
			self.parent.handle_event("normal")

		value.execute(extras)
