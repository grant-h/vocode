from dragonfly import *

class VimNormalRules(MappingRule):
	def __init__(self):
		self.parent = None
		super(VimNormalRules, self).__init__()

	name = "vim_normal"
	mapping = {
		'insert':  Key("i")
		}
	extras = []
	defaults = {}

	def _process_recognition(self, value, extras):
		#print "REC", str(self), "VALUE", str(value), "EXTRAS", str(extras)
		#print "action", value._action, "data", value._data
		if value._action._spec == "i":
			self.parent.handle_event("insert")

		value.execute(extras)
		#self.process_recognition(value)

