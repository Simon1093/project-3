from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId

from flask import Flask, render_template, redirect, request

from repositories import PostRepository
from models import Post


app = Flask('myblog')

post_repo = PostRepository()


@app.route('/')
def main():
    return redirect(f'/page/0')


@app.route('/page/<page>')
def page(page):
    try:
        page = int(page)
    except ValueError:
        return redirect(f'/page/0')
    from_db = post_repo.find({}, skip=page*10, limit=10)
    if from_db is None:
        from_db = []
    posts = [post.to_json() for post in from_db]
    return render_template('posts.html', posts=posts, current_page=page)


@app.route('/post/<post_id>')
def post(post_id):
    try:
        post_id = ObjectId(post_id)
    except InvalidId:
        return redirect(f'/page/0')
    from_db = post_repo.find_one({'_id': post_id})
    if from_db is None:
        return redirect(f'/page/0')
    post = from_db.to_json()
    return render_template('post.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    attrs = {}
    title = request.form.get('title')
    attrs['title'] = request.form.get('title')
    attrs['text'] = request.form.get('text')
    attrs['datetime'] = datetime.now()
    post = Post(attrs)
    post_id = post_repo.insert_one(post)
    return redirect(f'/post/{post_id}')


if __name__ == '__main__':
    app.run()
