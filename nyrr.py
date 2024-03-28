import requests
import pandas as pd


def get_runner_info(runner_id='38295218'):
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Language': 'en-US,en;q=0.9', 
        'Sec-Fetch-Mode': 'cors',
        'Host': 'rmsprodapi.nyrr.org',
        'Origin': 'https://results.nyrr.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
        'Referer': 'https://results.nyrr.org/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
    }
    json_data = {
        'runnerId': runner_id,
    }
    response = requests.post('https://rmsprodapi.nyrr.org/api/v2/runners/recentDetails', headers=headers, json=json_data)
    return response.json()


def get_runner_races(runner_id='38295218', page_index=1, count=False):
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Mode': 'cors',
        'Host': 'rmsprodapi.nyrr.org',
        'Origin': 'https://results.nyrr.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
        'Referer': 'https://results.nyrr.org/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
    }
    json_data = {
        'runnerId': runner_id,
        'searchString': None,
        'year': None,
        'distance': None,
        'teamCode': None,
        'overallPlaceFrom': None,
        'overallPlaceTo': None,
        'paceFrom': None,
        'paceTo': None,
        'overallTimeFrom': None,
        'overallTimeTo': None,
        'gunTimeFrom': None,
        'gunTimeTo': None,
        'ageGradedTimeFrom': None,
        'ageGradedTimeTo': None,
        'ageGradedPlaceFrom': None,
        'ageGradedPlaceTo': None,
        'ageGradedPerformanceFrom': None,
        'ageGradedPerformanceTo': None,
        'pageIndex': page_index,
        'pageSize': 51,
        'sortColumn': 'EventDate',
        'sortDescending': True,
    }
    response = requests.post('https://rmsprodapi.nyrr.org/api/v2/runners/races', headers=headers, json=json_data)
    if count:
        return response.json()['totalItems']
    return pd.DataFrame.from_dict(response.json()['items'])

def get_all_runner_races(nyrr_id):
    runner_race_count = get_runner_races(nyrr_id, count=True)
    num_result_pages = runner_race_count // 51 + 1
    all_races = []
    for page_num in range(1, num_result_pages + 1):
        runner_results = get_runner_races(nyrr_id, page_index=page_num)
        all_races.append(runner_results)
    all_races = pd.concat(all_races).reset_index()
    return all_races