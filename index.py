from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route('/')
def hello_world():
	df = pd.read_csv('C:/Users/오동현/Desktop/check/ChurchMember.csv', engine='python', encoding='cp949')
	index = list(df.columns)
	return render_template("index.html", value=df.values, index=index)

	

if __name__ == '__main__':
	app.run()