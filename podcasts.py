from datetime import datetime
import re
from os import abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PODCASTS = [
    {
        "title": "The Daily",
        "publisher": "The New York Times",
        "genre": "News",
        "release_date": "2017-02-06"
    },
    {
        "title": "The Joe Rogan Experience",
        "publisher": "Joe Rogan",
        "genre": "Comedy",
        "release_date": "2009-12-24"
    },
    {
        "title": "Radiolab",
        "publisher": "WNYC Studios",
        "genre": "Science",
        "release_date": "2002-05-14"
    }
]


def read_all():
    return list(PODCASTS)


def create(podcast):
    title = podcast.get("title")
    publisher = podcast.get("publisher")
    genre = podcast.get("genre")
    release_date = podcast.get("release_date")

    post = list(filter(lambda x: x["title"] == title, PODCASTS))
    if not post:
        PODCASTS.append({
            "title": title,
            "publisher": publisher,
            "genre": genre,
            "release_date": release_date
        })
        return PODCASTS[-1], 201
    else:
        print(406, f"Podcast with title {title} already exists")


def search(title):
    pattern = re.compile(title, re.IGNORECASE)
    post = list(filter(lambda x: pattern.search(x["title"]), PODCASTS))
    
    print("🤖 post: ", post)
    if post:
        print("🤖 there is a post: ", post)
        return post, 200
    else:
        return None, 404
    print(404, f"Podcast with title {title} not found")


def update(title, podcast):
    post = search(title)
    if post is not None:
        delete(title)
        create(podcast)
        return podcast
    else:
        print(
            404,
            f"Podcast with title {title} not found"
        )


def delete(title):
    if (search(title)[0] is not None):
        for podcast in PODCASTS:
            if podcast["title"] == title:
                PODCASTS.remove(podcast)
                
        return title, 204
    else:
        print(
            404,
            f"Podcast with title {title} not found"
        )
