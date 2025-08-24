from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/terms_of_use')
def terms_of_use():
    return render_template('terms_of_use.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/stage_explanation')
def stage_guide():
    return render_template('stage_explanation.html')

@app.route('/newsletter_signup')
def newsletter():
    return render_template('newsletter_signup.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

if __name__ == '__main__':
    app.run(debug=True)
