from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import config
import os

def create_app(config_name='default'):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Predefined valid credentials for the Cricket application
    VALID_CREDENTIALS = {
        'admin': 'cricket123',
        'user': 'password',
        'cricket_fan': 'ipl2024'
    }
    
    @app.route('/')
    def index():
        """Redirect to login page."""
        return redirect(url_for('login'))
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Handle login page display and form submission."""
        if request.method == 'POST':
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
            
            # Acceptance Criteria: Empty username or password displays validation message
            if not username or not password:
                flash('Please enter both username and password', 'error')
                return render_template('login.html')
            
            # Acceptance Criteria: Valid credentials display welcome message
            if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
                session['username'] = username
                flash(f'Welcome, {username}! You have successfully logged in to the Cricket Application.', 'success')
                return render_template('welcome.html', username=username)
            
            # Acceptance Criteria: Invalid credentials display error message
            flash('Invalid username or password', 'error')
            return render_template('login.html')
        
        # GET request - display login form
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        """Handle user logout."""
        session.pop('username', None)
        flash('You have been logged out successfully.', 'info')
        return redirect(url_for('login'))
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        return render_template('500.html'), 500
    
    return app

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV', 'development')
    app = create_app(env)
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)