from flask import Flask, render_template
app = Flask(__name__)

## Create a template, link the static CSS therein 

@app.route('/')
def default_board():
    return render_template('index.html', row = 8, column = 8, color_one = "red", color_two = "black") ## 8x8 checkboard to be the default

@app.route('/<int:rows>')
def custom_rows(rows):
    return render_template('index.html', row = rows, column = 8, color_one = "red", color_two = "black")

@app.route('/<int:rows>/<int:cols>')
def custom_dimensions(rows, cols):
    return render_template('index.html', row = rows, column = cols, color_one = "red", color_two = "black")

@app.route('/<int:rows>/<int:cols>/<string:custom_color_one>/<string:custom_color_two>')
def custom_board(rows, cols, custom_color_one, custom_color_two):
    return render_template('index.html', row = rows, column = cols, color_one = custom_color_one, color_two = custom_color_two)

if __name__=="__main__":
    app.run(debug=True)