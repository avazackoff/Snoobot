import flask
from flask import request, jsonify
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread import Cell
from datetime import datetime
from SnooClient import Client
import AppConfig as cfg
import pytz

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return f'Snoo bot is up and running at {current_timestamp}'

@app.route("/getSnooStatus",  methods = ['GET'])
def status():
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(cfg.googleCredentials, scope)
    googleClient = gspread.authorize(creds)
    googleFile = googleClient.open("Extracted Snoo Data").worksheet("Zapier")
    currentSheetValues = googleFile.get_all_values()
    gSheetLength = len(currentSheetValues)
    maxRowCount = currentSheetValues[gSheetLength - 1][0]

    client = Client("mzackoff@servicetitan.com", "Iloveaz1!", None)
    snooCurrentStatus = client.status()
    currentTimestamp = datetime.now(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S')

    cells = []
    cells.append(Cell(row=gSheetLength + 1, col=1, value=gSheetLength))
    cells.append(Cell(row=gSheetLength + 1, col=2, value=snooCurrentStatus))
    cells.append(Cell(row=gSheetLength + 1, col=3, value=currentTimestamp))
    googleFile.update_cells(cells)
    return f'added data to gsheet at {current_timestamp}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)