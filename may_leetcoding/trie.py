

class TrieNode:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end_of_word = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        crawl = self.root
        for lvl in range(len(word)):
            idx = ord(word[lvl]) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = TrieNode()
            crawl = crawl.children[idx]
        crawl.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        crawl = self.root
        for lvl in range(len(word)):
            idx = ord(word[lvl]) - ord('a')
            if crawl.children[idx] is None:
                return False
            crawl = crawl.children[idx]

        return crawl is not None and crawl.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        crawl = self.root
        for lvl in range(len(prefix)):
            idx = ord(prefix[lvl]) - ord('a')
            if crawl.children[idx] is None:
                return False
            crawl = crawl.children[idx]
        return crawl is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)