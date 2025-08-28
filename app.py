from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Legacy index.html removed; root permanently redirects to canonical update slug
    return redirect(url_for('june_2025_business_cycle_update'), code=301)

@app.route('/june-2025-business-cycle-update')
def june_2025_business_cycle_update():
    return render_template('june-2025-business-cycle-update.html')

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
