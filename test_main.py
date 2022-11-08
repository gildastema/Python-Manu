from main import app
import json

def test_status_ok():
    """_summary_
    Test Status 
    """
    response = app.test_client().get('/status') # Call end Point
    assert response.status_code == 200  # Verify if response is Ok 
    data = json.loads(response.data.decode('utf-8')) ## Get The result decode json content
    assert data['result'] == 'success' ## verify is {'result': 'success'}
   
    