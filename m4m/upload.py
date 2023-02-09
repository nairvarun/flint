from pymongo import MongoClient
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

    # create dummy data
    dummy_data = [
        {
            "log_contents": "Iguanas were falling out of the trees.",
        },
        {
            "log_contents": "Pandas were falling out of the trees.",
        },
        {
            "log_contents": "Dolphins were falling out of the trees.",
        },
        {
            "log_contents": "Sloths were falling out of the trees.",
        },
        {
            "log_contents": "Otters were falling out of the trees.",
        }
    ]

    # sign dummy data
    for d in dummy_data:
        d["sig"] = rsa.sign(str(d).encode(), priv_key, "SHA-256")

    # upload dummy data
    # collection.insert_many(dummy_data)


if __name__ == "__main__":
    main()
