from flask import Flask, request, render_template
from figma_service import FigmaService
from design_linter import DesignLinter
import sys
print("Python Path:", sys.path)
print("Python Executable:", sys.executable)
app = Flask(__name__)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            figma_link = request.form.get("figma_link")
            if not figma_link:
                return "No URL provided", 400
                
            file_key = extract_file_key(figma_link)
            figma = FigmaService(access_token="YOUR_FIGMA_TOKEN")
            design_data = figma.get_file(file_key)
            return render_template("report.html", data=design_data)
            
        except ValueError as e:
            return f"Error: {str(e)}", 400
        except Exception as e:
            return f"Server error: {str(e)}", 500
            
    return render_template("index.html")

def extract_file_key(url):
    """Extracts file key from both old and new Figma URL formats"""
    # Remove any query parameters or fragments
    clean_url = url.split('?')[0].split('#')[0]
    
    # Handle both formats:
    # - Old: https://www.figma.com/file/FILE_KEY/project-name
    # - New: https://www.figma.com/design/FILE_KEY/project-name
    for prefix in ['/file/', '/design/']:
        if prefix in clean_url:
            parts = clean_url.split(prefix)
            if len(parts) > 1:
                return parts[1].split('/')[0]
    
    raise ValueError("Invalid Figma URL format. Must contain '/file/' or '/design/'")

if __name__ == "__main__":
    app.run(debug=True)  # This line launches the server