import hashlib
import json

def get_leaf_hashes(dictionaries):
    return [hashlib.sha256(json.dumps(d).encode()).hexdigest() for d in dictionaries]

def build_merkle_tree(leaf_hashes):
    if len(leaf_hashes) == 1:
        return leaf_hashes
    else:
        parent_hashes = []
        for i in range(0, len(leaf_hashes) - 1, 2):
            parent = hashlib.sha256(
                (leaf_hashes[i] + leaf_hashes[i + 1]).encode()
            ).hexdigest()
            parent_hashes.append(parent)
        if len(leaf_hashes) % 2 == 1:
            parent_hashes.append(leaf_hashes[-1])
        return build_merkle_tree(parent_hashes)

# def generate_proof_of_inclusion(dictionary, dictionaries, leaf_hashes, merkle_tree):
#     index = dictionaries.index(dictionary)
#     proof = []
#     for i, parent_hash in enumerate(merkle_tree[index + len(dictionaries):]):
#         if i % 2 == 0:
#             proof.append(leaf_hashes[index + 1])
#         else:
#             proof.append(leaf_hashes[index - 1])
#     return proof
def generate_proof(leaf_hash, leaf_hashes, parent_hashes):
    proof = []
    index = leaf_hashes.index(leaf_hash)
    for parent in parent_hashes:
        if index % 2 == 0:
            sibling = leaf_hashes[index + 1] if index + 1 < len(leaf_hashes) else None
        else:
            sibling = leaf_hashes[index - 1]
            index -= 1
        if sibling:
            proof.append({"right": sibling} if index % 2 == 0 else {"left": sibling})
        index = index // 2
    return proof




# def verify_proof_of_inclusion(dictionary, proof, root):
#     hash = hashlib.sha256(json.dumps(dictionary).encode()).hexdigest()
#     is_left_child = True
#     for p in proof:
#         if is_left_child:
#             hash = hashlib.sha256((hash + p).encode()).hexdigest()
#         else:
#             hash = hashlib.sha256((p + hash).encode()).hexdigest()
#         is_left_child = not is_left_child
#     return hash == root
def verify_proof(leaf_hash, proof, root_hash):
    hash = leaf_hash
    for item in proof:
        if "right" in item:
            hash = hashlib.sha256((hash + item["right"]).encode()).hexdigest()
        elif "left" in item:
            hash = hashlib.sha256((item["left"] + hash).encode()).hexdigest()
    print(hash)
    print(root_hash)
    return hash == root_hash

dictionaries = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}]
leaf_hashes = get_leaf_hashes(dictionaries)
parent_hashes = build_merkle_tree(leaf_hashes)
root_hash = parent_hashes[-1]

leaf_hash = leaf_hashes[0]
proof = generate_proof(leaf_hash, leaf_hashes, parent_hashes[:-1])

print(verify_proof(leaf_hash, proof, root_hash))




# dictionaries1 = [{'data': 'abc'}, {'data': 'def'}, {'data': 'ghi'}]
# dictionaries2 = [{'data': 'abc'}, {'data': 'def'}, {'data': 'ghi'}]
# leaf_hashes1 = get_leaf_hashes(dictionaries1)
# leaf_hashes2 = get_leaf_hashes(dictionaries2)
# merkle_root1 = build_merkle_tree(leaf_hashes1)[0]
# merkle_root2 = build_merkle_tree(leaf_hashes2)[0]
# print(merkle_root1)
# print(merkle_root2)
# print(merkle_root1 == merkle_root2)
