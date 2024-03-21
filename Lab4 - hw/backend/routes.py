import time

import requests
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware


PILOTS_WS = 'http://127.0.0.1:8004'
SCORE_WS = 'http://127.0.0.1:8002'
TEAMS_WS = 'http://127.0.0.1:8003'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/pilots', status_code=200)
def pilots_collection_get(response: Response):
    res = requests.get(f'{PILOTS_WS}/pilots')
    try:
        res.raise_for_status()
    except:
        response.status_code = res.status_code
        return res.text

    pilots = res.json()

    for pilot in pilots:
        team_id = pilot['extra_info']['team_id']
        res = requests.get(f'{TEAMS_WS}/teams/{team_id}')
        try:
            res.raise_for_status()
        except:
            response.status_code = res.status_code
            return res.text

        team = res.json()
        del pilot['extra_info']['team_id']
        pilot['extra_info']['team'] = team['name']

    return pilots


@app.get('/scores/{pilot_id}', status_code=200)
def score(pilot_id, response: Response):
    res = requests.get(f'{SCORE_WS}/scores/{pilot_id}')
    try:
        res.raise_for_status()
    except:
        response.status_code = res.status_code
        return 'error'

    return res.json()
