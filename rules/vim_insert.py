from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape | normal mode':  Key("escape"),

		# Formatting
		"parns":  Text("()") + Key("left"),
		"brax":   Text("[]") + Key("left"),
		"curly":  Text("{}") + Key("left")
		}
	extras = []
	defaults = {}

	def _process_recognition(self, value, extras):
		print("INST: %s" % str(value._action))
		if value._action._spec == "escape":
			self.parent.handle_event("normal")

		value.execute(extras)
