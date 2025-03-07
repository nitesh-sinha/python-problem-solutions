# Suppose we have a file system that stores both files and directories. An example of one system is represented
# as the following (with ⟶ representing the tab character)::
#
# dir
# ⟶ subdir1
# ⟶ ⟶ file1.ext
# ⟶ ⟶ subsubdir1
# ⟶ subdir2
# ⟶ ⟶ subsubdir2
# ⟶ ⟶ ⟶ file2.ext
#
# If we were to write this representation in code, it will look like this:
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".
# Note that the '\n' and '\t' are the new-line and tab characters
#
# Every file and directory has a unique absolute path in the file system, which is the order of directories
# that must be opened to reach the file/directory itself, all concatenated by '/'s. Using the above example,
# the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". Each directory name consists of letters, digits,
# and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits,
# and/or spaces.
#
# Given a string input representing the file system in the explained format, return the length of the longest absolute
# path to a file in the abstracted file system. If there is no file in the system, return 0.
#
# Note that the testcases are generated such that the file system is valid and no file or directory name has length 0.
#
# Example 1:
# Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
# Output: 20
# Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
#
# Example 2:
# Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# Output: 32
# Explanation: We have two files:
# "dir/subdir1/file1.ext" of length 21
# "dir/subdir2/subsubdir2/file2.ext" of length 32.
# We return 32 since it is the longest absolute path to a file.
#
# Example 3:
# Input: input = "a"
# Output: 0
# Explanation: We do not have any files, just a single directory named "a".
#
# Constraints:
#
# 1 <= input.length <= 104
# input may contain lowercase or uppercase English letters, a new line character '\n', a tab character '\t',
# a dot '.', a space ' ', and digits.
# All file and directory names have positive length.

# Time complexity: O(n*d) where n=no. of files or dirs in filesystem, d=depth(no. of levels) of filesystem
# Space complexity: O(d)

class LongestFilePath:
    def fetch(self, input: str) -> int:
        paths = input.split('\n')
        stack = [""] # to store absolute dir names while traversing the input.
        # stores the longest path name of file(although for this specific question,
        # only storing counts would be enough)
        max_filename = ""
        for path in paths:
            path_parts = path.split('\t')
            depth = len(path_parts)
            name = path_parts[-1] # last part, after splitting on tab, is the file or dir name
            # We have reached a new dir with lesser depth.
            # Pop all the previous subdir names from stack
            # as they're not needed anymore
            while depth < len(stack):
                stack.pop()
            if '.' in name:
                # its a file, obtain absolute filename
                # by appending absolute dirname with current
                # filename
                cur_filename = stack[-1] + name
                if len(cur_filename) > len(max_filename):
                    max_filename = cur_filename
            else:
                # its a dir, store the absolute dir name on stack
                stack.append(stack[-1] + name + '/')

        #print(max_filename)
        return len(max_filename)


if __name__ == "__main__":
    lfp = LongestFilePath()
    inputs = [
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
        "dir\n\tsubdirectorywith a long name\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\t\tfile3.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
        "dir\n\tfile2.ext",
        "dir",
        "dir\n\nsubdir"
    ]
    for input in inputs:
        max_file_path_len = lfp.fetch(input)
        print(max_file_path_len)
        print("===============")

    # Outputs:
    # 32
    # == == == == == == == =
    # 42
    # == == == == == == == =
    # 32
    # == == == == == == == =
    # 13
    # == == == == == == == =
    # 0
    # == == == == == == == =
    # 0