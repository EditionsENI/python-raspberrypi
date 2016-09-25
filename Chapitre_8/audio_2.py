#!/usr/bin/env python3
import alsaaudio
import wave

with wave.open('test.wav', 'rb') as w:
    sortie = alsaaudio.PCM()
    sortie.setchannels(w.getnchannels())
    sortie.setrate(w.getframerate())
    sortie.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    sortie.setperiodsize(1024)
    fichier = w._file.file.name
    print('Lecture de {0} ...'.format(fichier))

    while True:
        try:
            data = w.readframes(1024)
            if not data: break
            sortie.write(data)
        except KeyboardInterrupt:
            break

    print('Fin de la lecture!')
