"""
Combined physics calculations for the Foucault pendulum
"""
import numpy as np
from pendulum_motion import calculate_harmonic_motion
from coriolis_effect import calculate_precession_rate

def calculate_position(t, amplitude, period, precession_rate):
    """Calculate the position of the pendulum at time t.
    
    Args:
        t (float): Time in seconds
        amplitude (float): Amplitude of oscillation
        period (float): Period of oscillation
        precession_rate (float): Precession rate in rad/s
        
    Returns:
        tuple: (x, y) coordinates
    """
    # Calculate basic harmonic motion
    displacement, _ = calculate_harmonic_motion(t, amplitude, period)
    
    # Apply precession to the oscillation plane
    precession_angle = precession_rate * t
    
    # Transform the displacement into the rotating reference frame
    x = displacement * np.cos(precession_angle)
    y = displacement * np.sin(precession_angle)
    
    return x, y