import json


class PostsHandeler:
    def __init__(self, path):
        self.path = path

    def load_posts_from_json(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_post(self, substr):
        posts = []

        for post in self.load_posts_from_json():
            if substr.lower() in post['content'].lower():
                posts.append(post)

        return posts

    def save_posts_to_gson(self, posts):
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file)
        except Exception as e:
            return e

    def add_post(self, post):
        posts = self.load_posts_from_json()
        posts.append(post)
        return self.save_posts_to_gson(posts)
