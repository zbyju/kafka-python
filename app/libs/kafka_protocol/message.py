from abc import ABC, abstractmethod
from .header import HeaderV2
from .body import Body


class AbstractMessage(ABC):
	@abstractmethod
	def encode(self) -> bytes:
		pass


class Message(AbstractMessage):
	header: HeaderV2
	body: Body

	def __init__(self, header: HeaderV2, body: Body) -> None:
		self.header = header
		self.body = body

	def encode(self):
		# TODO: Properly find length of the response
		len_bytes = int(0).to_bytes(4, byteorder="big")
		id_bytes = self.header.id.to_bytes(4, byteorder="big")

		if self.header.api_version not in {0, 1, 2, 3, 4}:
			return len_bytes + id_bytes + int(35).to_bytes(2, byteorder="big")

		return len_bytes + id_bytes
