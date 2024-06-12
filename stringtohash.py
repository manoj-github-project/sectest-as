import hashlib

result = hashlib.md5(b"My_inpute_string1").hexdigest()
print(result)

m = hashlib.md5(b"My_inpute_string2")
print(m.name)
print(m.digest_size)
print(m.digest())   
print(m.hexdigest()) 
