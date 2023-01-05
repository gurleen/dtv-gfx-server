from typing import Dict, List
from aiotinydb import AIOTinyDB


async def insert_into_db(db_name: str, object: Dict):
    async with AIOTinyDB(db_name) as db:
        db.insert(object)


async def get_all_from_db(db_name: str) -> List[Dict]:
    async with AIOTinyDB(db_name) as db:
        rows = db.all()
        for row in rows:
            row["id"] = row.doc_id
        return rows


async def delete_row_with_id(db_name: str, id: int):
    async with AIOTinyDB(db_name) as db:
        db.remove(doc_ids=[id])
