"""
Parameters
==========

Model parameters defined here. Parameters should be considered 
'upstream' of any models and initialized as the package loads. They 
should be considered immutable, and any model should use parameters only 
to initialize a simulation.

Parameters should have at minimum the following attributes: 
- 'name' or key
- default value
- description 

Additionally one should consider associating a parameter with one or 
more validators.

Contents


_epidemiological:   characteristics of the virus itself
_regional:          characteristics of the region being simulated
_validators:        parameter validation functions
parameters:         base classes, helper functions and global store
"""