from flask import Flask, render_template, redirect, url_for
from collections import OrderedDict
import ast

app = Flask (__name__)

@app.route('/')
def index():
	with open('static/projects.txt') as f:
		projects = f.read()
	projects = ast.literal_eval(projects)
	#print (projects)
	return render_template('index.html', projects=projects)
    
@app.route('/projects/<project_url>')
def projects(project_url):
	with open('static/projects.txt') as f:
		projects = f.read()
	projects = ast.literal_eval(projects)
	print(project_url)
	
	for item in projects:
		print(item['heading'])
		if project_url == item['heading'].lower():
			project = item
			print(project)
			return render_template('projects.html', project=project)

	#catch bad URL and redirect home
	return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
