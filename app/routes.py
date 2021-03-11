from flask import render_template, request, Response
from app import app
from app.models import Borough

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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