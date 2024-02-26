from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template_string("""
        <h1>Blog</h1>
        <a href="/create">Créer un Article</a>
        {% for post in posts %}
            <div>
                <h2>{{ post.title }}</h2>
                <p>{{ post.content }}</p>
            </div>
        {% endfor %}
    """, posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template_string("""
        <form method="post">
            Titre: <input type="text" name="title"><br>
            Contenu:<br>
            <textarea name="content"></textarea><br>
            <input type="submit" value="Créer">
        </form>
    """)

if __name__ == '__main__':
    app.run(debug=True)
