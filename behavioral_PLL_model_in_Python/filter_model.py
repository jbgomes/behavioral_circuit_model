# Author: Julia Gomes
# Date: July 17, 2025
# Description: Filter

import numpy as np

#def LPF(Icp, t, C_lpf, vctrl_min, vctrl_max, vctrl):
#    delta_v = np.trapz(Icp, t) / C_lpf 
    #print(f"ΔV = {delta_v:.3e}, Vctrl before = {vctrl:.3f} V") 
#    vctrl += delta_v
#    vctrl = np.clip(vctrl, vctrl_min, vctrl_max)  
#    return vctrl

def LPF(vctrl, f_max, f_min, vctrl_min, vctrl_max, f_ref):
    vctrl = (f_ref - f_min) * (vctrl_max - vctrl_min) / (f_max - f_min) + vctrl_min 
    return vctrl