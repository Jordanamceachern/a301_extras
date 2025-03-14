# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
Te = 255 # K
r = 6378 # km
omega = 5.67e-8
d = np.arange(2000,10000000,1000) # km

# Q 4.32 using parallel beams
Ts1 = Te*(1/4*(r/(r+d))**2)**(1/4)

# Q 4.31 for d>>r
#
Fs = omega * Te**4  * (r/(d+r))**2
Ts2 = (Fs/omega)**(1/4)

# %%
plt.plot(d,Ts1, label='inverse square law')
plt.plot(d,Ts2, label='solid angle method')
plt.xlabel('distance/km')
plt.ylabel('temperature/K')
plt.legend()
# %%
