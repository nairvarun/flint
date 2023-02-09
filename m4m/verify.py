from pymongo import MongoClient
import datetime
import rsa


def main():
    # get keys
    with open("./pub.pem", "rb") as f:
        pub_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("./priv.pem", "rb") as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read())

    # establish conection
    client = MongoClient()
    db = client['flint-dummy']
    collection = db['m4m']

    # get dummy data and verify
    for d in collection.find():
        try:
            msg = str({k:v for k, v in d.items() if k not in {"sig", "_id"} }).encode()
            # msg = "a".encode()
            rsa.verify(msg, d["sig"], pub_key)
            print("ok")
        except rsa.VerificationError:
            print(f"{d['_id']} has been tampered")



if __name__ == "__main__":
    main()
