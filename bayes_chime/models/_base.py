"""models/_base.py

base
====

Base class for models
"""
from abc import ABCMeta, abstractmethod


class Simulation(metaclass=ABCMeta):
    """Mixin class for simulations"""


    @abstractmethod

    def set_simulation_parameters(cls):



    @abstractmethod
    def fit(self, *args, **kwargs):
        """Fits the model to the data"""

    @abstractmethod
    def step(self):
        """"""
