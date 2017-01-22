from dragonfly import *

class VimCommonRules(MappingRule):
	name = "vim_common"
	mapping = {
		"enter|return" : Key("enter"),
                "(blabber|babel) <text>" : Text("%(text)s"),

		"pageup" : Key("pgup"),
		"pagedown": Key("pgdown"),

                # Common Movement
		"up" : Key ("up"),
		"down" : Key ("down"),
		"left" : Key("left"),
		"right" : Key("right"),
                "up <total_line>" : Key("up:%(total_line)d"),
                "down <total_line>" : Key("down:%(total_line)d"),
                "left <total_line>" : Key("left:%(total_line)d"),
                "right <total_line>" : Key("right:%(total_line)d")
		}
	extras = [
            Dictation("text"),
            Dictation("var"),
            IntegerRef("total_line", 1, 100),
            IntegerRef("start", 1, 100),
            IntegerRef("end", 1, 100),
            IntegerRef("line_num", 1, 9999)
            ]
        defaults = {
            "text" : "",
            "total_line" : 1,
            "start": 0,
            "end": 5,
            "line_num" : 1
            }

	def _process_recognition(self, value, extras):
		print("COM: %s" % str(value._action))

		value.execute(extras)
