# Author: Julia Gomes
# Date: July 8, 2025
# Description: VCO circuit model that generates signal with voltage-controlled frequency

import numpy as np
from scipy import signal

def vco(vctrl, vctrl_min, vctrl_max, f_min, f_max):  
    if vctrl < vctrl_min:
        vctrl = vctrl_min
    elif vctrl > vctrl_max:
        vctrl = vctrl_max

    phase_vco = 0
    f_vco = (vctrl - vctrl_min) * (f_max - f_min) / (vctrl_max - vctrl_min) + f_min

    fs = 100*f_vco
    Ts = 1/fs
    #tf = 100*Ts
    tf = 10e-6
    t = np.arange(0, tf, Ts)

    vco_signal = signal.square(2 * np.pi * f_vco * t + phase_vco)

    return f_vco, phase_vco, t, vco_signal