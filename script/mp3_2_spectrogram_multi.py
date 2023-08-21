from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
import numpy as np

mic_number = 4 

for m in range(mic_number):
    rate, data = wavfile.read('/home/namiko/catkin_ws/src/audio_common/recorded_data/output' + str(m+1) +'.mp3')  # read mp3 or wav file
    print(m, "rate:", rate, ",  data:", data)

    # raw_data
    time = np.arange(0, data.shape[0]/rate, 1/rate)
    plt.plot(time, data)
    plt.savefig("raw_data" + str(m+1) +".png")
    plt.clf()

    # FFT (fast fourier transform)
    fft_data = np.abs(np.fft.fft(data))    
    #横軸：周波数の取得　　#np.fft.fftfreq(データ点数, サンプリング周期)
    freqList = np.fft.fftfreq(data.shape[0], d=1.0/rate)
    #データプロット
    plt.xlim(0, 8000) #0～8000Hzまで表示
    plt.plot(freqList, fft_data)
    plt.savefig("FFT" + str(m+1) +".png")
    plt.clf()

    # spectrogram
    plt.specgram(data, Fs=rate, NFFT=128, noverlap=0)  # plot
    plt.savefig('spectrogram' + str(m+1) +'.png')
    plt.clf()

