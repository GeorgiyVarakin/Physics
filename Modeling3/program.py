import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

R = 1
V = 1

def circle(a, b, r):
    T = 100
    x, y = [0]*T, [0]*T
    for i,theta in enumerate(np.linspace(0,2*np.pi,T)):
        x[i] = a + r*np.cos(theta)
        y[i] = b + r*np.sin(theta)
    return x, y


def gen():
    for theta in np.linspace(0,4*np.pi,100):
        yield R*(theta-np.sin(theta)), R*(1-np.cos(theta)), R*theta

fig = plt.figure(figsize=(6,3))
ax = fig.add_subplot(111)
ax.set_ylim(0, 3)
ax.set_xlim(0, 15)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')
ax.grid()
time_text = ax.text(0.05, 0.8, '', transform=ax.transAxes)

cycloid, = ax.plot([], [], 'r-', lw=2)
line, = ax.plot([], [], 'y-', lw=2)
circle_line, = ax.plot([], [], 'g', lw=2)
point, = ax.plot([], [], 'bo', ms=4)

xx, yy = [], []
def func(data):
    x, y, Rt = data
    time_text.set_text(r'$\theta$ = %.2f $\pi$' % (Rt/np.pi))
    xx.append(x)
    yy.append(y)
    cx, cy = circle(Rt, R, R)

    cycloid.set_data(xx, yy)
    line.set_data((x,Rt), (y,R))
    circle_line.set_data(cx, cy)
    point.set_data(x, y)

ani = animation.FuncAnimation(fig, func, gen, blit=False, interval=50)

fn = 'cycloid_FuncAnimation'
ani.save('%s.mp4'%(fn), writer='ffmpeg', fps=1000/50)

xx, yy = [], []
ani.save('%s.gif'%(fn), writer='imagemagick', fps=1000/50)

import subprocess
cmd = 'magick convert %s.gif -fuzz 10%% -layers Optimize %s_r.gif'%(fn,fn)
subprocess.check_output(cmd)

plt.rcParams['animation.html'] = 'html5'
xx, yy = [], []
ani
