import importlib.metadata

__version__ = importlib.metadata.version("mem0ai")

from mem0.client.main import MemoryClient, AsyncMemoryClient  # noqa
from mem0.memory.main import Memory  # noqa



print(123)

print(123)