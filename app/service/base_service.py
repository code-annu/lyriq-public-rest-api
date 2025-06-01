from typing import TypeVar, Generic

from bson import ObjectId
from pymongo.collection import Collection

from app.core.exceptions import NotFoundException

T = TypeVar('T')


class BaseService(Generic[T]):
    def __init__(self, collection: Collection, model: type[T]):
        self.collection = collection
        self.model = model

    def read(self, id: str) -> T:
        document = self.collection.find_one({'_id': ObjectId(id)})
        if document:
            document = dict(document)
            document['id'] = id
            return self.model(**document)
        raise NotFoundException()

    def read_many(self, ids: list[str]) -> list[T]:
        object_ids = [ObjectId(id) for id in ids]
        documents = self.collection.find({'_id': {'$in': object_ids}})
        return [self.model(**{**doc, 'id': str(doc['_id'])}) for doc in documents]

    def shuffled_data(self, size: int) -> list[T]:
        # Using the $sample aggregation stage to get a random sample of artists
        pipeline = [
            {"$sample": {"size": size}}  # Randomly sample 'size' documents
        ]
        documents = self.collection.aggregate(pipeline, allowDiskUse=True)
        return [self.model(**{**doc, "id": str(doc["_id"])}) for doc in documents]

    def search_data(self, index_name: str, path_name: str, query: str) -> list[T]:
        pipeline = [
            {
                "$search": {
                    "index": index_name,  # Replace it with your index name
                    "autocomplete": {
                        "query": query,
                        "path": path_name,
                        "fuzzy": {
                            "maxEdits": 1,
                            "prefixLength": 1
                        }
                    },
                }
            },
        ]
        cursor = self.collection.aggregate(pipeline)
        data_list = [self.model(**doc, id=str(doc["_id"])) for doc in cursor]
        return data_list
