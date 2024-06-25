from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms import LoginForm, RegisterForm
from models import User, users  # Import users
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

def scrape_indeed_jobs(keyword, location=''):
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    options.add_argument("--accept-language=en-US,en;q=0.9")
    options.add_argument("--accept-encoding=gzip, deflate, br")

    driver = uc.Chrome(options=options)
    driver.get(url)
    time.sleep(20)

    content = driver.page_source
    driver.quit()

    soup = BeautifulSoup(content, 'html.parser')
    job_cards = soup.find_all('div', class_='slider_item css-mk9n32 eu4oa1w0')

    jobs = []

    for job_card in job_cards:
        title_elem = job_card.find('h2', class_='jobTitle')
        title = title_elem.text.strip() if title_elem else 'N/A'

        company_elem = job_card.find('span', attrs={'data-testid': 'company-name'})
        company = company_elem.text.strip() if company_elem else 'N/A'

        location_elem = job_card.find('div', attrs={'data-testid': 'text-location'})
        location = location_elem.text.strip() if location_elem else 'N/A'

        summary_elem = job_card.find('ul')
        summary = summary_elem.text.strip() if summary_elem else 'N/A'

        link_elem = job_card.find('a', href=True)
        link = 'https://www.indeed.com' + link_elem['href'] if link_elem else 'N/A'

        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'summary': summary,
            'link': link
        })

    return jobs

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        location = request.form['location']
        return redirect(url_for('results', keyword=keyword, location=location))
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    keyword = request.args.get('keyword')
    location = request.args.get('location')
    jobs = scrape_indeed_jobs(keyword, location)
    
    if request.method == 'POST':
        selected_jobs = request.form.getlist('selected_jobs')
        # Process selected jobs (e.g., apply to jobs)
        return "Applied to selected jobs!"  # Placeholder response
    
    return render_template('results.html', jobs=jobs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_username(form.username.data)
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.find_by_username(form.username.data) is None:
            user_id = str(len(users) + 1)
            User.register(user_id, form.username.data, form.password.data)
            flash('Registration successful, please log in.')
            return redirect(url_for('login'))
        flash('Username already exists')
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
