from flask import Flask, render_template
import subprocess
import script

app = Flask(__name__, template_folder=".")
@app.route('/')
def index():
    # Call the script.py file and capture its output
    output = script.get_top_searches()
    # Split the output into a list of top searches
    top_searches = output.split(',')

    # Render the index.html template and pass the top searches as a variable
    return render_template('index.html', top_searches=top_searches)


if __name__ == '__main__':
    app.run(port=5000, debug=True)