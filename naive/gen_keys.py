import rsa


def main():
    pub, priv = rsa.newkeys(1024)

    with open("pub.pem", "wb") as f:
        f.write(pub.save_pkcs1("PEM"))

    with open("priv.pem", "wb") as f:
        f.write(priv.save_pkcs1("PEM"))


if __name__ == "__main__":
    main()
