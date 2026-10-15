import unittest

from app import app


class TimeServiceTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DevOps Time Service", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_time_api_returns_utc_timestamp(self):
        response = self.client.get("/api/time")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["timezone"], "UTC")
        self.assertIn("timestamp", data)
        self.assertTrue(data["timestamp"].endswith("+00:00"))


if __name__ == "__main__":
    unittest.main()
