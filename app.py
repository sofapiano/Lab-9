from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('где я батрачила')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(250))
    term = db.Column(db.Integer)

    def __repr__(self):
        return '<Company {self.id}/{self.term} months> {self.company}'


@app.route('/')
def main():
    works = Work.query.all()
    return render_template('index.html', 
                           works_list=works)


@app.route('/work', methods = ['POST'])
def create_work():
    data = request.json
    work = Work(**data)
    db.session.add(work)
    db.session.commit()
    return 'ok'


@app.route('/clear', methods=['POST'])
def clear_works():
    try:
        db.session.query(Work).delete()
        db.session.commit()
        return 'ok'
    except Exception as e:
        db.session.rollback()
        return str(e), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)