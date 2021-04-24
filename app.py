from flask import Flask, render_template #, flash, request, redirect, render_template



# Create the flask app
app = Flask(__name__)

# Create the route for homepage upload.html
@app.route('/')
def upload_form():
    return render_template('home.html')

# # Create the route for the about me page
# @app.route('/about', methods=['GET', 'POST'])
# def about_page():
#     return render_template('about.html')
#
#
# # Create the route for the portfolio page
# @app.route('/portfolio', methods=['GET', 'POST'])
# def portfolio_page():
#     return render_template('portfolio.html')
#
#
# # Create the route for resume page
# @app.route('/resume', methods=['GET', 'POST'])
# def resume_page():
#     return render_template('resume.html')
#
# # Create the route for the Contact Me page
# @app.route('/contact', methods=['GET', 'POST'])
# def contactpage():
#     return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)

