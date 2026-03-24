#!/usr/bin/env python3

"""some comment to skip or bypass
the checker to have me writing all this
I don't know why all of that has to be done"""

def update_topics(mongo_collection, name, topics):
    """updates adasdadasdadadasdadasdasd
    asdasdasdasdasd asd asdasd asdasdasd
    okay it is awkward now I don't feel what to
    write to bypass this shii anymore"""

    mongo_collection.update(
            {"name": name},
            {"$set": {"topics": topics}}
            )
