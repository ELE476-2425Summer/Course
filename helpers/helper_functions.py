import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

def plot_timeseries(title, x, y, line=['continuous']):
    """Function to plot up multiple timeseries on the same axis.
    
    Parameters
    ----------
    title : string
        The title of the plot.
    x : numerical array
        An array containing the x axes of the plots.
    y : numerical array
        An array containing the y axes of the plots.
    line : string array
        An array stating the plot type for each plot.
        (Continuous, discrete, dash)
    """
    plt.figure(figsize=(10,4))
    ax = plt.gca()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title(title)

    for i in range(len(x)):
        if line[i] == 'continuous':
            ax.plot(x[i],y[i])
        elif line[i] == 'discrete':
            ax.stem(x[i], y[i], basefmt='blue', linefmt='red', markerfmt='C3o')
        elif line[i] == 'dash':
            ax.plot(x[i],y[i],'green',linestyle='--',linewidth = 2.5)
    
    plt.show()
    
def find_fft(signal, n_window):
    fft = np.fft.fftshift(np.fft.fft(signal, n_window))

    return 10*np.log10(abs(fft)/len(signal))

def plot_fft(freqs, fft_signal, fs, title, label=None):
    plt.figure(figsize=(10,4))
    ax = plt.gca()
    for i in range(len(freqs)):
        if label != None:
            ax.plot(freqs[i][int(len(freqs[i])/2):], 
                    fft_signal[i][int(len(freqs[i])/2):],
                    label=label[i])
        else:
            ax.plot(freqs[i][int(len(freqs[i])/2):], 
                    fft_signal[i][int(len(freqs[i])/2):])
        
    plt.axvline(x = fs, color = 'g', linestyle='--', label='fs')
    plt.axvline(x = fs/2, color = 'r', linestyle='--', label='fs/2')
    ax.grid(True)
    ax.set_title(title)
    ax.set_xlabel('Frequency, Hz')
    ax.set_ylabel('Amplitude, dB')
    ax.set_xlim(0, 3000)
    ax.legend()
    plt.show()
    
def plot_response(fs, w, h, title, xlim=None):
    """Utility function to plot response functions
    """
    if xlim == None:
        xlim = fs/2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(0.5*fs*w/np.pi, 20*np.log10(abs(h)))
    ax.set_ylim(-60, 20)
    ax.set_xlim(0, xlim)
    ax.grid(True)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Gain (dB)')
    ax.set_title(title)
    
 
