from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fotografi.db'
db = SQLAlchemy(app)

class Fotografija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(100), nullable=False)
    prezime = db.Column(db.String(100), nullable=False)
    vrsta = db.Column(db.String(100), nullable=False)
    detalji = db.Column(db.Text, nullable=False)
    portfolio = db.Column(db.String(200), nullable=False)
    cijena = db.Column(db.Float, nullable=False)
    ocjena = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'vrsta': self.vrsta,
            'detalji': self.detalji,
            'portfolio': self.portfolio,
            'cijena': self.cijena,
            'ocjena': self.ocjena
        }

def create_db():
    with app.app_context():
        db.create_all()

create_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/popis_fotografa')
def popis_fotografa():
    search_query = request.args.get('search', '', type=str)
    sort_option = request.args.get('sort', 'cijena_desc', type=str)

    fotografije = Fotografija.query
    if search_query:
        search = f"%{search_query}%"
        fotografije = fotografije.filter(
            (Fotografija.ime.ilike(search)) |
            (Fotografija.prezime.ilike(search)) |
            (Fotografija.vrsta.ilike(search))
        )

    if sort_option == 'ocjena_asc':
        fotografije = fotografije.order_by(Fotografija.ocjena).all()
    elif sort_option == 'ocjena_desc':
        fotografije = fotografije.order_by(Fotografija.ocjena.desc()).all()
    elif sort_option == 'cijena_asc':
        fotografije = fotografije.order_by(Fotografija.cijena).all()
    elif sort_option == 'cijena_desc':
        fotografije = fotografije.order_by(Fotografija.cijena.desc()).all()
    else:
        fotografije = fotografije.all()

    return render_template('vrati.html', data=fotografije)

@app.route('/dodaj_fotografa', methods=['GET', 'POST'])
def dodaj_fotografa():
    if request.method == 'POST':
        ime = request.form['ime']
        prezime = request.form['prezime']
        vrsta = request.form['vrsta']
        detalji = request.form['detalji']
        portfolio = request.form['portfolio']
        cijena = float(request.form['cijena'])
        ocjena = float(request.form['ocjena'])

        nova_fotografija = Fotografija(ime=ime, prezime=prezime, vrsta=vrsta, detalji=detalji, portfolio=portfolio, cijena=cijena, ocjena=ocjena)

        db.session.add(nova_fotografija)
        db.session.commit()

        return redirect(url_for('popis_fotografa'))
    return render_template('dodaj.html')

@app.route('/fotografija/<int:fotografija_id>', methods=['POST', 'DELETE'])
def obrisi_fotografa(fotografija_id):
    fotografija = Fotografija.query.get_or_404(fotografija_id)
    if request.method == 'DELETE':
        db.session.delete(fotografija)
        db.session.commit()
        return jsonify({'response': 'Success'})
    return redirect(url_for('popis_fotografa'))

@app.route('/uredi_fotografa/<int:fotografija_id>', methods=['GET', 'POST'])
def uredi_fotografa(fotografija_id):
    fotografija = Fotografija.query.get_or_404(fotografija_id)
    if request.method == 'POST':
        fotografija.ime = request.form['ime']
        fotografija.prezime = request.form['prezime']
        fotografija.vrsta = request.form['vrsta']
        fotografija.detalji = request.form['detalji']
        fotografija.portfolio = request.form['portfolio']
        fotografija.cijena = float(request.form['cijena'])
        fotografija.ocjena = float(request.form['ocjena'])
        db.session.commit()
        return redirect(url_for('popis_fotografa'))
    return render_template('uredi.html', fotografija=fotografija)

@app.route('/vizualizacija')
def vizualizacija():
    return render_template('vizualizacija.html')

@app.route('/api/fotografi')
def get_fotografi():
    fotografije = Fotografija.query.all()
    return jsonify([fotografija.to_dict() for fotografija in fotografije])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

