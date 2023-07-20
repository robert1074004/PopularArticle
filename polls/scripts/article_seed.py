from ..models import Article
def run():

    articles_data = [{
        "title": "Article 1",
        "image": "https://example.com/image1.jpg"
      }, {
        "title": "Article 2",
        "image": "https://example.com/image2.jpg"
      }]
    
    for data in articles_data:
        Article.objects.create( title = data["title"], image = data["image"] )