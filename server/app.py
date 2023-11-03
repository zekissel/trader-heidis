from flask import Flask, request
from schema import db

app = Flask(__name__)
app.config.update(dict(
	SECRET_KEY='devkey',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
))
db.init_app(app)


# clear all models and reinitialize
@app.cli.command('initdb')
def initdb_command():
	db.drop_all()
	db.create_all()

	db.session.commit()
	print('Reinitialized the database.')


@app.route('/submit_order', methods=['POST'])
def add_recipe():

	return {'test': 'success'}, 200