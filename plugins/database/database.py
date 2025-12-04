#Coded by the @legend580 💛❤️

import datetime, pymongo
#import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self, uri, database_name):
        self._client = pymongo.MongoClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.pla = self.db.place

    # Team things
    def add_place(self):
        return dict(
            id='cs01',
            hints={'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0],'a':['xy',0]}
        )

    # Users things
    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            auth_user=False
        )
        
    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        self.pla.insert_one(self.add_place())
        user = self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})
        
    async def full_userbase(self):
        user_docs = self.col.find()
        user_ids = []
        for doc in user_docs:
            user_ids.append(doc['id'])
        return user_ids

    async def delete_user(self, user_id):
        self.col.delete_many({'id': int(user_id)})

    async def set_auth_user(self, id, add_user):
        self.col.update_one({'id': id}, {'$set': {'auth_user': add_user}})

    async def get_auth_user(self, id):
        user = self.col.find_one({'id': int(id)})
        return user.get('auth_user', True)

    async def set_upload_as_doc(self, id, upload_as_doc):
        self.col.update_one({'id': id}, {'$set': {'upload_as_doc': upload_as_doc}})

    async def get_upload_as_doc(self, id):
        user = self.col.find_one({'id': int(id)})
        return user.get('upload_as_doc', False)

    async def set_thumbnail(self, id, thumbnail):
        self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)

    async def get_user_data(self, id) -> dict:
        user = self.col.find_one({'id': int(id)})
        return user or None

db = Database(Config.DATABASE_URL, Config.DATABASE_NAME)
