import sys

sys.path.insert(
    0,
    "sdk/athena-tool-sdk/src"
)

from athena_sdk.conversation import (
    normalize_conversation,
)

__all__ = [
    "normalize_conversation",
]
