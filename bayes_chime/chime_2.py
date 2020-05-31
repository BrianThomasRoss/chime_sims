"""

"""
from typing import NewType

import __main__
from ._config import Settings
from ._parameters import Parameters
from .models import Compartmental


parameters = Parameters(logging=False)
settings = Settings()


class BayesCHIME:

    _cache = {}
    _model = Model
    _data: Parameters = None

    def __new__(cls):
        """Allocator"""
        if cls.__name__ in dir(__main__):
            delattr(__main__, f"{cls.__name__}")

    def __init__(self,
                 model: str = "seir",
                 distributions: str = "normal"
                 ) -> None:

        self.model = get_simulation(model)

    def fit(self):
        """
        Fits the model to the data
        """

    def predict(self):
        """Runs the simulation"""

        return