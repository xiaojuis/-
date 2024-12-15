"""
Visualization module for the Foucault pendulum simulation
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from physics import calculate_position
from coriolis_effect import calculate_precession_rate

class PendulumAnimator:
    def __init__(self, latitude, period, amplitude, duration, fps, rotation_period, time_multiplier=1.0):
        """Initialize the pendulum animator.
        
        Args:
            latitude (float): Latitude in degrees
            period (float): Period of oscillation in seconds
            amplitude (float): Amplitude of oscillation in meters
            duration (float): Duration of simulation in seconds
            fps (float): Frames per second for animation
            rotation_period (float): Rotation period of the celestial body in seconds
            time_multiplier (float): Time speed multiplier (default: 1.0)
        """
        self.latitude = latitude
        self.period = period
        self.amplitude = amplitude
        self.duration = duration
        self.fps = fps
        self.rotation_period = rotation_period
        self.time_multiplier = time_multiplier
        
        self.precession_rate = calculate_precession_rate(latitude, rotation_period)
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.time_template = 'Time = %.1fs'
        self.time_text = self.ax.text(0.05, 0.95, '', transform=self.ax.transAxes)
        
        # Initialize plot
        self.setup_plot()
        
    def setup_plot(self):
        """Set up the plot appearance"""
        self.ax.set_xlim(-self.amplitude * 1.2, self.amplitude * 1.2)
        self.ax.set_ylim(-self.amplitude * 1.2, self.amplitude * 1.2)
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        
        # Add plot title with parameters
        precession_deg_per_hour = np.degrees(self.precession_rate) * 3600
        title = (f'Foucault Pendulum at {self.latitude}°N\n'
                f'Rotation Period: {self.rotation_period:.1f} seconds\n'
                f'Precession Rate: {precession_deg_per_hour:.2f}°/hour\n'
                f'Time Speed: {self.time_multiplier:.1f}x')
        self.ax.set_title(title)
        
        self.ax.set_xlabel('X (meters)')
        self.ax.set_ylabel('Y (meters)')
        
        # Plot the trace with low alpha
        t = np.linspace(0, self.duration, 1000)
        x_trace = []
        y_trace = []
        for time in t:
            x, y = calculate_position(time, self.amplitude, self.period, self.precession_rate)
            x_trace.append(x)
            y_trace.append(y)
        self.ax.plot(x_trace, y_trace, 'gray', alpha=0.2, label='Trace')
        
        # Create pendulum point
        self.point, = self.ax.plot([], [], 'ro', markersize=10, label='Pendulum')
        # Create line from origin to pendulum
        self.line, = self.ax.plot([], [], 'b-', linewidth=1)
        
        # Add initial oscillation direction
        self.ax.arrow(0, 0, self.amplitude, 0, color='green', alpha=0.5,
                     head_width=0.05, head_length=0.1, label='Initial Direction')
        
        self.ax.legend()
        
    def animate(self, frame):
        """Animation function for each frame"""
        t = frame / self.fps * self.time_multiplier
        x, y = calculate_position(t, self.amplitude, self.period, self.precession_rate)
        
        self.point.set_data([x], [y])
        self.line.set_data([0, x], [0, y])
        self.time_text.set_text(self.time_template % t)
        
        return self.point, self.line, self.time_text
    
    def create_animation(self):
        """Create and return the animation"""
        frames = int(self.duration * self.fps)
        interval = 1000/self.fps  # Keep constant frame interval regardless of time_multiplier
        anim = FuncAnimation(self.fig, self.animate, frames=frames,
                           interval=interval, blit=True)
        return anim