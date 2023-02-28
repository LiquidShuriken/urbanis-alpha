from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # code to retrieve user with specified ID
    return user_data

@app.route('/login')
def login():
    session['username'] = 'example_user'
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return render_template("welcome.html", username=username)
    else:
        return 'You need to log in first.'

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Get the data from the form
        mf = request.form['MF']
        color = request.form['color']
        sport = request.form['sport']
        
        # Do something with the data
        print("Fashion choice:", mf)
        print("The user's favorite color is", color)
        print("The user's favorite sport is", sport)
        
        # Redirect to a thank you page
        return render_template('thank_you.html')
    else:
        # Display the form to the user
        return render_template('survey.html')

@app.route('/thank-you')
def thank_you():
    return 'Thank you for your response!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
