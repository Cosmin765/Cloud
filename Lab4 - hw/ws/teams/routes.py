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


@app.get('/teams', status_code=200)
def teams_collection_get():
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['teams'].find())]


@app.get('/teams/{team_id}', status_code=200)
def teams_item_get(team_id, response: Response):
    try:
        team_id = bson.ObjectId(team_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    database = util.get_mongo_database()
    team = database['teams'].find_one({'_id': team_id})

    if team is None:
        response.status_code = 404
        return "Not Found"

    return util.serialize_item(team)


@app.post('/teams', status_code=201)
def teams_collection_post(team: Team):
    team = team.dict()
    util.get_mongo_database()['teams'].insert_one(team)
    return util.serialize_item(team)


@app.put('/teams/{team_id}', status_code=200)
def teams_item_put(team_id, team: Team, response: Response):
    database = util.get_mongo_database()

    try:
        team_id = bson.ObjectId(team_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    if database['teams'].find_one({'_id': team_id}) is None:
        response.status_code = 404
        return 'Not Found'

    database['teams'].replace_one({'_id': team_id}, team.dict())
    return 'success'


@app.delete('/teams/{team_id}', status_code=200)
def teams_item_delete(team_id, response: Response):
    database = util.get_mongo_database()

    try:
        team_id = bson.ObjectId(team_id)
    except (TypeError, bson.errors.InvalidId):
        response.status_code = 400
        return 'bad id format'

    if database['teams'].find_one({'_id': team_id}) is None:
        response.status_code = 404
        return 'Not Found'

    database['teams'].delete_one({'_id': team_id})
    return 'success'
