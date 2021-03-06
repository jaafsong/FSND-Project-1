# coding=utf-8

import media
import fresh_tomatoes

# Battlefield Trailer: title, storyline, image, and game trailer.
battlefield = media.Movie("BattleField 4",
                          "Battlefield 4 gaming trailer",
                          "https://static.gamespot.com/uploads/original/1197/11970954/2369154-bf4_screen_01.png",  # NOQA
                          "https://www.youtube.com/watch?v=hl-VV9loYLw")

# Superman Movie Trailer: title, storyline, poster image, and movie trailer.
superman = media.Movie("Man of Steel",
                       "Clark Kent is forced to reveal his identity...",
                       "https://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=T6DJcgm3wNY")

# Lego: Batman Movie Trailer: title, storyline, poster image, and movie
# trailer.
batman = media.Movie("Lego: Batman",
                     "Batman takes on villains in the Lego World",
                     "https://upload.wikimedia.org/wikipedia/en/7/79/Lego_Batman%2C_The_Movie_cover.jpeg",  # NOQA
                     "https://www.youtube.com/watch?v=rGQUKzSDhrg")

# WonderWoman: title, storyline, poster image, and movie trailer.
wonderwoman = media.Movie("Wonderman",
                          "2017 Superhero on an epic adventure...",
                          "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=VSB4wGIdDwo")

# Ant-Man: title, storyline, poster image, and movie trailer.
antman = media.Movie("Ant-Man",
                     "Ant-Man taking on the world in any size...",
                     "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=pWdKf3MneyI")

# IronMan: title, storyline, poster image, and movie trailer.
ironman = media.Movie("Iron Man",
                      "Tony Stark is Iron Man...",
                      "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",  # NOQA
                      "https://www.youtube.com/watch?v=8hYlB38asDY")

# IpMan: title, storyline, poster image, and movie trailer.
ipman = media.Movie("Ip Man",
                    "Life of Bruce Lee's former Master",
                    "https://upload.wikimedia.org/wikipedia/en/3/38/The_Legend_is_Born_%E2%80%93_Ip_Man_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=nhz4Jl6nf58")

'''Array of all the movies created.'''
movies = [battlefield, superman, batman, wonderwoman, antman, ironman, ipman]

'''Takes array of instance from movies as input for open_movies_page()'''
fresh_tomatoes.open_movies_page(movies)
