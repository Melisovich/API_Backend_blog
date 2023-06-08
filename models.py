class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.comments = []


class Comment:
    def __init__(self, id, text, post_id):
        self.id = id
        self.text = text
        self.post_id = post_id


class Blog:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.posts = []
