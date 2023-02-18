"""This creates a second source of truth beyond pyproject.toml which is not great.
However, this is the simplest workaround for ensuring a __version__ string is available
to FastAPI app startup in both dev and prod.
"""

__version__: str = "0.1.0"
