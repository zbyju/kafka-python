from abc import ABC, abstractmethod
from header import HeaderV0
from body import Body


class AbstractMessage(ABC):
	@abstractmethod
	def encode(self) -> bytes:
		pass


class Message(AbstractMessage):
	header: HeaderV0
	body: Body

	def __init__(self, header, body) -> None:
		self.header = header
		self.body = body

	def encode(self, id: int):
		id_bytes = id.to_bytes(4, byteorder="big")
		len_bytes = len(id_bytes).to_bytes(4, byteorder="big")
		return len_bytes + id_bytes
