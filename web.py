import sqlite3
from flask import Flask, render_template

c = sqlite3.connect("web-label.db")
c.commit()

python = c.execute("SELECT * FROM Python;").fetchall()
command = c.execute("SELECT * FROM Command;").fetchall()
sysadmin = c.execute("SELECT * FROM sysadmin;").fetchall()
latest = c.execute("SELECT * FROM Home;").fetchall()

app = Flask(__name__)
c.commit()
@app.route("/")
def make_web():
    return render_template('index.html', python=python,
    command=command, sysadmin=sysadmin, latest=latest)

def main():
    solve()

if __name__ == "__main__":
    app.run(debug=True, port=2313)