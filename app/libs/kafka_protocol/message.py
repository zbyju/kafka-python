from abc import ABC, abstractmethod
from enum import Enum, unique

from .header import HeaderV2
from .body import Body


@unique
class ErrorCode(Enum):
	NONE = 0
	UNSUPPORTED_VERSION = 35


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

	def validate(self) -> ErrorCode:
		# Check supported versions
		supported_versions = [0, 1, 2, 3, 4]
		if self.header.api_version not in supported_versions:
			return ErrorCode.UNSUPPORTED_VERSION

		# All checks passed
		return ErrorCode.NONE

	@staticmethod
	def __int_bytes(value: int, length: int):
		return int(value).to_bytes(length, "big")

	def encode(self):
		response_header = self.__int_bytes(self.header.id, 4)

		error_code = self.validate()
		min_version, max_version = 0, 4
		throttle_time_ms = 0
		tag_buffer = b"\x00"
		response_body = (
			self.__int_bytes(error_code.value, 2)
			+ self.__int_bytes(2, 1)
			+ self.__int_bytes(self.header.api_key, 2)
			+ self.__int_bytes(min_version, 2)
			+ self.__int_bytes(max_version, 2)
			+ tag_buffer
			+ self.__int_bytes(throttle_time_ms, 4)
			+ tag_buffer
		)

		response_length = len(response_header) + len(response_body)
		return self.__int_bytes(response_length, 4) + response_header + response_body
