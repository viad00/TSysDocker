from django.test import TestCase

# Tests here.


class ViewTest(TestCase):
    """Test Views"""

    def test_home(self):
        """Test home page"""
        response = self.client.get('/')
        self.assertContains(response, 'TestSys', 2, 200)
