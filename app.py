import sys
import logging
from flask_bootstrap import Bootstrap
from flask import Flask, url_for, render_template, redirect, request
from nyrr import get_runner_info, get_all_runner_races
import pandas as pd


app = Flask(__name__)
Bootstrap(app)

def setup_logger(logger, output_file):
    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter('%(asctime)s [%(funcName)s]: %(message)s'))
    logger.addHandler(stdout_handler)

    file_handler = logging.FileHandler(output_file)
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(funcName)s] %(message)s'))
    logger.addHandler(file_handler)


logger = logging.Logger(__name__)
setup_logger(logger, 'debug_output.log')


# @app.route("/")
# def show_runner_data(nyrr_id='38295218'):
#     runner_details = get_runner_info(nyrr_id)['details']
#     runner_events = get_all_runner_races(nyrr_id)
#     return render_template(
#         'view-races.html',
#         runnerDetails=runner_details,
#         runnerEvents=runner_events,
#     )
    

@app.route("/")
def show_runner_data(nyrr_id='38295218'):
    #nyrr_id='38670786' jeff
    runner_details = get_runner_info('38670786')['details']
    runner_events = pd.read_csv("./data/jeff_races.csv")
    #runner_events = get_all_runner_races(nyrr_id)
    return render_template(
        'view-races.html',
        runnerDetails=runner_details,
        runnerEvents=(runner_events.values),
    )
    


# @app.route("/runner/<nyrr_id>")
# def show_runner_data(nyrr_id='38295218'):
#     runner_details = get_runner_info(nyrr_id)
#     runner_events = get_runner_races(nyrr_id)
#     return render_template(
#         'view-races.html',
#         runnerDetails=runner_details,
#         runnerEvents=runner_events,
#     )


if __name__ == "__main__":
    app.run(debug=True)