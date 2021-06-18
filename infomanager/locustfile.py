import time
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def test_info(self):
        self.client.get("api/info")
        time.sleep(1)
