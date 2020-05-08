"""
"""
from .parameters import Parameter, ParameterError


class MarketShare(Parameter):
    _key = "market_share"
    _default_value = 0.38
    _dist = "constant"
    _validators = []
    _description = "Hospital market share (%)"


class InitialHospitalized(Parameter):
    _key = "initial_hospitalized"
    _default_value = 1.0
    _dist = "constant"
    _validators = []
    _description = "Number of hospitalized COVID-19 patients on day 1"


class HospitalizedALOS(Parameter):
    _key = "hospitalized_alos"
    _default_value = (12.0, 113.65004210109757, 0.06066759946037977)
    _dist = "gamma"
    _validators = []
    _description = "Hospitalized average length of stay"


class CriticalCareALOS(Parameter):
    _key = "critical_alos"
    _default_value = (9.0, 31.76283993749876, 0.2803727316431524)
    _dist = "gamma"
    _validators = []
    _description = "ICU length of stay"


class VentilatoryALOS(Parameter):
    _key = "ventilatory_alos"
    _default_value = (1.111111111, 32.6782986344606, 0.34151831940405153)
    _dist = "gamma"
    _validators = []
    _description = "Time on ventilator"


class RegionalPopulation(Parameter):
    _key = "regional_population"
    _default_value = 440000.0
    _dist = "constant"
    _validators = []
    _description = "Regional population (Susceptible)"


class HospitalCapacity(Parameter):
    _key = "hospital_capacity"
    _default_value = None
    _dist = "constant"
    _validators = []
    _description = "Number of hospital beds"


class VentilatorCapacity(Parameter):
    _key = "ventilator_capacity"
    _default_value = None
    _dist = "constant"
    _validators = []
    _description = "Number of ventilators"
