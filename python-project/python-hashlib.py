# Import hashlib python mode to hash algorithm
import hashlib
# Enter file name where you want to get hash value
filename=input("Enter file name \n")
# # Open file in read mode
# with open(filename, "rb") as file:
#     bytes=file.read() # Read file as bytes
#     readable_hash=hashlib.md5(bytes).hexdigest()
#     print(readable_hash)

## Python program to find out hash value with big file size using better programming
# Initialize md5 hash algorithm
md5_hash=hashlib.md5()
# Open file in read mode
with open(filename,"rb") as f:
    # Read and update hash in chunk of 4k
    for bytes_block in iter(lambda: f.read(4096),b""):
        md5_hash.update(bytes_block)
    print(md5_hash.hexdigest())


