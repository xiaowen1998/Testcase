from locust import HttpLocust, TaskSet, task
import time
from locust import HttpUser, task, between
from szgd_src.common.headers import headers
from szgd_src.common.url import url1, url2, url3, url4
import os


# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.get(url1 + "jobinfo/pageList", headers=headers, verify=False)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


if __name__ == "__main__":
    os.system('locust -f UI_test.py --web-host=localhost')