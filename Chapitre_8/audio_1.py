#!/usr/bin/env python3
import alsaaudio
import wave

carte = 'sysdefault:CARD=U0x46d0x825'
entree = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, carte)
entree.setchannels(1)
entree.setrate(44100)
entree.setformat(alsaaudio.PCM_FORMAT_S16_LE)
entree.setperiodsize(1024)

with wave.open('test.wav', 'w') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    print('Enregistrement en cours ...')

    while True:
        try:
            _, data = entree.read()
            w.writeframes(data)
        except KeyboardInterrupt:
            break

    print("Fin de l'enregistrement!")
