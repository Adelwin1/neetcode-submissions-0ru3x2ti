class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end = "#"
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not  in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def search(self, word: str) -> bool:

        def h(node, i):
            if i == len(word):
                return self.end in node
            
            char = word[i]

            if char == '.':
                for child in node:
                    if child!=self.end and h(node[child], i+1):
                        return True
                return False
            else:
                if char not in node:
                    return False 
                return h(node[char], i+1)
        return h(self.root, 0)


        
