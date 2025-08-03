__all__ = ["CAS"]
from .casregnum import CAS

try:
    from importlib.metadata import version
    __version__ = version("casregnum")
except ImportError:
    __version__ = "unknown"
