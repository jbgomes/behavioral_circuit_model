# Author: Julia Gomes
# Date: June 27, 2025
# Description: Code that generates reference signal and error pulse 
# equivalent to the phase difference between reference and VCO

import numpy as np
from scipy import signal

def function_generate(f_ref, phase_ref, t):               
    ref_signal = signal.square(2 * np.pi * f_ref * t + phase_ref)
    return ref_signal

def detect_rising_edges(signal_array):
    return np.where((signal_array[1:] > 0) & (signal_array[:-1] <= 0))[0] + 1

def PD_and_S2D(ref_signal, vco_signal, t):
    ref_edges = detect_rising_edges(ref_signal)
    vco_edges = detect_rising_edges(vco_signal)

    up = np.zeros(len(t))
    upb = np.ones(len(t))
    dn = np.zeros(len(t))
    dnb = np.ones(len(t))

    num_events = min(len(ref_edges), len(vco_edges))

    for i in range(num_events):
        t_ref = ref_edges[i]
        t_vco = vco_edges[i]

        if t_ref < t_vco:
            up[t_ref:t_vco] = 1
            upb[t_ref:t_vco] = 0
        elif t_vco < t_ref:
            dn[t_vco:t_ref] = 1
            dnb[t_vco:t_ref] = 0

    return up, upb, dn, dnb