import os


def find_files(suffix, path):
    arr = list()
    if not os.path.isdir(path):
        return None
    def recursion_files(suffix, path, arr):
        for element in os.listdir(path):
            if element.endswith(suffix):
                arr.append(element)
            if os.path.isdir(path+f'/{element}'):
                recursion_files(suffix, path+f'/{element}', arr)
    recursion_files(suffix, path, arr)
    return arr


print(find_files(".c", "./testdir")) #directory does not exist; returns None
print(find_files(".c", "./testdir_1")) #empty directory; returns empty list
print(find_files(".c", "./testdir_2")) #udacity test directory; returns ['a.c', 'b.c', 'a.c', 't1.c']
