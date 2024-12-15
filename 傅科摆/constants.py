"""
Constants used in the Foucault pendulum simulation
"""
import numpy as np

# Default rotation period of the celestial body (Earth = 24 hours)
DEFAULT_ROTATION_PERIOD = 24 * 3600  # seconds

# Gravitational acceleration (m/s^2)
G = 9.81

# Default simulation parameters
DEFAULT_LATITUDE = 45  # degrees
DEFAULT_PERIOD = 2  # seconds
DEFAULT_AMPLITUDE = 1  # meters
DEFAULT_DURATION = 60  # seconds
DEFAULT_FPS = 30  # frames per second