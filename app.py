from flask import Flask, jsonify, request
from models import Post, Comment, Blog

app = Flask(__name__)

blogs = []


@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify([blog.__dict__ for blog in blogs])


@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    blog = Blog(len(blogs) + 1, data['name'])
    blogs.append(blog)
    return jsonify(blog.__dict__)


@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        return jsonify(blog.__dict__)
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        data = request.get_json()
        blog.name = data['name']
        return jsonify(blog.__dict__)
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        blogs.remove(blog)
        return jsonify({'message': 'Blog deleted'})
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts', methods=['GET'])
def get_posts(blog_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        return jsonify([post.__dict__ for post in blog.posts])
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts', methods=['POST'])
def create_post(blog_id):
    data = request.get_json()
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = Post(len(blog.posts) + 1, data['title'], data['content'])
        blog.posts.append(post)
        return jsonify(post.__dict__)
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>', methods=['GET'])
def get_post(blog_id, post_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            return jsonify(post.__dict__)
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>', methods=['PUT'])
def update_post(blog_id, post_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            data = request.get_json()
            post.title = data['title']
            post.content = data['content']
            return jsonify(post.__dict__)
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>', methods=['DELETE'])
def delete_post(blog_id, post_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            blog.posts.remove(post)
            return jsonify({'message': 'Post deleted'})
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(blog_id, post_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            return jsonify([comment.__dict__ for comment in post.comments])
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(blog_id, post_id):
    data = request.get_json()
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            comment = Comment(len(post.comments) + 1, data['text'], post_id)
            post.comments.append(comment)
            return jsonify(comment.__dict__)
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=['GET'])
def get_comment(blog_id, post_id, comment_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            comment = next((comment for comment in post.comments if comment.id == comment_id), None)
            if comment:
                return jsonify(comment.__dict__)
            return jsonify({'error': 'Comment not found'}), 404
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=['PUT'])
def update_comment(blog_id, post_id, comment_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            comment = next((comment for comment in post.comments if comment.id == comment_id), None)
            if comment:
                data = request.get_json()
                comment.text = data['text']
                return jsonify(comment.__dict__)
            return jsonify({'error': 'Comment not found'}), 404
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


@app.route('/blogs/<int:blog_id>/posts/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(blog_id, post_id, comment_id):
    blog = next((blog for blog in blogs if blog.id == blog_id), None)
    if blog:
        post = next((post for post in blog.posts if post.id == post_id), None)
        if post:
            comment = next((comment for comment in post.comments if comment.id == comment_id), None)
            if comment:
                post.comments.remove(comment)
                return jsonify({'message': 'Comment deleted'})
            return jsonify({'error': 'Comment not found'}), 404
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'error': 'Blog not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
