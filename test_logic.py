import pytest
from data_provider import get_session_data

def test_data_provider_import():
    """
    Prueft, ob die Daten-Logik korrekt importiert werden kann.
    """
    assert get_session_data is not None

# Da echte API-Aufrufe in CI/CD schwierig sind (Rate Limits, Zeit),
# wuerde man hier normalerweise Mocking verwenden.
