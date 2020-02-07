class Newws:
    '''
    Newws class that defines new objects
    '''

    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.description = description
        # self.url = url
        # self.category = category
        # self.country = country


class Articles:
    '''
    Article class that defines the article objects
    '''

    def __init__(self, author, title, description, url, urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage