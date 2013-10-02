#!bin/python3.3
from flask import Flask, render_template, request, session, url_for, redirect, escape
from hashlib import md5, sha256

app = Flask(__name__)

userfile = "./users.txt"
salt = "+TmLir8DYItc0QSYg3SRR4k7X76K+/VfHxjb0LAQq/hZOIFthHqDy7vJI++5t847lQedi/IdVkJLnl66kXDzGxie0yfm0Nx0oqy8Dbe07qO32NPUP"
app.secret_key = '6G4NGaSXTpMSyKe9sjjOr+V45cOkMt7wkujITavSie5O331bovDRbSae4BxKaztonU9FBcbuV6n2F9CBZ6pXYFht/PLAWYPKroi7/M4K+FERzSnuK44xmTwx6OjtQL4mwstO+NvXCAeMRdKmnhqFF+kWWAcJnNNaKlMQqyth2iu/fasr6ZKooJ50ziPv/B2CV6soaUKKfXcSghtZ6hXI1aRZ/pxzjxTmnZt6K12Spwb4XJPnXBlyuY4WilsgatFO92vVRsO3xSCMneubhZOBU13sJdSRetRhbnsGoSFKO+JrvR1wppENPnitfBDcJl2HnhIYYBlK9qYrJIN/PrpWzXJNNJ3AlUjY+c6HPiHdrVE7nc+T5O0p8hJCNWMn56Ka25JxXCN6AfEZqCdHMYrQD1X8jJMpSY4+HyJIyEcco9f2Aj4DKRJlc6efJMysJN+tC+BEnYlEUA7s/y6vli7iV3TlBcayX4i4fm3TFpgNxm7vHL5JVzbxSlOVO+GdKyisV2VnNilyDAq5T7hMW1aTFPDRrMjRejhf8VT5cqiHZO1SAva+y2Uo8d1dnfG1vEVrj0t8UEdENmvEMTJp14oTKZ20cNvD+m2K+PqDtaCqPvTK17xuYfgEIPo3whsdiwdRyH3oBv5iK23NNjhBklNXEjmQ6BqSXrFsnza/n8VSIscWU4iyQmP6SHVzcOXCOTVwpgtK73+fL9MJNskfhGg6GxGS9Atmut1UqHIwaJoemp7ZkQAXyOiFb89bJ1xjDN75ap6oP/aSBKmaYxJ7Kg9LkfbnsPBWSL+eBJT4MwYplZwg9f/V6ccV6dKsOFTX0oQ9OpWpYQdi3C8N1/1fksQzsdibfNjnotTMaQyo9Cn1Y7hg3/g9TfFhRUbXFJcKk/qGCIDHyQ58q+XYjxeg8u5Y0cD6SL+UsRQwwljcn+iLd+cI7Q/WjzhQLhuozNzo5uPlZ9DFv+dHFlWYrUUo89/7+WoKAg8J42TfbaX6WNM9RagbQRMF+P5BrAMJbpfk6OsUH4t6St5L9jRz9B588MTncOxWsSzyDpgZSO81amgN0//Wj+EY7bhgYtGC2KTWSnr0JyWTc6+PeOpC9wqPlwWG3/c2vWA+7dtaoQh4HdVoLN3FFFzbszBNQJyhZhBwl3sp+y1oLYOKO3zjG7++RwiivQgi/mmJbHi7bR6fEJCjh5BDtuplrGrfM6TAolv6A4OU/JpNJd2niNTazsSwwO5ktLtrruhjSl6UVIvu4BCNXieRNcIc/6O9eqn9jPk2VF1G5pHTytfyFXRo7mL/+wKPjfcD5JNwEpD0xUh40V2SrlZox54LxAZNthm6KI6+kQjt6LntaWaJ5U8fAe7x3JKnNszh7gkWX84NsUe7d4eDD8VtBVHRS+ukBQ+6U4CJ5MoqKFiCgtAcVjN+d+i/OvAeIAY5M+OZOfAZUkV4irSvhvsyo2K1Y9uqgk/8TlSdSyaM7'

#########################
# Helper functions      #
#########################

def valid_login(user, pw):
    global userfile
    # Read userfile
    try:
        f = open(userfile)
        users = f.readlines()
        f.close()
    except:
        return False
    # separate user, salted password and todofile
    users_splitted = []
    for u in users:
        users_splitted.append(u.split())
    del users
    # Calculate Salted pw
    md5_plus_salt = md5(pw.encode('utf-8')).hexdigest() + salt
    salted = sha256(md5_plus_salt.encode('utf-8')).hexdigest()
    for u in users_splitted:
        if u[0] == user and u[1] == salted:
            session['todofile'] = u[2]
            return True
    return False
    

def get_todos():
    todos = []
    i = 0
    try:
        f = open(session['todofile'])
        for line in f.readlines():
            todos.append([escape(line), i])
            i = i +1
        f.close()
        return todos
    except:
        return [["Dateifehler beim holen der Todos.", 42000000000]] # Yeah you shouldn't do thinks like this.
def mkerror(title, text):
    return render_template("error.html", errortitle=title, errortext=text, css=url_for('static', filename='css/bootstrap.css'), js=url_for('static',filename='js/bootstrap.min.js'))

#########################
# The Pages             #
#########################

# Main Page
@app.route('/')
def index():
    if 'username' in session:
        return render_template("todos.html", todos=get_todos(), css=url_for('static', filename='css/bootstrap.css'),  js=url_for('static',filename='js/bootstrap.min.js'))
    else:
        return render_template("loginform.html", css=url_for('static', filename='css/bootstrap.css'),  js=url_for('static',filename='js/bootstrap.min.js'))

# Todo managment
@app.route('/add', methods=['POST'])
def add():
    try:
        if 'username' in session:
            f = open(session['todofile'], "a")
            f.write(request.form['todo'] + "\n")
            f.close()
            app.logger.debug("Added Todo")
        return redirect(url_for('index'))
    except:
        return mkerror("Dateifehler", "Fehler beim bearbeiten der Datei")

@app.route('/delete', methods=['POST'])
def delete():
    try:
        if 'username' in session:
            f = open(session['todofile'], "r")
            todos = f.readlines()
            f.close()
            del todos[int(request.form['delete'])]
            f = open(session['todofile'], "w")
            for t in todos:
                f.write(t)
            f.close()
            app.logger.debug("To delete: " + request.form["delete"])
        return redirect(url_for('index'))
    except:
        return mkerror("Dateifehler", "Fehler beim bearbeiten der Datei")

# Login/Logout
@app.route('/login', methods=['POST'])
def login():
    if valid_login(request.form['username'], request.form['password']):
         session['username'] = request.form['username']
         app.logger.debug("Login by " + session['username'])
         return redirect(url_for('index'))
    else:
        app.logger.debug("Failed login")
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    app.logger.debug("Logout by " + session['username'])
    session.pop('username', None)
    session.pop('todofile', None)
    return redirect(url_for('index'))

# Run it
if __name__ == '__main__':
    app.run(debug=True)