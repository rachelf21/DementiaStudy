from flask import render_template, current_app, request, Response
from app import app
from app.models import Participant, Visit0, Visit1, Visit2, Visit3, Visit4

num1 = 10
num2 = 25

@app.route('/')
def index():
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/view_data')
def view_data():
    participants = Participant.query.all()
    return render_template('data.html', participants = participants, num1=num1, num2=num2)

@app.route('/visit_data/<visit_num>')
def visit_data(visit_num):
    if visit_num == '0':
        visit = Visit0.query.filter(Visit0.mmse1 >= num1).filter(Visit0.mmse1 <=num2).filter(Visit0.mmse3 > 0).all()
    elif visit_num == '1':
        visit = Visit1.query.filter(Visit1.mmse1 >= num1).filter(Visit1.mmse1 <=num2).filter(Visit1.mmse3 > 0).all()
    elif visit_num == '2':
        visit = Visit2.query.filter(Visit2.mmse1 >= num1).filter(Visit2.mmse1 <=num2).filter(Visit2.mmse3 > 0).all()
    elif visit_num == '3':
        visit = Visit3.query.filter(Visit3.mmse1 >= num1).filter(Visit3.mmse1 <=num2).filter(Visit3.mmse3 > 0).all()
    elif visit_num == '4':
        visit = Visit4.query.filter(Visit4.mmse1 >= num1).filter(Visit4.mmse1 <=num2).filter(Visit4.mmse3 > 0).all()
    else:
        visit_num=0
        visit = Visit0.query.filter(Visit0.mmse1 >= num1).filter(Visit0.mmse1 <= num2).filter(Visit0.mmse3 > 0).all()
    visit_num = int(visit_num)+1
    return render_template('visit_data.html', visit = visit, visit_num=visit_num, num1=num1, num2=num2)

@app.route('/participants')
def participants():
    visit = Visit0.query.filter(Visit0.mmse1 >= num1).filter(Visit0.mmse1 <=num2).filter(Visit0.mmse3 >0).all()
    return render_template('participants.html', visit = visit, num1=num1, num2=num2)

@app.route('/placeholder')
def placeholder():
    return render_template('placeholder.html', num1=num1, num2=num2)

@app.route('/about')
def about():
    return render_template('about.html', num1=num1, num2=num2)

@app.route('/cookie_theft')
def cookie_theft():
    return render_template('cookie_theft.html', num1=num1, num2=num2)

@app.route('/graphs')
def graphs():
    return render_template('graphs.html', num1=num1, num2=num2)

@app.route('/transcripts')
def transcripts():
    with current_app.open_resource("static/output.txt", "r") as f:
        content = f.read()
    return render_template("transcripts.html", content=content, num1=num1, num2=num2)


# @app.route('/list_dev/<borough>')
# def list_dev(borough):
#     borough_id=0
#     if int(borough) == 0:
#         dev = Development.query.all()
#         borough_name = "ALL BOROUGHS"
#     else:
#         dev = Development.query.filter_by(borough_id=int(borough)).all()
#         print(dev[0].borough.name)
#         borough_name = dev[0].borough.name
#         borough_id = dev[0].borough_id
#     return render_template('dev.html', dev=dev, borough_name=borough_name, borough_id=borough_id)
#
# @app.route('/charges/<bldg_id>')
# def charges(bldg_id):
#     try:
#         bills = Bill.query.filter_by(building_id=int(bldg_id)).all()
#         borough_name = bills[0].building.dev.borough.name
#         borough_id = bills[0].building.dev.borough_id
#         dev_id = bills[0].building.dev.dev_id
#         dev_name = bills[0].building.dev.name
#         bldg_name = bills[0].building.location
#     except Exception as e:
#         building = Building.query.filter_by(building_id=int(bldg_id)).first()
#         borough_name = building.dev.borough.name
#         borough_id = building.dev.borough_id
#         dev_id = building.dev.dev_id
#         dev_name = building.dev.name
#         bldg_name = building.location
#         output = f"Development: {dev_name} Building: {bldg_name} Building ID: {bldg_id} had no charges from 2018-2020. <br> Due to space constraints of 10K records on Heroku server for free accounts, I eliminated charges prior to 2018 from the database."
#         return output + "<p>Error for debugging purposes only: " + str(e)
#
#     return render_template('charges.html', bills=bills, borough_name=borough_name, dev_name=dev_name, bldg_name=bldg_name, borough_id=borough_id, dev_id=dev_id)