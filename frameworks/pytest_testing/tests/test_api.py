import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

    # Act
    r = requests.get(url)
    body = r.json()

    # Assert
    assert r.status_code == 200
    assert 'Python' in body['AbstractText']
