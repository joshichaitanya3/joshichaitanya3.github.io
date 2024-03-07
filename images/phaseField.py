import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use("blog.mplstyle")
def phase_field(x,y, epsilon=0.1):
    r = np.sqrt(x**2 + y**2)
    return np.tanh((1-r)/np.sqrt(2*epsilon))

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)
X,Y = np.meshgrid(x,y)
Z = phase_field(X,Y, epsilon=0.01)

px = 1/plt.rcParams['figure.dpi']  # pixel in inches
# plt.figure(figsize=(500*px,500*px))
plt.figure(figsize=(2,2))
im = plt.contourf(X,Y,Z, cmap='PiYG')
clb = plt.colorbar(im,fraction=0.046, pad=0.04)
clb.ax.locator_params(nbins=5)
clb.ax.set_title(r"$\phi$")
plt.gca().set_aspect('equal')
plt.tight_layout()
plt.savefig("phaseField.png", dpi=300, transparent=True)
plt.show()

