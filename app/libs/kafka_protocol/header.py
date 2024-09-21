from dataclasses import dataclass
from typing import List


@dataclass
class HeaderV0:
	id: int


@dataclass
class HeaderV1(HeaderV0):
	tagged_fields: List[str]


@dataclass
class HeaderV2(HeaderV1):
	api_key: int
	api_version: int
	client_id: int
