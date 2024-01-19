#         Two strings are isomorphic if the characters in s can be replaced to get t.
# 
#         All occurrences of a character must be replaced with another character while preserving the order of characters.
#         No two characters may map to the same character but a character may map to itself.
# 
#         For example,
#         Given "egg", "add", return true.
# 
#         Given "foo", "bar", return false.
# 
#         Given "paper", "title", return true.
#
# 
#  Time complexity: O(n) where n=length of string(assuming both strings are of same length)
#  Space complexity: O(n)

class Isomorphic:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        return Isomorphic.isIsomorphicHelper(s,t) and Isomorphic.isIsomorphicHelper(t,s)

    @staticmethod
    def isIsomorphicHelper(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        for idx, charS in enumerate(s):
            if charS in char_map:
                if char_map.get(charS) != t[idx]:
                    return False
            else:
                char_map.update({charS: t[idx]})
        return True


if __name__ == "__main__":
    iso = Isomorphic()
    print(iso.isIsomorphic("egg", "add"))
    print(iso.isIsomorphic("foo", "bar"))
    print(iso.isIsomorphic("paper", "title"))
    print(iso.isIsomorphic("egg", "aaa"))



# Solution 2(slower)
# Find the indices of first occurence of every char
# in s and t. Basically those indices signify whether
# chars are repeated in the string.
# If those indices match, then isomorphic
# Example: for s="egg", t="add"
# s_indices = [0, 1, 1], t_indices = [0, 1, 1]

# def IsIsomorphic(self, s: str, t: str) -> bool:
#     s_indices, t_indices = [], []
#     for char in s:
#         s_indices.append(s.index(char))
#     for char in t:
#         t_indices.append(t.index(char))
#     print(s_indices, t_indices)
#     return s_indices == t_indices