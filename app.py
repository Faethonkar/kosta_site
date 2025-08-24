from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/set_agreement', methods=['POST'])
def set_agreement():
    resp = make_response(redirect('/'))
    resp.set_cookie('agreed_terms', 'yes', max_age=60*60*24*365)
    return resp

@app.route('/')
def home():
    agreed = request.cookies.get('agreed_terms')
    if not agreed:
        return redirect('/terms_of_use')
    return render_template('index.html')

@app.route('/terms_of_use', methods=['GET', 'POST'])
def terms_of_use():
    agreed = request.cookies.get('agreed_terms')
    if agreed:
        return redirect('/')
    if request.method == 'POST':
        resp = make_response(redirect('/'))
        resp.set_cookie('agreed_terms', 'yes', max_age=60*60*24*365)
        return resp
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
