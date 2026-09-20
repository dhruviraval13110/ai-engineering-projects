from src.pipeline import run_pipeline

def test_pipeline_returns_result():
    result = run_pipeline("example")
    assert result.status == "ok"
    assert result.value == "example"

def test_pipeline_rejects_none():
    import pytest
    with pytest.raises(ValueError):
        run_pipeline(None)
