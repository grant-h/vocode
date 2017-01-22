from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape | normal mode':  Key("escape"),

		# Formatting
		"parns":  Text("()") + Key("left"),
		"brax":   Text("[]") + Key("left"),
		"curly":  Text("{}") + Key("left"),

                # Editing
		"delete" : Key("delete"),
		"backspace|back" : Key("backspace"),

                # Quirks
                'cut' : Text("cut"),
                'paste'  : Text("paste"),
                'undo' : Text("undo"),
                'redo' : Text("redo"),
                'save' : Text("save"),
                'quit' : Text("quit")
		}
	extras = []
	defaults = {}

	def _process_recognition(self, value, extras):
		print("INST: %s" % str(value._action))
		if value._action._spec == "escape":
			self.parent.handle_event("normal")

		value.execute(extras)
