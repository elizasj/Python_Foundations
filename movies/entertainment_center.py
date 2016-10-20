import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

field_of_dreams = media.Movie("Field of Dreams",
                              "A man hears a voice and builds a baseball field to welcome ghosts from the past",
                              "https://upload.wikimedia.org/wikipedia/en/6/6b/Field_of_Dreams_poster.jpg",
                              "https://www.youtube.com/watch?v=Ut06d4dptWo")

godfather = media.Movie("The Godfather",
                        "The story of an italian mob family",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

movies = [toy_story, avatar, field_of_dreams, godfather]
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)

# print(media.Movie.__doc__) <-- documentation
# print(media.Movie.__name__) <-- name of the class in question
# print(media.Movie.__module__) <-- name of the module that contains the class
