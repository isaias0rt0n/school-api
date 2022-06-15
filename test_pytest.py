import requests


class TestCourses:
    # Just for TokenAuthentication - Change in settings project
    # https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    headers = {'Authorization': 'Token 51caba258784f54c952f193d8df916b71d3b911c'}
    baseURL = 'http://localhost:8000/api/courses/'

    def test_get_courses(self):
        response = requests.get(url=self.baseURL, headers=self.headers)

        assert response.status_code == 200

    def test_get_course(self):
        response = requests.get(url=f'{self.baseURL}4')

        assert response.status_code == 200

    def test_post_course(self):
        data = {
            "title": "Curso teste22",
            "url": "http://cursoteste22.com"
        }
        response = requests.post(url=self.baseURL, headers=self.headers, data=data)

        assert response.status_code == 201
        assert response.json()['title'] == data['title']

    def test_put_course(self):
        data = {
            "title": "test updated course",
            "url": "testupdated.com.br"
        }
        response = requests.put(url=self.baseURL, headers=self.headers, data=data)

        assert response.status_code == 200
        assert response.json()['title'] == data['title']

    def test_delete_course(self):
        response = requests.delete(url=self.baseURL, headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0
