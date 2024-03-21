import random

import bson
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from collections import defaultdict

from common import util


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

score_delta_cache = defaultdict(int)


@app.get('/scores/{pilot_id}', status_code=200)
def pilot_score(pilot_id, response: Response):
    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    database = util.get_mongo_database()
    pilot = database['pilots'].find_one({'_id': pilot_id})

    if pilot is None:
        response.status_code = 404
        return "Not Found"

    delta_score = random.randint(0, 5)
    score_delta_cache[pilot_id] += delta_score

    return pilot['score'] + score_delta_cache[pilot_id]
