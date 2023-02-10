from pymerkle import  MerkleTree
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel

# data model
class LogData(BaseModel):
    log_contents: str

app = FastAPI()

# routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/log", status_code=status.HTTP_201_CREATED)
async def log(data: LogData):
    # establish conection
    client = MongoClient()
    db = client['flint-dummy']
    collection = db['m4u']

    # upload data
    collection.insert_one(dict(data))

@app.get("/challenge")
async def challenge(data: str):
    # merkle tree
    tree = MerkleTree()

    # establish conection
    client = MongoClient()
    db = client['flint-dummy']
    collection = db['m4u']

    # populate tree
    for d in collection.find():
        tree.encrypt(str({k:v for k, v in d.items() if k not in {"_id"}}))

    # Prove and verify encryption of `bar`
    challenge = tree.get_digest(data)
    proof = tree.generate_audit_proof(challenge)
    try:
        proof.verify()
        return "ok"
    except Exception as e:
        print(e)
        return f"{data} has been tampered"

@app.get("/state")
async def get_state():
    # merkle tree
    tree = MerkleTree()

    # establish conection
    client = MongoClient()
    db = client['flint-dummy']
    collection = db['m4u']

    # populate tree
    for d in collection.find():
        tree.encrypt(str({k:v for k, v in d.items() if k not in {"_id"}}))

    return tree.get_root_hash()

# @app.get("/proove")
# async def proove(state: str):
#     # merkle tree
#     tree = MerkleTree()

#     # establish conection
#     client = MongoClient()
#     db = client['flint-dummy']
#     collection = db['m4u']

#     # populate tree
#     for d in collection.find():
#         tree.encrypt(str({k:v for k, v in d.items() if k not in {"_id"}}))

#     proof = tree.generate_consistency_proof(challenge=state.encode())
#     try:
#         proof.verify()
#         return True
#     except Exception as e:
#         print(e)
#         return False
