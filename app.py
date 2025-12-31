from flask import Flask, render_template, abort
import markdown
import os

app = Flask(__name__)

# Configuration
CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content')
README_PATH = os.path.join(CONTENT_DIR, 'README.md')

@app.route('/')
def index():
    """Renders the Home page with the project README."""
    try:
        # Read the synced README file
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert Markdown to HTML
        # Using extensions for tables, fenced code blocks, etc.
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'toc', 'smarty'])
        
        return render_template('index.html', content=html_content)
    except FileNotFoundError:
        return render_template('index.html', content="<p>README not found. Please ensure content is synced.</p>")

@app.route('/api')
def api_docs():
    """Renders the detailed API documentation page."""
    return render_template('api.html')

@app.route('/faq')
def faq():
    """Renders the FAQ / Troubleshooting page."""
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
