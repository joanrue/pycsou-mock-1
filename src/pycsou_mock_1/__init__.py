
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from .math import eigh

__all__ = (
    "eigh",
    )