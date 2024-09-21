from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import List


class KafkaServerException(Exception):
	code: int = 0


class UnsupportedVersionException(KafkaServerException):
	code = 35
	version: int

	def __init__(self, version: int) -> None:
		self.version = version


@dataclass
class HeaderV0:
	id: int

	@staticmethod
	def decode(bytes: bytes):
		id = int.from_bytes(bytes[8:12], byteorder="big")

		return HeaderV0(id)


@dataclass
class HeaderV1(HeaderV0):
	tagged_fields: List[str]

	@staticmethod
	def decode(bytes: bytes):
		h0 = HeaderV0.decode(bytes)

		return HeaderV1(h0.id, [])


@dataclass
class HeaderV2(HeaderV1):
	api_key: int
	api_version: int
	client_id: int

	@staticmethod
	def decode(bytes: bytes):
		h1 = HeaderV1.decode(bytes)
		api_key = int.from_bytes(bytes[4:6], byteorder="big")
		api_version = int.from_bytes(bytes[6:8], byteorder="big")
		client_id = 0

		return HeaderV2(h1.id, h1.tagged_fields, api_key, api_version, client_id)
