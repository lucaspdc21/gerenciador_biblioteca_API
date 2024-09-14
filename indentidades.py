class book:
        def __init__(self, title, **kwargs):
            self.title = title
            self.genre = kwargs.get(genre, None)
            self.year = kwargs.get(year, None)
            self.author = kwargs.get(author, None)
    
class author:
    def __init__(self, name, **kwargs):
        self.name= title
        self.birthday = kwargs.get(birthday, None)
        self.nationality = kwargs.get(nationality, None)