def tic_tac():
	print("Tic")
	yield
	print("tac")
	yield
	return "err"



STATUS_NEW = 'NEW'
STATUS_RUNNING = 'RUNNING'
STATUS_FINISHED = 'FINISHED'
STATUS_ERROR = 'ERROR'
STATUS_CANCELLED = 'CANCELLED'
class Task:
	def __init__(self,coro):
		self.coro = coro
		self.name = coro.__name__
		self.status = STATUS_NEW
		self.return_value = None
		self.error_value = None
	def run(self):
		try:
			self.status = STATUS_RUNNING
			next(self.coro)
		except StopIteration as err:
			self.status = STATUS_FINISHED
			self.return_value = err.value
		except Exception as err:
			self.status = STATUS_ERROR
			self.error_value = err
	def is_done(self):
		return self.status in {STATUS_FINISHED,STATUS_ERROR}
	def cancel(self):
		if self.is_done():
			return
		self.status = STATUS_CANCELLED
	def is_cancelled(self):
		return self.status == STATUS_CANCELLED
	def __repr__(self):
		result = ''
		if self.is_done():
			result = "({!r})".format(self.return_value or self.error_value)
		return "<Task '{}' [{}]{}>".format(self.name, self.status, result)

"""
task = Task(tic_tac())
print(task)
while not task.is_done():
	task.run()
	print(task)
print(task.return_value)
"""
from collections import deque
"""
running_tasks = deque()
running_tasks.append(Task(tic_tac()))
running_tasks.append(Task(tic_tac()))

while running_tasks:
	task = running_tasks.popleft()
	task.run()
	if task.is_done():
		print(task)
	else:
		running_tasks.append(task)
"""

class Loop:
	def __init__(self):
		self._running = deque()
	def _loop(self):
		task = self._running.popleft()

		if task.is_cancelled():
			print(task)
			return


		task.run()
		if task.is_done():
			print(task)
			return
		self.schedule(task)
	def run_until_complete(self,task):
		task = self.schedule(task)
		while not task.is_done():
			self._loop()
	def run_until_empty(self):
		while self._running:
			self._loop()
	def schedule(self, task):
		if not isinstance(task,Task):
			task = Task(task)
		self._running.append(task)
		return task


def spam():
	print("Spam")
	yield
	print("Eggs")
	yield
	print("Bacon")
	yield
	return "Spam"

def cancel(task):
	task.cancel()
	yield

def example():
	print("Tache 'example'")
	print("Lancement de la tache 'subtask'")
	sub = ensure_future(subtask())
	print("Retour dans 'example'")
	for _ in range(3):
		print("(example")
		yield
	yield from cancel(sub)
def subtask():
	print("Tache 'Subtask'")
	for _ in range(5):
		print("(Subtask)")
		yield
DEFAULT_LOOP = Loop()


def ensure_future(coro, loop=None ):
	if loop is None:
		loop = DEFAULT_LOOP
	return loop.schedule(coro)





