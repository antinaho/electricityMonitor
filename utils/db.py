from dataclasses import dataclass
from contextlib import contextmanager

import psycopg2 as p


@dataclass
class ConnectionParams:
	db : str
	user : str
	password : str
	host : str
	port : int


class DatabaseConnection:

	def __init__(self, conn: ConnectionParams):
		self.__database = conn.db
		self.__user = conn.user
		self.__password = conn.password
		self.__host = conn.host
		self.__port = conn.port;


	@contextmanager
	def connection(self):
		self.conn = p.connect(
			database=self.__database,
			user=self.__user,
			password=self.__password,
			host=self.__host,
			port=self.__port)
		self.conn.autocommit = True
		self.curr = self.conn.cursor()
		try:
			yield self.curr
		finally:
			self.curr.close()
			self.conn.close()