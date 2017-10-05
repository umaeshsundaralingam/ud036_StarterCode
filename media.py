import webbrowser
class Movie():
    #Default Constructor -- Initializes objects created
    def __init__(self,movie_title,movie_director,movie_trailer,poster_image,movie_storyline):
        self.title = movie_title
        self.director = movie_director
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster_image
        self.storyline = movie_storyline
    def show_trailer(self):
        webbrowser.open(self,trailer)
    
