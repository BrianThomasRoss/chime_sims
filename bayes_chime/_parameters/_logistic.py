"""
Logistic Parameters
===================
"""
from .parameters import Parameter


class LogisticK(Parameter):
    _key = "logistic_k"
    _default_value = (1.0, 4.018953794, 0.22738215)
    _distribution = "gamma"
    _validators = []
    _description = "Logistic growth rate"


class LogisticX0(Parameter):
    _key = "logistic_x0"
    _default_value = (14.0, 6.407435434, 2.859728136)
    _distribution = "gamma"
    _validators = []
    _description = "Logistic days from beginning of time series to middle of logistic"


class LogisticL(Parameter):
    _key = "logistic_l"
    _default_value = (0.25, 5, 10)
    _distribution = "beta"
    _validators = []
    _description = "Logistic depth of social distancing"
