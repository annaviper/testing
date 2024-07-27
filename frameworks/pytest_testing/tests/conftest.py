import pytest
from ..accum import Accumulator


@pytest.fixture
def accum(scope='function'):
    return Accumulator()
