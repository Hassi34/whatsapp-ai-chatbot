# import httplib2
# def test_api():
#     http = httplib2.Http(timeout=2313)
#     resp, content = http.request(
#         uri="http://127.0.0.1:80/chatgpt_webhook",
#         method='POST',
#         headers={'Content-Type': 'application/json; charset=UTF-8'},
#         body="Hi",
#     )
#     text_content = content.decode("utf-8")
#     assert resp.status == 200
#     print(">>>>>>>>>>>>>>>>>>>>>> Response 200 test passed <<<<<<<<<<<<<<<<<<<<<")
#     assert type(text_content) == str
#     print(">>>>>>>>>>>>>>>>>>>>>> Data type test passed <<<<<<<<<<<<<<<<<<<<< ")

from requests.adapters import HTTPAdapter, Retry
import requests


def test_api():
    
    s = requests.Session()

    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('http://', HTTPAdapter(max_retries=retries))
    response = s.post("http://127.0.0.1:80/chatgpt_webhook",
                        data="Hi")
    text_response = response.content.decode("utf-8")
    assert response.status_code == 200 
    assert type(text_response) == str

# if __name__ == '__main__':
#     test_api()