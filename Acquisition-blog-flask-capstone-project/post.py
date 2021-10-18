import requests

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/2485c0a195448540d580"

    def get_posts(self):
        response = requests.get(self.url)
        return response.json()

    def get_post_via_id(self, id):
        self.posts = self.get_posts()
        for post in self.posts:
            if post['id'] == id:
                return post
