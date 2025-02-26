# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#   1. WordDictionary(): Initializes the object.
#   2. void addWord(word) Adds word to the data structure, it can be matched later.
#   3. bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
#      word may contain dots '.' where dots can be matched with any letter.
#
# Example:
#
# Input:
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#
# Output:
# [null,null,null,null,false,true,true,true]
#
# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.

class TrieNode:
    def __init__(self):
        self.children = {}  # dict which maps char to node of Trie
        self.is_word = False # True indicates a word is present


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children.update({char: TrieNode()})
            cur_node = cur_node.children.get(char)
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs_search(word, self.root, 0)

    def dfs_search(self, word: str, node: TrieNode, index: int):
        if index == len(word):
            return node.is_word

        if word[index] == ".":
            # Search over all the children of current node.
            # If match found in any one of those searches, return True
            for child in node.children.values():
                if self.dfs_search(word, child, index + 1):
                    return True

        if word[index] in node.children:
            # current char matched, now recursively check for remaining chars
            return self.dfs_search(word, node.children[word[index]], index + 1)
        return False
