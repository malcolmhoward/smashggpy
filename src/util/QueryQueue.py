from src.util.Query import Query
from src.util.QueryQueueElement import QueryQueueElement
from src.common.Exceptions import NotInitializedException

class QueryQueue(object):

	__instance = None
	__initialized = False

	def __init__(self, queue: list=[]):
		self.queue = queue

	@staticmethod
	def get_instance():
		if not QueryQueue.__initialized:
			QueryQueue.__instance = QueryQueue()
			QueryQueue.__initialized = True
		return QueryQueue.__instance

	@staticmethod
	def verify_initialized():
		if not QueryQueue.__initialized:
			raise NotInitializedException()

	def add(self, query: Query):
		QueryQueue.verify_initialized()
		element = QueryQueueElement(query)
		self.queue.append(element)

	def pop(self):
		QueryQueue.verify_initialized()
		return self.queue.pop(0)