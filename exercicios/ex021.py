from pygame import mixer
mixer.init()

musica = mixer.music.load('jojo.mp3')
mixer.music.play()
stop = input('\nPressione qualquer tecla para parar... ')

