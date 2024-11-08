from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000/"  # 여기에 실제 테스트할 웹 애플리케이션의 호스트 URL

    def on_start(self):
        print('test start')

    @task
    def my_data(self):
        self.client.get("test/my_data/")

    @task
    def my_data_has_null(self):
        self.client.get("test/my_data_has_null/")

    @task
    def mean_age(self):
        self.client.get("test/mean_age/")

    @task
    def normal_sort(self):
        self.client.get("test/normal_sort/")

    @task
    def priority_queue(self):
        self.client.get("test/priority_queue/")

    @task
    def bubble_sort(self):
        self.client.get("test/bubble_sort/")