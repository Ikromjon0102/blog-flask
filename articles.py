from slugify import slugify
import os
import json

class Article:
    ARTICLE_DIR = "articles"
    
    def __init__(self, title):
        self.title = title
        self.content = ""
        self.file_path = os.path.join(self.ARTICLE_DIR, f"{title}")
    
    @property
    def slug(self):
        return slugify(self.title)
    
    def save_content(self, content):
        self.content = content
        with open(self.file_path, "w") as file:
            file.write(f"{self.title}\n{self.content}")
        return self.load_content()
    
    def load_content(self):
        with open(f"articles/{self.title}") as file:
            self.content = file.read()
    
    @classmethod
    def all(cls):
        titles = os.listdir("articles")
        slug_articles = {}
        for title in titles:
            slug = slugify(title)
            article = Article(title)
            article.load_content()
            slug_articles[slug] = article
        
        return slug_articles

# # ======== chatgpt ning autoload bo'yicha yechimi ========
# # ======== chatgpt ning autoload bo'yicha yechimi ========

# from slugify import slugify
# import os
# import json

# class Article:
#     ARTICLE_DIR = "articles"

#     def __init__(self, title):
#         self.title = title
#         self.content = ""
#         self.file_path = os.path.join(self.ARTICLE_DIR, f"{slugify(title)}.json")

#     @property
#     def slug(self):
#         return slugify(self.title)

#     def load_content(self):
#         if os.path.exists(self.file_path):
#             with open(self.file_path, "r") as file:
#                 data = json.load(file)
#                 self.content = data.get("content", "")

#     def save_content(self, content):
#         self.content = content
#         data = {"content": content}
#         with open(self.file_path, "w") as file:
#             json.dump(data, file)

#     @classmethod
#     def all(cls):
#         if not os.path.exists(cls.ARTICLE_DIR):
#             os.makedirs(cls.ARTICLE_DIR)

#         articles = {}
#         for file_name in os.listdir(cls.ARTICLE_DIR):
#             file_path = os.path.join(cls.ARTICLE_DIR, file_name)
#             if os.path.isfile(file_path) and file_name.endswith(".json"):
#                 with open(file_path, "r") as file:
#                     data = json.load(file)
#                     title = data.get("title", "")
#                     article = Article(title)
#                     article.load_content()
#                     articles[article.slug] = article

#         return articles
