from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "skillher_secret"

DATABASE = "models.db"

# -------------------------
# DB Connection
# -------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------
# LANDING
# -------------------------
@app.route("/")
def landing():
    return render_template("landing.html")


# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        conn = get_db()
        conn.execute("""
            INSERT INTO users (name, email, password, skill_offered, skill_wanted, level)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            request.form["name"],
            request.form["email"],
            request.form["password"],
            request.form["skill_offered"],
            request.form["skill_wanted"],
            request.form["level"]
        ))
        conn.commit()
        conn.close()

        session["user"] = request.form["name"]
        return redirect("/dashboard")

    return render_template("register.html")

# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE name=? AND password=?",
            (request.form["name"], request.form["password"])
        ).fetchone()
        conn.close()

        if user:
            session["user"] = user["name"]
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":
        skill_offered = request.form["skill_offered"]
        skill_wanted = request.form["skill_wanted"]

        conn.execute("""
            UPDATE users
            SET skill_offered=?, skill_wanted=?
            WHERE name=?
        """, (skill_offered, skill_wanted, session["user"]))

        conn.commit()
        conn.close()

        return redirect("/dashboard")

    # GET method → load existing skills
    user = conn.execute(
        "SELECT * FROM users WHERE name=?",
        (session["user"],)
    ).fetchone()

    conn.close()

    return render_template("edit_profile.html", user=user)

# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    current_user = session["user"]

    # Get logged-in user details
    me = conn.execute(
        "SELECT * FROM users WHERE name=?",
        (current_user,)
    ).fetchone()

    # Get all other users
    all_users = conn.execute(
        "SELECT * FROM users WHERE name != ?",
        (current_user,)
    ).fetchall()

    matches = []

    for other in all_users:
        if (
            me["skill_offered"] == other["skill_wanted"] and
            other["skill_offered"] == me["skill_wanted"]
        ):
            matches.append(other["name"])

    user_requests = conn.execute("""
        SELECT * FROM swap_requests
        WHERE sender = ? OR receiver = ?
    """, (current_user, current_user)).fetchall()

    conn.close()
    print(matches)
    return render_template(
        "dashboard.html",
        user=me,   # ✅ send full user row
        current_user=current_user,
        matches=matches,
        swap_requests=user_requests
    )


# -------------------------
# SEND REQUEST
# -------------------------
@app.route("/send_request/<username>")
def send_request(username):

    if "user" not in session:
        return redirect("/login")

    sender = session["user"]
    receiver = username

    conn = get_db()

    # ✅ Check if request already exists
    existing = conn.execute("""
        SELECT * FROM swap_requests
        WHERE sender=? AND receiver=?
    """, (sender, receiver)).fetchone()

    if existing:
        conn.close()
        return "Request already sent!"

    # ✅ Insert only if not exists
    conn.execute(
        "INSERT INTO swap_requests (sender, receiver, status) VALUES (?, ?, ?)",
        (sender, receiver, "Pending")
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")


# -------------------------
# ACCEPT REQUEST
# -------------------------
@app.route("/accept_request/<int:req_id>")
def accept_request(req_id):

    conn = get_db()
    conn.execute("""
        UPDATE swap_requests
        SET status = 'Accepted'
        WHERE id = ?
    """, (req_id,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")


# -------------------------
# REJECT REQUEST
# -------------------------
@app.route("/reject_request/<int:req_id>")
def reject_request(req_id):

    conn = get_db()
    conn.execute("""
        UPDATE swap_requests
        SET status = 'Rejected'
        WHERE id = ?
    """, (req_id,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

@app.route("/chat/<username>", methods=["GET", "POST"])
def chat(username):
    if "user" not in session:
        return redirect("/login")

    conn = get_db()

    if request.method == "POST":
        message = request.form["message"]

        conn.execute(
            "INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)",
            (session["user"], username, message)
        )
        conn.commit()

    # Fetch conversation (both directions)
    messages = conn.execute("""
        SELECT * FROM messages
        WHERE (sender=? AND receiver=?)
        OR (sender=? AND receiver=?)
        ORDER BY timestamp
    """, (session["user"], username, username, session["user"])).fetchall()

    conn.close()

    return render_template("chat.html", messages=messages, username=username)

@app.route("/get_messages/<username>")
def get_messages(username):
    if "user" not in session:
        return ""

    conn = get_db()

    messages = conn.execute("""
        SELECT * FROM messages
        WHERE (sender=? AND receiver=?)
        OR (sender=? AND receiver=?)
        ORDER BY timestamp
    """, (session["user"], username, username, session["user"])).fetchall()

    conn.close()

    result = ""
    for msg in messages:
        result += f"<p><b>{msg['sender']}:</b> {msg['message']}</p>"

    return result

if __name__ == "__main__":
    app.run(debug=True)