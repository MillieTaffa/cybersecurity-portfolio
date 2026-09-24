from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
  <head><title>Vulnerable Demo</title></head>
  <body>
    <h1>Local Vulnerable Demo</h1>
    <form method="POST">
      <label for="username">Username:</label>
      <input type="text" name="username" id="username">
      <button type="submit">Login</button>
    </form>
    <p>Demo note: this intentionally shows unsafe SQL-style handling.</p>
    {% if result %}
      <p>Result: {{ result }}</p>
    {% endif %}
  </body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        username = request.form.get('username', '')
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        result = f"Unsafe query: {query}"

    return render_template_string(HTML, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
