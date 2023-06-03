from flask import Flask, jsonify, request

app = Flask(__name__)


class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content


class Comment:
    def __init__(self, id, text, post_id):
        self.id = id
        self.text = text
        self.post_id = post_id


class Blog:
    def __init__(self, id, name):
        self.id = id
        self.name = name


posts = []
comments = []
blogs = []

# Эндпоинты для крад поста
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify([post.__dict__ for post in posts])

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = Post(len(posts) + 1, data['title'], data['content'])
    posts.append(post)
    return jsonify(post.__dict__)

@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = next((post for post in posts if post.id == id), None)
    if post:
        return jsonify(post.__dict__)
    return jsonify({'error': 'Post not found'}), 404

@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = next((post for post in posts if post.id == id), None)
    if post:
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        return jsonify(post.__dict__)
    return jsonify({'error': 'Post not found'}), 404

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = next((post for post in posts if post.id == id), None)
    if post:
        posts.remove(post)
        return jsonify({'message': 'Post deleted'})
    return jsonify({'error': 'Post not found'}), 404

# Эндпоинты для крад коммент
@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify([comment.__dict__ for comment in comments])

@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = Comment(len(comments) + 1, data['text'], data['post_id'])
    comments.append(comment)
    return jsonify(comment.__dict__)

@app.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    comment = next((comment for comment in comments if comment.id == id), None)
    if comment:
        return jsonify(comment.__dict__)
    return jsonify({'error': 'Comment not found'}), 404

@app.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = next((comment for comment in comments if comment.id == id), None)
    if comment:
        data = request.get_json()
        comment.text = data['text']
        return jsonify(comment.__dict__)
    return jsonify({'error': 'Comment not found'}), 404

@app.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = next((comment for comment in comments if comment.id == id), None)
    if comment:
        comments.remove(comment)
        return jsonify({'message': 'Comment deleted'})
    return jsonify({'error': 'Comment not found'}), 404

# Эндпоинты для крад блога
@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify([blog.__dict__ for blog in blogs])

@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog = Blog(len(blogs) + 1, data['name'])
    blogs.append(blog)
    return jsonify(blog.__dict__)

@app.route('/blogs/<int:id>', methods=['GET'])
def get_blog(id):
    blog = next((blog for blog in blogs if blog.id == id), None)
    if blog:
        return jsonify(blog.__dict__)
    return jsonify({'error': 'Blog not found'}), 404

@app.route('/blogs/<int:id>', methods=['PUT'])
def update_blog(id):
    blog = next((blog for blog in blogs if blog.id == id), None)
    if blog:
        data = request.get_json()
        blog.name = data['name']
        return jsonify(blog.__dict__)
    return jsonify({'error': 'Blog not found'}), 404

@app.route('/blogs/<int:id>', methods=['DELETE'])
def delete_blog(id):
    blog = next((blog for blog in blogs if blog.id == id), None)
    if blog:
        blogs.remove(blog)
        return jsonify({'message': 'Blog deleted'})
    return jsonify({'error': 'Blog not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
