import time
from locust import HttpUser, task, between
from xiaowen_Python_work.common.headers import headers
from xiaowen_Python_work.common.url import url
import os


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        # print('12121')
        self.client.get(url + "v1/get_profile", headers=headers)
        self.client.get(url + "product_packages", headers=headers)
        self.client.get(url + "interact_remind", headers=headers)
    """
    在此view_items任务中，我们使用变量查询参数加载10个不同的URL。为了不在Locust的统计信息中获得10个单独的条目
    （由于统计信息在URL上分组），我们使用name参数将所有这些请求分组在一个名为的条目下"/item"。
    此外，我们还声明了on_start方法。每个模拟用户在启动时都会调用具有该名称的方法。有关更多信息，请参见on_start和on_stop方法。
    """
    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)
    def on_start(self):
        self.client.post(url + "login", json={
            'username': '1766353759@qq.com',
            'password': '123456789',
            'device_type': 'android',
            'client_id': '9',
            'client_secret': 'ruua6V1baBNfsc7Uld5gDTDlcytsZu2WyDbSKnOo',
            'grant_type': 'password'}, headers=headers)
        self.client.post(url + "getUserBalanceLogs", json=None, headers=headers)
        self.client.post(url + "find_match", json=None, headers=headers)


if __name__ == "__main__":
    os.system('locust -f locust_test.py --web-host=localhost')