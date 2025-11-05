from flask import Flask, request, redirect, make_response, render_template_string

app = Flask(__name__)

# Хранилище комментариев (в памяти)
comments = []

@app.route("/")
def index():
    return """
    <h1>CF Demo is working!</h1>
    <ul>
        <li>/loginLogin</a></li>
        <li>/searchSearch</a></li>
        <li>/commentComments</a></li>
        <li>/redirect?next=https://example.comOpen Redirect</a></li>
    </ul>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "password123":
            resp = make_response("Welcome, admin!")
            resp.set_cookie("session", "admin-session-token")
            return resp
        else:
            return "Invalid credentials", 401
    return '''
    <h2>Login</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route("/search")
def search():
    query = request.args.get("q", "")
    # Симуляция SQL-инъекции (на самом деле не подключается к БД)
    return f"<h2>Search Results for: {query}</h2>"

@app.route("/comment", methods=["GET", "POST"])
def comment():
    global comments
    if request.method == "POST":
        text = request.form.get("comment")
        comments.append(text)
    comment_list = "<br>".join(comments)
    return f'''
    <h2>Leave a Comment</h2>
    <form method="POST">
        <textarea name="comment"></textarea><br>
        <input type="submit" value="Post">
    </form>
    <h3>All Comments:</h3>
    {comment_list}
    '''

@app.route("/redirect")
def open_redirect():
    next_url = request.args.get("next", "/")
    return redirect(next_url)

@app.route("/admin")
def admin():
    session = request.cookies.get("session")
    if session == "admin-session-token":
        return "Welcome to the admin panel!"
    else:
        return "Access denied", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
