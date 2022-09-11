import get_country




from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
	<form action = "http://localhost:5000/result" method = "POST">
         Name: <input type = "text" name = "country_name" />
         <input type = "submit" value = "submit" />
    	</form>"""

@app.route("/result", methods=['POST'])
def result():
    user_input =  request.form.to_dict()["country_name"]
    return get_country.get_country_language(user_input)
    
if __name__ == "__main__":
    app.run(debug=True)
