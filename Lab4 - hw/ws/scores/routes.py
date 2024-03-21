import random

import bson
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from common import util


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/scores/{pilot_id}', status_code=200)
def pilots_item_get(pilot_id, response: Response):
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

    final_score = pilot['score'] + random.randint(-10, 10)

    return 0 if final_score < 0 else final_score
