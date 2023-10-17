#from .test_web_api import backend_rest_client, backend_server

async def test_track_getregistration(backend_rest_client):
    response = await backend_rest_client.get('/registration')
    assert(response.status == 200)
    #settings = await response.json()


async def test_track_badges(backend_rest_client, backend_server):
    response = await backend_rest_client.put('/registration/badge/99999/name',json='fred')
    assert(response.status == 200)

    response = await backend_rest_client.put('/registration/badge/99998/name',json='joe')
    assert(response.status == 200)

    response = await backend_rest_client.put('/registration/lane/1/badge_id',json='99999')
    assert(response.status == 200)
    assert(backend_server.track.lanes[1].name == "fred")

    response = await backend_rest_client.put('/registration/lane/1/badge_id',json='99998')
    assert(response.status == 200)
    assert(backend_server.track.lanes[1].name == "joe")
    