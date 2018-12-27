# -*- coding: utf-8 -*-
import webbrowser


class Movie():
    """ Class Movie - define as váriáves que podem ser utilizadas e a
    função show_trailer() que reproduz o trailer de cada instancia. """

# Função init da classe, recebe os parametros e atribui às variáveis.
    def __init__(self, m_title, m_storyline, poster, trailer, lancamento):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.lancamento = lancamento


# Método que reproduz o trailer através do link recebido.
def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
