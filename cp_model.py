# Author: Julia Gomes
# Date: July 17, 2025
# Description: Charge pump circuit model that converts the logic 
# state produced by the PFD into a current pulse source for VCO control

import numpy as np

def cp(up, dn, t):
    Icp = np.zeros(len(t))

    for i in range(len(t)):
        if up[i] == 1 and dn[i] == 0:
            Icp[i] = 20e-6
        elif up[i] == 0 and dn[i] == 1:
            Icp[i] = -20e-6
        else:
            Icp[i] = 0
    return Icp

