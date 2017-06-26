# coding=utf-8

import webbrowser

'''class Movie() is used by movies.py to call functions,
especially the __init__ function. class Movie() is needed
to create instances like battlefield or ironman'''


class Movie():

    ''' __init__  when called by class Movie();
    from media.py initializes each argument for each instance.
    Ex: Battlefield has its respective arguments which gets
    passed through this function'''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

'''Instance method where it opens webbrowser plays the trailer link '''


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
