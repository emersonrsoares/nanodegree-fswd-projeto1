import webbrowser


class Movie():
    """ Class Movie - define as váriáves que podem ser utilizadas e tem a
    função show_trailer() que reproduz o trailer de cada instancia. """


def __init__(self, m_title, m_storyline, poster, trailer):
    self.title = m_title
    self.storyline = m_storyline
    self.poster_image_url = poster
    self.trailer_youtube_url = trailer


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
