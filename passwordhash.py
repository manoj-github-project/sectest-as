import hashlib
import base64
import uuid

password = 'password123!'
salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)


t_sha = hashlib.sha512()
t_sha.update(password + salt)
hashed_password = base64.urlsafe_b64encode(t_sha.digest())
