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

		self._trans_init_normal()

		print("VimState - initialized")

	def _trans_init_normal(self):
		print("VimState - Init --> Normal")

		for r in self.grammars['NORMAL']:
			r.enable()

	def _trans_insert_normal(self):
		print("VimState - Insert --> Normal")

		for r in self.grammars['INSERT']:
			r.disable()
		for r in self.grammars['NORMAL']:
			r.enable()

	def _trans_normal_insert(self):
		print("VimState - Normal --> Insert")

		for r in self.grammars['NORMAL']:
			r.disable()
		for r in self.grammars['INSERT']:
			r.enable()

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
