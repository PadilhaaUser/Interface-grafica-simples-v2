import os
os.environ ["KIVY_AUDIO"] ="sdl2"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.core.audio import Sound, SoundLoader
from kivy.clock import Clock

class Principal(BoxLayout):
    minha_imagem= StringProperty('imagemAbertura.png')  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size= (400,600)
        self.som_aguaTermal  = SoundLoader.load('somAguaTermal.wav')
        self.som_fogueira    = SoundLoader.load('somFogueira.wav')
        self.som_raio        = SoundLoader.load('somRaio.wav')
        self.som_secador     = SoundLoader.load('somSecador.wav')
        self.som_sair        = SoundLoader.load('somSair.wav')

    def selecione(self,text):
        if text == 'Aguas Termais':
            self.ids.mensagem.text= '[b][color=#FF69B4]Aguas Termais atinge a temperatura máxima de 37°C [/color][/b]'
            self.minha_imagem= 'aguaTermal.png'
            self.som_aguaTermal.play()
        elif text == 'Ferro':
            self.ids.mensagem.text= '[i][color=#FF3333]Ferro atinge a temperatura máxima de 200°C [/color][/i]'
            self.minha_imagem= 'ferro.png'
        elif text == 'Fogueira':
            self.ids.mensagem.text= '[u][color=#00FF00]Fogueira atinge a temperatura máxima de 897°C [/color][/u]'
            self.minha_imagem= 'fogueira.png'
            self.som_fogueira.play()
        elif text == 'Forno':
            self.ids.mensagem.text= '[i][color=#4B0082]Forno atinge a temperatura máxima de 280°C [/color][/i]'
            self.minha_imagem= 'forno.png'
        elif text == 'Raio':
            self.ids.mensagem.text= '[b][color=#FF7F50]Raio atinge a temperatura máxima de 30 000°C[/color][/b]'
            self.minha_imagem= 'raio.png'
            self.som_raio.play()
        elif text == 'Secador':
            self.ids.mensagem.text= '[u][color=#FFFF00]Secador atinge a temperatura máxima de 90°C [/color][/u]'
            self.minha_imagem= 'secador.png'
            self.som_secador.play()                                                


    def controla_som(self, situacao):
        if situacao:
            self.som_aguaTermal  = 1
            self.som_fogueira    = 1
            self.som_raio        = 1
            self.som_secador     = 1
            self.som_sair        = 1

        else:
            self.som_aguaTermal  = 0
            self.som_fogueira    = 0
            self.som_raio        = 0
            self.som_secador     = 0
            self.som_sair        = 0

    def sair(self):
        self.som_sair.play()
        Clock.schedule_once(self.encerrar,2)
        
    def encerrar(self,valor):
        App.get_running_app().stop()


class TemperaturasApp(App):
    def build(self):
        self.title= 'Meios de Transporte'
        return Principal()


temperatura = TemperaturasApp()
temperatura.run()      
