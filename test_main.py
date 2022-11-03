from main import app
import json


def test_status_ok():
    response = app.test_client().get('/status')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['result'] == 'success'
   
    