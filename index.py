import subprocess
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, flash
from main import DecryptionModule

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', "POST"])
def result():
    if request.method == 'POST':
        search = request.form['method']
        key = request.form.get('key', None)
        print(search, key)
        if key is not None and key.isnumeric():
            key = int(key)
        elif key is not None and key.isalpha():
            key = str(key)
        else:
            key = None
        decryption_module = DecryptionModule()
        if decryption_module.status_code == 404:
            return render_template('errorpage.html')
        method, decrypted_text = decryption_module.decode(search, key)[:2]
        print(search, key)
        if method is None:
            return render_template('index.html', identified_methods=None, method="Method not identified")

        return render_template('index.html', identified_methods=decrypted_text, method=method)


    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=4000)
