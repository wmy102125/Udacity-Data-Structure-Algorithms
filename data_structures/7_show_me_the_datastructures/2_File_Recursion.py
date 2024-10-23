import os

from fontTools.misc.cython import returns


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = list()
    try:
        dir_file_lists = os.listdir(path)
    except IOError as e:
     print("open exception: %s: %s" %(e.errno, e.strerror))
     return None
    if dir_file_lists is None:
        return []
    for item in dir_file_lists:
        if os.path.isfile(path + "/" + item):
            if item.endswith(suffix):
                result.append(path + "/" +item)
        else:
             result.extend(find_files(suffix, path + "/" + item))
    return result


# print(os.path.isfile("./testdir/t1.c"))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
def test_function(test_case):
    output = find_files(test_case[0],test_case[1])
    if output == test_case[2]:
        print("Pass")
    else:
        print("Fail")
## Test Case 1
test_case_1 = [".c","./testdir",['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']]
test_function(test_case_1)
## Test Case 2
test_case_1 = [".c","./testdir/subdir2",[]]
test_function(test_case_1)
## Test Case 3
test_case_1 = [".c","./testdir/subdir3",['./testdir/subdir3/subsubdir1/b.c']]
test_function(test_case_1)
## Test Case 4
test_case_1 = [".c","./111",None]
test_function(test_case_1)

## Test Case 4
test_case_1 = [".cccc","./testdir",[]]
test_function(test_case_1)
