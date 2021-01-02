from flask import Flask, render_template
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
    
@app.route('/projects/<project>')
def projects(project):
	with open('static/projects.txt') as f:
		projects = f.read()
	projects = ast.literal_eval(projects)

	for project in projects:
		if project == project['heading']:
			project = project

	return render_template('projects.html', project=project)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
