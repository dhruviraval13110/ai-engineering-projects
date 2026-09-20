"""Small deterministic starter pipeline for End-to-End AI Platform."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Result:
    value: Any
    status: str = "ok"

def run_pipeline(value: Any) -> Result:
    if value is None:
        raise ValueError("value must not be None")
    return Result(value=value)
