from pymerkle import MerkleTree


def main():
    tree = MerkleTree()

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

    # Populate tree with some records
    for data in dummy_data:
        tree.encrypt(str(data))

    # Prove and verify encryption of `bar`
    challenge = tree.get_digest(str(dummy_data[0]))
    proof = tree.generate_audit_proof(challenge)
    proof.verify()

    # Save current tree state
    state = tree.get_root_hash()

    # Append further leaves
    # todo: try with dict
    for data in [b'corge', b'grault', b'garlpy']:
        tree.encrypt(data)

    # Prove and verify saved state
    proof = tree.generate_consistency_proof(challenge=state)
    print(proof.verify())


if __name__ == "__main__":
    main()
