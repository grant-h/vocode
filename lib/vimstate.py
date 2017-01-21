from enum import Enum

class VimMode(Enum):
	NORMAL = 0
	INSERT = 1
	VISUAL = 2

class VimState(object):
	def __init__(self):
		self.mode = VimMode.NORMAL
		self.grammars = {
			'NORMAL' : [],
			'INSERT' : [],
			'VISUAL' : []
		}

	def init(self):
		self._trans_init_normal()

		print("VimState - initialized")

	def _enable_group(self, name):
		g = self.grammars[name]

		print("Enabling %d rules for %s" % (len(g), name))
		for r in g:
			print("...%s" % (str(r)))
			r.enable()

	def _disable_group(self, name):
		g = self.grammars[name]

		print("Disabling %d rules for %s" % (len(g), name))
		for r in g:
			print("...%s" % (str(r)))
			r.disable()

	def _trans_init_normal(self):
		print("VimState - Init --> Normal")

		self._enable_group('NORMAL')

	def _trans_insert_normal(self):
		print("VimState - Insert --> Normal")
		self._disable_group('INSERT')
		self._enable_group('NORMAL')

	def _trans_normal_insert(self):
		print("VimState - Normal --> Insert")
		self._disable_group('NORMAL')
		self._enable_group('INSERT')

	def handle_event(self, event):
		# TODO: visual mode
		if event == "normal":
			self.mode = VimMode.NORMAL
			self._trans_insert_normal()
		elif event == "insert":
			self.mode = VimMode.INSERT
			self._trans_normal_insert()
		else:
			print("Unhandled event %s" % event)
