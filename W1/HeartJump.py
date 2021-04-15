import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# animation function.  This is called sequentially
def animate(time_run,xdata,ydata):
    run_seq = ydata[time_run:time_run+math.ceil(2.0*15)]
    run_time = xdata[time_run:time_run+math.ceil(2.0*15)]
    plt.xlim(xmin= run_time[0],xmax= 2*run_time[-1]-run_time[0])
    print('call')
    ln.set_data(run_time,run_seq)
    return ln,
def animate2(i):
    data = np.random.random((255, 255))
    im.set_array(data)
    return [im]

def plot_heartjump(heart_rate=80.,fps=15.,time_show = 3.):
    # parameter set
    time_fps = 1/fps
    elec_p = 10.0
    elec_n = -7.0
    time_num = int(fps*time_show)

    #define heart seq & time seq
    elec_seq = np.zeros(time_num)
    time_seq = np.linspace(0,time_show,time_num)

    # calculate positive and negative index 
    index_p = (60.0/heart_rate*fps)
    rate_p2n = 0.1

    index_jump = 0
    index_i = 0
    while index_i < time_num:
        elec_seq[index_i]
        index_i = math.ceil(index_jump*index_p)
        if index_i < time_num:
            elec_seq[index_i] = elec_p
        index_i = math.ceil((index_jump+rate_p2n)*index_p)
        if index_i < time_num:
            elec_seq[index_i] = elec_n
        index_jump = index_jump+1

    # calcultate the cycle seq
    vel_jump = 4*math.pi*heart_rate/(60*fps)
    elec_cy = np.sin(vel_jump*np.arange(time_num))

    #little  noise
    elec_noise = np.random.normal(0.0,0.15,(time_num))

    #elec = sum of all 
    elec_sum = elec_seq + elec_cy + elec_noise
    plt.ion()
    '''
    time_run = 0
    while time_run+math.ceil(2.0*fps)< time_num: 
        run_seq = elec_sum[time_run:time_run+math.ceil(2.0*fps)]
        run_time = time_seq[time_run:time_run+math.ceil(2.0*fps)]
        time_run = time_run +1

        plt.cla()
        plt.xlim(xmin= run_time[0],xmax= 2*run_time[-1]-run_time[0])
        plt.yticks([]) 
        plt.plot(run_time,run_seq)
        plt.scatter(run_time,run_seq)
        plt.pause(0.1)
        plt.show()

    plt.close()
    plt.ioff()
    '''
    return [time_seq,elec_sum]


[xdata,ydata]= plot_heartjump(time_show=10)

fig = plt.figure()
data = np.random.random((255, 255))
ln, = plt.plot([], [], 'ro',animated=True)
anim = animation.FuncAnimation(fig, animate, frames=[120,xdata,ydata] ,blit=False, interval=10,repeat=False)
plt.show()


