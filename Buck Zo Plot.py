# -*- coding: utf-8 -*-
"""
How to generate Bode Plots
Example with buck converter
"""
from math import pi, log10
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Create Laplace variable
s = tf('s')
# Buck converter parameters
Vi=10; Vo=5; RL=1; D=0.5
L=50e-6; rl=0.05; C=10e-6; rc=0.15
# Ramp peak-to-peak voltage
Vpp=10

# Buck output impedance
ZL= rl + s*L; Zc=rc + 1/(s*C)
Zo= 1/( 1/ZL + 1/Zc + 1/RL)

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz

mag, phase, omega = bode_plot(Zo, dB=True, Hz=True, omega_limits=(10,100e3), \
                              omega_num=100 )
i=75
print(omega[i]/2/pi, mag[i], phase[i]*180/pi)
   
























