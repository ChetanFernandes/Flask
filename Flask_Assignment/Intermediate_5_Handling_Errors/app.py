from flask import Flask
from flask import render_template, request,abort

app = Flask(__name__)

# Handling of 404 error code
@app.route("/404")
def error_404():
    abort(404)

@app.errorhandler(404)
def not_found(e):
    print(e)
    return render_template("404.html")

# Handling of 502 error code
@app.route("/502")
def error_502():
    abort(502)

@app.errorhandler(502)
def not_found(e):
    app.logger.error(f"Server error:{e}, route: {request.url}")
    return render_template("502.html")



if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5001)