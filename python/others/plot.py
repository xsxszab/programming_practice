import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6),dpi=80)
plt.subplot(111)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X, C, color="black", linewidth=1.0, linestyle="-")
plt.plot(X, S, color="red", linewidth=1.0, linestyle="-")
plt.xlim(-np.pi,np.pi)
plt.ylim(-1.0,1.0)