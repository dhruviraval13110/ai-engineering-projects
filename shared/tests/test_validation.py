import pytest
from shared.validation import require_fields

def test_require_fields_accepts_complete_record():
    require_fields({"name": "Dhruvi", "age": 20}, ("name", "age"))

def test_require_fields_reports_missing():
    with pytest.raises(ValueError, match="age"):
        require_fields({"name": "Dhruvi"}, ("name", "age"))
