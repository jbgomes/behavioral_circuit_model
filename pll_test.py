# Author: Julia Gomes
# Date: July 17, 2025
# Description: Test and PLL model loop closed

import matplotlib.pyplot as plt
from vco_model import vco
from pfd_model import PD_and_S2D, function_generate
from cp_model import cp
from filter_model import LPF

vctrl_min = 0.3 
vctrl_max = 0.7 
vctrl = 0.7
f_min = 1e6 
f_max = 1.5e6 

f_ref = 1.125e6
phase_ref = 0

C_lpf = 1e-12

N = 10

vctrl_hist = [vctrl]
t_global = []
ref_hist = []
vco_hist = []
up_hist = []
dn_hist = []
Icp_hist = []
#f_vco_hist = []
#phase_vco_hist = []

for i in range(N):
    f_vco, phase_vco, t, vco_signal = vco(vctrl, vctrl_min, vctrl_max, f_min, f_max)
    ref_signal = function_generate (f_ref, phase_ref, t)
    up, upb, dn, dnb = PD_and_S2D(ref_signal, vco_signal, t)
    Icp = cp(up, dn, t)
    #vctrl = LPF(Icp, t, C_lpf, vctrl_min, vctrl_max, vctrl)
    vctrl = LPF(vctrl, f_max, f_min, vctrl_min, vctrl_max, f_ref)
    
    vctrl_hist.append(vctrl)
    t_global.extend(t + i * t[-1])
    ref_hist.extend(ref_signal)
    vco_hist.extend(vco_signal)
    up_hist.extend(up)
    dn_hist.extend(dn)
    Icp_hist.extend(Icp)
    #f_vco_hist.append(f_vco)
    #phase_vco_hist.append(phase_vco)

plt.figure(1)
plt.subplot(4, 1, 1)
plt.plot(t_global, ref_hist, label='Reference', color='b')
plt.plot(t_global, vco_hist, label='VCO', color='g')
plt.grid()
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t_global, up_hist, label='UP', color='r')
plt.grid()
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t_global, dn_hist, label='DN', color='y')
plt.grid()
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t_global, Icp_hist, label='Icp', color='pink')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(2)
plt.plot(vctrl_hist)
plt.title('Vctrl over iterations')
plt.xlabel('Iteration')
plt.ylabel('Vctrl [V]')
plt.grid()
plt.show()

