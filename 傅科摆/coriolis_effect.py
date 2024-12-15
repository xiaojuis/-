"""
Coriolis effect calculations
"""
import numpy as np

def calculate_angular_velocity(rotation_period):
    """Calculate the angular velocity of the celestial body.
    
    Args:
        rotation_period (float): Rotation period in seconds
        
    Returns:
        float: Angular velocity in radians per second
    """
    return 2 * np.pi / rotation_period

def calculate_precession_rate(latitude_deg, rotation_period):
    """Calculate the precession rate of the pendulum plane.
    
    Args:
        latitude_deg (float): Latitude in degrees
        rotation_period (float): Rotation period of celestial body in seconds
        
    Returns:
        float: Precession rate in radians per second
    """
    latitude_rad = np.radians(latitude_deg)
    omega = calculate_angular_velocity(rotation_period)
    return omega * np.sin(latitude_rad)