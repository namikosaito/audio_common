from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
import numpy as np

rate, data = wavfile.read('output.mp3')  # read mp3 or wav file
print("rate:", rate, ",  data:", data[:,0])

# raw_data
time = np.arange(0, data.shape[0]/rate, 1/rate)
plt.plot(time, data[:,0])
plt.savefig("raw_data.png")
plt.clf()

# FFT (fast fourier transform)
fft_data = np.abs(np.fft.fft(data[:,0]))    
#横軸：周波数の取得　　#np.fft.fftfreq(データ点数, サンプリング周期)
freqList = np.fft.fftfreq(data[:,0].shape[0], d=1.0/rate)
#データプロット
plt.xlim(0, 8000) #0～8000Hzまで表示
plt.plot(freqList, fft_data)
plt.savefig("FFT.png")
plt.clf()

# spectrogram
plt.specgram(data[:,0], Fs=rate, NFFT=128, noverlap=0)  # plot
plt.savefig('spectrogram.png')


#####################
plt.clf()
rate, data = wavfile.read('output2.mp3')  # read mp3 or wav file
print("rate:", rate, ",  data:", data[:,0])

# raw_data
time = np.arange(0, data.shape[0]/rate, 1/rate)
plt.plot(time, data[:,0])
plt.savefig("raw_data2.png")
plt.clf()

# FFT (fast fourier transform)
fft_data = np.abs(np.fft.fft(data[:,0]))    
#横軸：周波数の取得　　#np.fft.fftfreq(データ点数, サンプリング周期)
freqList = np.fft.fftfreq(data[:,0].shape[0], d=1.0/rate)
#データプロット
plt.xlim(0, 8000) #0～8000Hzまで表示
plt.plot(freqList, fft_data)
plt.savefig("FFT2.png")
plt.clf()

# spectrogram
plt.specgram(data[:,0], Fs=rate, NFFT=128, noverlap=0)  # plot
plt.savefig('spectrogram2.png')