"""
Epidemiological Parameters
==========================

Parameters which are either characteristics of the virus or directly
tied to it.
"""
from .parameters import Parameter


class RecoveryDays(Parameter):
    _key = "recovery_days"
    _default_value = 14.0
    _distribution = "constant"
    _validators = []
    _description = "Days from infection to recovery"


class IncubationDays(Parameter):
    _key = "incubation_days"
    _default_value = 5.0
    _distribution = "constant"
    _validators = []
    _description = "Days from exposure to infectiousness"


class Nu(Parameter):
    _key = "nu"
    _default_value = (2.5, 93.95521690000001, 0.02634306)
    _distribution = "gamma"
    _validators = []
    _description = "Networked contact structure power-law exponent"


class Beta(Parameter):
    _key = "beta"
    _default_value = (0.25, 5.0, 10.0)
    _distribution = "beta"
    _validators = []
    _description = "SEIR beta parameter (force of infection)"


class HospitalizationRate(Parameter):
    _key = "hospitalization_rate"
    _default_value = (0.025, 6.326832789, 0.004168888)
    _distribution = "gamma"
    _validators = []
    _description = "Proportion of infected individuals requiring hospitalization"


class ICURate(Parameter):
    _key = "icu_rate"
    _default_value = (0.45, 52.05931116, 96.86741968)
    _distribution = "beta"
    _validators = []
    _description = "Proportion of admission requiring ICU intervention"


class VentilatoryRate(Parameter):
    _key = "ventilatory_rate"
    _default_value = (0.66, 5.224029085, 3.0788852660000003)
    _distribution = "beta"
    _validators = []
    _description = "Proportion of ICU admissions requiring ventilatory care"
