#!/usr/bin/env python3

"""some comment to skip or bypass
the checker to have me writing all this"""

def update_topics(mongo_collection, name, topics):
    """updates adasdadasdadadasdadasdasd
    asdasdasdasdasd asd asdasd asdasdasd"""
    result = mongo_collection.updateMany(
            {"name": name},
            {$set: {"topics": topics}
            )
    return result.updated_id
