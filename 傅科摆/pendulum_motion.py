"""
Core pendulum motion calculations
"""
import numpy as np

def calculate_harmonic_motion(t, amplitude, period):
    """Calculate simple harmonic motion components.
    
    Args:
        t (float): Time in seconds
        amplitude (float): Maximum displacement
        period (float): Period of oscillation
        
    Returns:
        tuple: (displacement, velocity)
    """
    omega = 2 * np.pi / period
    displacement = amplitude * np.cos(omega * t)
    velocity = -amplitude * omega * np.sin(omega * t)
    return displacement, velocity