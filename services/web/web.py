from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return '''<!DOCTYPE html>
<html>
<head>
<title>Projector 13 Homework</title>
</head>

<body>
<h1>Hello World</h2>
</body>

</html> 
'''

