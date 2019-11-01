from django.test import TestCase
from django.test import TestCase
# Create your tests here.
class YourTestCase(TestCase):
    def test_import_keys_posting(self):
        data = request.FILES['source']
        ## send the file to /process
        url = 'http://127.0.0.1:8000/'
        result = requests.get(url,files = {'source':data},)
        response = self.client.post(reverse('import_keys'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'result': 'ok'})

 