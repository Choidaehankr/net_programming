from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc")
digest.update(b"123")
hash = digest.finalize()
print(hash)

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc123")
hash = digest.finalize()
print(hash)

digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc124")
hash = digest.finalize()
print(hash)