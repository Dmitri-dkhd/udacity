import os


def find_files(suffix, path):
    arr = list()

    def recursion_files(suffix, path, arr):
        for element in os.listdir(path):
            if element.endswith(suffix):
                arr.append(element)
            if os.path.isdir(path+f'/{element}'):
                recursion_files(suffix, path+f'/{element}', arr)
    recursion_files(suffix, path, arr)
    return arr


print(find_files(".c", "./testdir"))
