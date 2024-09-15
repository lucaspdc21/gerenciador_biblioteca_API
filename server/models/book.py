class Book:
    def __init__(self, title: str, genre: str = "", year: str = "", author_id: str = ""):
        self.title = title
        self.genre = genre
        self.year = year
        self.author_id = author_id

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'genre': self.genre,
            'year': self.year,
            'author_id': self.author_id
        }
