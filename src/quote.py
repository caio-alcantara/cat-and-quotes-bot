class Quote:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __str__(self):
        return f'{self.content} ({self.author})'