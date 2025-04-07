from ._imports_ import *  # importa os componentes React
from ._metadata import PACKAGE_NAME, __version__

__all__ = ["DeckGL"]

_js_dist = [
    {
        "relative_package_path": "dash_deck.min.js",
        "namespace": PACKAGE_NAME
    },
    {
        "relative_package_path": "dash_deck.min.js.map",
        "namespace": PACKAGE_NAME,
        "dynamic": True
    }
]

for component in __all__:
    setattr(locals()[component], "_js_dist", _js_dist)

