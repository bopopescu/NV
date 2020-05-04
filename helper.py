from functools import wraps
from flask import redirect, render_template, request, session, url_for

# Logged in check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# make input no space
def nospace(string):
    txt = string
    stxt = "".join(txt.strip().split()).lower()
    return stxt
