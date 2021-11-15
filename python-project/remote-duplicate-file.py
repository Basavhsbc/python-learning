# important in-build operating system and hashing module using import statement
import os
import hashlib

'''
Appends same files to the list belongs to a specific key(same md5 checksum) in the dictionary.
Input: my_dictionary(dictionary data structure), dirPath(path of the directory)
'''
def createDictionary(my_dictionary, dirPath):
    # Traverse folder recursively that is including sub folders.
    for dirName, subdirList, fileList in os.walk(dirPath):
        for fname in fileList:
            # join directory, name and file name to get full path
            fullpath = os.path.join(dirName, fname)
            # initialize hash
            hash=hashlib.md5()
            # print(f"hash object is initialized {hash}")
            # use "ignores" to avoid errors due to unicode encoding and update hash by chunks to avoid memory errors
            with open(fullpath, errors="ignores") as fileTocheck:
                # chunk size can be increased or decreased
                for chunk in iter(lambda: fileTocheck.read(40960), ""):
                    hash.update(str(chunk).encode('utf-8'))
                # unicode->utf-8, use md5 checksum to determine same files
                md5Hash = hash.hexdigest()
                # print(md5Hash)
                # append if it exist
                if md5Hash in my_dictionary:
                    my_dictionary[md5Hash].append(fullpath)
                    # print(my_dictionary)
                else:
                    my_dictionary[md5Hash]=[fullpath]
    print(f"To print dictionary after creating it {my_dictionary}")

'''
Finds duplicate files, removes the ones created later. Keeps the original file. Returns the size of the deleted files.
Input: dupDict(dictionary data structure)
Output: totalSize(total size of the deleted files)
'''
def removeDuplicates(my_dictionary):
    # initialize total size
    totalSize=0
    # check each MD5 hash
    print(f"Inside remoteDuplicate function ...")
    # print(my_dictionary)
    for key in my_dictionary:
        # Print the list of duplicate files to show information
        # print("inside for loop statement")
        # if there are more than two files for the same md5 checksum, keep the first created one and remove others
        if (len(my_dictionary[key]) > 1):
            # print the list of duplicate files to show information
            sameFiles = my_dictionary[key]
            print(sameFiles)
            # create a list of creation times, since the files are same, it actually does not matter
            ctList = [os.path.getctime(i) for i in sameFiles]
            # get the index of the minimum (first created)
            minIdx = ctList.index(min(ctList))
            # remove others and keep the original, sum the size of the deleted files (calcSizeAndDel func.)
            totalSize = totalSize + sum([calcSizeAndDel(i) for i in sameFiles if sameFiles.index(i) != minIdx])
    return totalSize

'''
Removes the given file and returns its size
Input: file(file path)
Output: size(size of the file in bytes)
'''
def calcSizeAndDel(file):
    size = os.path.getsize(file)
    os.remove(file)
    return size

def main():
    dirPath='C:\\Users\\admin\\Desktop\\python-learning\\python-learning\\python-project'
    my_dictionary=dict()
    createDictionary(my_dictionary,dirPath)
    totalSize = removeDuplicates(my_dictionary)
    # convert "bytes" to "megabytes" and limit to two decimal points
    print("Recovered:%.2f MBs" % (totalSize / (1024 ** 2)))

'''
Run the main above
'''
if __name__ ==  "__main__":
    main()
