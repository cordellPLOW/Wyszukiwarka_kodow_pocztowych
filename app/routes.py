import csv
from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models.models import Postcode
from app.forms import CitynameSearchForm, PostcodeSearchForm


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cityname_search', methods=['GET', 'POST'])
def cityname_search():
    form = CitynameSearchForm()
    data = None
    if form.validate_on_submit():
        data = Postcode.query.filter_by(town=form.town.data).order_by(Postcode.address.asc()).all()
        if not data:
            flash("Nie znaleziono danych na podstawie przekazanych informacji", category="info")
    return render_template('cityname_search.html', form=form, data=data)


@app.route('/postcode_search', methods=['GET', 'POST'])
def postcode_search():
    form = PostcodeSearchForm()
    data = None
    if form.validate_on_submit():
        data = Postcode.query.filter_by(code=form.code.data).order_by(Postcode.address.asc()).all()
        if not data:
            flash("Nie znaleziono danych na podstawie przekazanych informacji", category="info")
    return render_template('postcode_search.html', form=form, data=data)


@app.route('/drop_all_postcodes')
def drop_all_postcodes():
    db.session.query(Postcode).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/from_csv')
def from_csv():
    with open("kody.csv", encoding="utf-8-sig") as f:
        postal_codes = csv.DictReader(f, delimiter=";")
        for post_code in postal_codes:
            row = Postcode(
                code = post_code['KOD POCZTOWY'],
                address = post_code['ADRES'],
                town = post_code['MIEJSCOWOŚĆ'],
                province = post_code['WOJEWÓDZTWO'],
                county = post_code['POWIAT'])
            db.session.add(row)
        db.session.commit()

    return "Dodano dane z pliku csv do bazy danych"
