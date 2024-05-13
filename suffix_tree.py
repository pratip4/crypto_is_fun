# This is a suffix tree node implementation for pattern matching.
# useful for cracking ciphers

class SuffixTreeNode():
    def __init__(self):
        self.children = {} # dictionary for child nodes

    def build_suffix_tree(self, msg):
        root = SuffixTreeNode()
        
        for i in range(len(msg)):
            node = root

            for ch in msg[i:]:
                if ch not in node.children:
                    node.children[ch] = SuffixTreeNode()
                node = node.children[ch]

        return root

if __name__ == '__main__':
    sfx = SuffixTreeNode()
    msg = 'KRPQESXERHAIQSYK GJNCMWWKHGSQUZ'
    patterns = sfx.build_suffix_tree(msg)
    
    print(f'{patterns}')
