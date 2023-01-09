import unittest, pytest
from datetime import datetime
from podcasts import get_timestamp, read_all, create, search, update, delete


class TestPodcastAPI(unittest.TestCase):
    PODCASTS_MOCK = []
    
    def setup_data(self): 
      return {
        "The Daily": {
            "title": "The Daily",
            "publisher": "The New York Times",
            "genre": "News",
            "release_date": "2017-02-06"
        },
        "The Joe Rogan Experience": {
            "title": "The Joe Rogan Experience",
            "publisher": "Joe Rogan",
            "genre": "Comedy",
            "release_date": "2009-12-24"
        },
        "Radiolab": {
            "title": "Radiolab",
            "publisher": "WNYC Studios",
            "genre": "Science",
            "release_date": "2002-05-14"
        }

    }

    @pytest.fixture(autouse=True)
    def before_and_after_test(self):
        PODCASTS = self.setup_data()
        yield



    # def test_get_timestamp(self):
    #     # Test that the get_timestamp function returns a string in the correct format
    #     timestamp = get_timestamp()
    #     self.assertIsInstance(timestamp, str)
    #     self.assertRegex(timestamp, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    #     # Test that the get_timestamp function returns the current timestamp
    #     now = datetime.now()
    #     timestamp = get_timestamp()
    #     self.assertEqual(timestamp, now.strftime("%Y-%m-%d %H:%M:%S"))

    def test_create(self):
        create({
            "title": "title1",
            "publisher": "publisher1",
            "genre": "genre",
            "release_date": "2017-02-06"
        })
        posts = read_all()
        print(f"🤖 posts: {posts[len(posts) - 1]}")
        self.assertEqual(posts[len(posts) - 1]["title"], "title1")

    def test_read_all(self):
        self.PODCASTS_MOCK = self.setup_data()
        posts = read_all()
        print(f"🤖 posts: {posts}")
        self.assertEqual(posts[0]["title"], "The Daily")

    def test_search(self):
        post = search("The Daily")
        self.assertEqual(post[0][0]["publisher"], "The New York Times")

    def test_delete(self):
        delete("The Daily")
        post = search("The Daily")
        print(f"🤖 post: {post}")
        self.assertEqual(post, (None, 404))

    # def test_update(self):
    #   update("The Daily", {
    #     "title": "The Daily",
    #     "publisher": "The New York Times 2",
    #     "genre": "News",
    #     "release_date": "2017-02-06"
    #   })
    #   post = search("The Daily")
    #   print(post)
    #   self.assertEqual(post[0][0]["publisher"], "The New York Times 2")


if __name__ == '__main__':
    unittest.main()
