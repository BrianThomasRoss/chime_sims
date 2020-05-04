"""parameters/_base.
"""
from collections import namedtuple
from typing import Any, Callable, List, Dict, NamedTuple, Set, Tuple
# parameter metadata
param_args = [
    "param_key",
    "default_val",
    "param_dist",
    "validators",
    "param_desc",
]
# Holds a single parameter's metadata
RegisteredParameter = namedtuple("RegisteredParameter", param_args)

# Stores metadata for all configured parameters
_registered_parameters: Dict[str, RegisteredParameter] = {}
# Reserved keys for special use
_reserved_keys: List[str] = ["all"]
# Temporary holder for key value pair of parameter configuration
_param_config: Dict[str, Any] = {}



class ParameterError(AttributeError, KeyError): # custom exception
    """
    Error for handling exceptions encountered while interacting with 
    parameters.
    
    Extends on AttributeError, KeyError
    """


def _get_param(pattern: str)-> None:
    """Attempts to return the registered parameter"""
    p = pattern.lower()
    if p in _registered_parameters:
        return _registered_parameters[p]
    raise ParameterError(f"'{pattern}' is not a parameter")

def _register_param(
    param_key: str,  # -------- # parameter 'name'
    default_val: Any,# -------- # default value for the parameter if none is found
    param_dist: str, # -------- # parameter distribution group
    validators: List[Callable], # validation functions to be used on the parameter
    param_desc: str="" # ------ # description of the parameter
)-> None:
    """Attempts to register a parameter"""
    p = param_key.lower()
    if p in _registered_parameters:
        raise ParameterError(f"'{param_key}' is already registered!")
    # ensure the default value can be validated if validators are included
    if validators:
        for validate in validators:
            validate(default_val)
    if len(param_desc) == 0:
        raise ParameterError('Parameters must include a description')
    # if all checks pass register the parameter with the metadata
    _registered_parameters[p] = RegisteredParameter(param_key=param_key,
                                                    default_val=default_val,
                                                    param_dist=param_dist,
                                                    validators=validators,
                                                    param_desc=param_desc
                                                    )

def _describe_param(pattern: str)-> str:
    param = _get_param(pattern)
    return param.param_desc

def _get_param_defval(pattern: str)-> Any:
    param = _get_param(pattern)
    return param.default_val


class Parameter(object):
    
    def __new__(cls, *args, **kwargs):
        if cls._key in _param_config:
            raise ParameterError(f"'{cls._key}' already registered!")
        return super().__new__(cls)
    
    def __init_subclass__(cls, *args, **kwargs):
        """Register parameter metadata at subclass definition"""
        _register_param(param_key=cls._key,
                       default_val=cls._defval,
                       param_dist=cls._dist,
                       validators=cls._validators,
                       param_desc=cls._description)
        
        return super().__init_subclass__(**kwargs)

    def __setattr__(self, name, value):
        "If parameter already set throw error"
        if self._key in _param_config:
            raise ParameterError('Parameters are immutable!')
        else:
            return super().__setattr__(name, value)

    def __validate__(self, *args, **kwargs):
        if '_value' in zip(args, kwargs):
            for v in self._validators:
                v(kwargs['_value'])
    
    def __describe__(self):
        return self._description

