from __future__ import annotations

from typing import Mapping, Any


def require_fields(record: Mapping[str, Any], fields: tuple[str, ...]) -> None:
    missing = [field for field in fields if field not in record]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
