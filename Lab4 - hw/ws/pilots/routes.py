import bson
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from common import util
from common.models import *


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/pilots', status_code=200)
def pilots_collection_get():
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['pilots'].find())]


@app.get('/pilots/{pilot_id}', status_code=200)
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

    return util.serialize_item(pilot)


@app.post('/pilots', status_code=201)
def pilots_collection_post(pilot: Pilot):
    pilot = pilot.dict()
    util.get_mongo_database()['pilots'].insert_one(pilot)
    return util.serialize_item(pilot)


@app.put('/pilots/{pilot_id}', status_code=200)
def pilots_item_put(pilot_id, pilot: Pilot, response: Response):
    database = util.get_mongo_database()

    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    if database['pilots'].find_one({'_id': pilot_id}) is None:
        response.status_code = 404
        return 'Not Found'

    database['pilots'].replace_one({'_id': pilot_id}, pilot.dict())
    return 'success'


@app.delete('/pilots/{pilot_id}', status_code=200)
def pilots_item_delete(pilot_id, response: Response):
    database = util.get_mongo_database()

    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    if database['pilots'].find_one({'_id': pilot_id}) is None:
        response.status_code = 404
        return 'Not Found'

    database['pilots'].delete_one({'_id': pilot_id})
    return 'success'
