from main import app
import json
import flask

def test_status_ok():
    response = app.test_client().get('/status')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['result'] == 'success'
   
    
    
# def test_ip(requests_mock, mocker):
#     ip = '145.201.25.35'
#     city='Douala'
#     state = 'Littoral'
#     request_mock = mocker.patch.object(flask, "request")
#     request_mock.remote_addr.get.return_value = ip
#     requests_mock.get(f'https://ipapi.co/{ip}/json/', json={'ip' : ip,
#                                                             'city' : city,
#                                                             'region': state})
    
#     response = app.test_client().get('/ip')
#     assert response.status_code == 200
#     data = json.loads(response.data.decode('utf-8'))
#     assert data['ip'] == ip
#     assert data['city'] == city
#     assert data['state'] == state
    
    