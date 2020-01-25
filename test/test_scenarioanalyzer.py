from .context import anacondo
from .test_blocks import generate_sample_block

@pytest.fixture
def sample_block():
	return generate_sample_block()

