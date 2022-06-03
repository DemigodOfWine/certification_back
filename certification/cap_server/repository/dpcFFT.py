import numpy as np
from django.conf import settings
from matplotlib import pyplot as plt
from scipy.fft import fft
from scipy.signal import find_peaks
import os
import matplotlib
matplotlib.use('Agg')


def dpc_fft(forms, osc_dir, fft_dir):
    for data in forms:
        signal = np.asarray(data.ascan)
        osc = np.reshape(signal, signal.size)        
        osc = osc[0:int(data.settings.end_signal*100)]
        print(osc)
        timeRange = np.arange(0, len(osc) / data.settings.sampling_frequency, 1 / data.settings.sampling_frequency)
        max_ampl = np.max(osc)
        min_ampl = np.min(osc)
        plt.cla()
        plt.draw()
        plt.ion()
        plt.rc('font', size=12)
        if data.model.form_certificate == 1:
            plt.plot(timeRange, osc)
            plt.plot([data.echo_pulse_delay, data.echo_pulse_delay], [max_ampl / -2, max_ampl / 2], '--r')
            plt.plot([data.echo_pulse_duration, data.echo_pulse_duration], [max_ampl / -2, max_ampl / 2], '--r')
            plt.grid(True)
            plt.title(None)
            path = os.path.join(str(settings.BASE_DIR) + osc_dir + str(data.id) + ".png")
            plt.savefig(path, bbox_inches='tight')
            freqMinLimit = 0
            freqMaxLimit = data.settings.zonder_frequency * (2.5 / 1000)
            osc = osc - osc.mean()
            ffSize = 8 * 16 * 4096
            yf = np.abs(fft(osc, ffSize))
            yf = np.abs(yf)
            yf = yf / yf.max()
            fftSizeKHz = data.settings.sampling_frequency / ffSize * 1000
            iCutSpectrBeg = np.int16(freqMinLimit / fftSizeKHz)
            iCutSpectrEnd = np.int16(freqMaxLimit / fftSizeKHz)
            yf = yf[iCutSpectrBeg:iCutSpectrEnd]
            t = list(range(1, yf.size + 1))
            time_spectr = np.asarray(t) * fftSizeKHz
            plt.cla()
            plt.rc('font', size=12)
            plt.rc('axes', labelsize=20)
            plt.plot(time_spectr, yf)
            plt.plot([data.afc_frequency_maximum, data.afc_frequency_maximum], [0, 1], '--r')
            plt.plot([data.lower_afc_frequency, data.lower_afc_frequency], [0, 0.5], '--r')
            plt.plot([data.upper_afc_frequency, data.upper_afc_frequency], [0, 0.5], '--r')
            plt.plot([data.lower_afc_frequency, data.upper_afc_frequency], [0.5, 0.5], '--r')

            plt.title(None)
            plt.grid(True)
            path = os.path.join(str(settings.BASE_DIR) + fft_dir + str(data.id) + ".png")
            plt.savefig(path, bbox_inches='tight')

        elif data.model.form_certificate == 2:
            plt.plot(timeRange, osc)
            delay = 0
            for s in range(0, len(timeRange)):
                if timeRange[s] > data.echo_pulse_delay:
                    delay = s		    
                    break

            autoHeight = max(signal[0:delay])*4
            autoRange = 1 / data.settings.zonder_frequency * 1000000 * data.settings.sampling_frequency *2  
            peaksUp, _ = find_peaks(osc, height=autoHeight, distance=autoRange, prominence=0.6)
            peaksDown, _ = find_peaks(-osc, height=autoHeight, distance=autoRange, prominence=0.6)
            period = 0
            if data.base.phase == False:
                firstPeak = peaksDown[0]
                secondPeak = peaksUp[0]
                for s in range(secondPeak, len(osc)):
                    if osc[s] < 0:
                        period = s
                        break
            elif data.base.phase == True:
                firstPeak = peaksUp[0]
                secondPeak = peaksDown[0]
                for s in range(secondPeak, len(osc)):
                    if osc[s] > 0:
                        period = s
                        break
            # отмечаем пиковые значения
            plt.plot(timeRange[peaksDown], osc[peaksDown], "x")
            plt.plot(timeRange[peaksUp], osc[peaksUp], "x")
            # задержка сигнала
            plt.plot([data.echo_pulse_delay, data.echo_pulse_delay], [min_ampl, max_ampl], '--r')
            # первый полупериод
            # plt.plot([timeRange[firstPeak], timeRange[firstPeak]], [min_ampl, max_ampl], '--r')
            # второй полупериод
            # plt.plot([timeRange[secondPeak], timeRange[secondPeak]], [min_ampl, max_ampl], '--r')
            # период
            plt.plot([timeRange[period], timeRange[period]], [min_ampl, max_ampl], '--g')
            # уровень сигнала по первому полупериоду
            # plt.plot([timeRange[0], timeRange[-1]], [osc[firstPeak], osc[firstPeak]], '--r')
            plt.grid(True)
            plt.title(None)
            path = os.path.join(str(settings.BASE_DIR) + osc_dir + str(data.id) + ".png")
            plt.savefig(path, bbox_inches='tight')
            freqMinLimit = 0
            freqMaxLimit = data.settings.zonder_frequency * (2.5 / 1000)
            signal_fft = osc[delay:period]
            signal_fft = signal_fft - signal_fft.mean()
            ffSize = 8 * 16 * 4096
            yf = np.abs(fft(signal_fft, ffSize))
            yf = np.abs(yf)
            yf = yf / yf.max()
            fftSizeKHz = data.settings.sampling_frequency / ffSize * 1000
            iCutSpectrBeg = np.int16(freqMinLimit / fftSizeKHz)
            iCutSpectrEnd = np.int16(freqMaxLimit / fftSizeKHz)
            yf = yf[iCutSpectrBeg:iCutSpectrEnd]
            t = list(range(1, yf.size + 1))
            time_spectr = np.asarray(t) * fftSizeKHz

            plt.cla()
            plt.rc('font', size=12)
            plt.rc('axes', labelsize=20)
            plt.plot(time_spectr, yf)
            plt.plot([data.afc_frequency_maximum_first_wave, data.afc_frequency_maximum_first_wave], [0, 1], '--r')
            plt.title(None)
            plt.grid(True)
            path = os.path.join(str(settings.BASE_DIR) + fft_dir + str(data.id) + ".png")
            plt.savefig(path, bbox_inches='tight')
        else:
            return

