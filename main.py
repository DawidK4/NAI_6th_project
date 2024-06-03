import sys


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, node):
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.freq)

    def pop(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)


def build_huffman_tree(frequencies):
    pq = PriorityQueue()

    for char, freq in frequencies.items():
        pq.push(Node(char, freq))

    while len(pq) > 1:
        left = pq.pop()
        right = pq.pop()
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        pq.push(merged)

    return pq.pop()


def build_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_encoding(frequencies):
    root = build_huffman_tree(frequencies)
    return build_codes(root)


def read_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    frequencies = {}
    for line in lines[1:n + 1]:
        char, freq = line.split()
        frequencies[char] = int(freq)

    return frequencies


def main(filepath):
    frequencies = read_file(filepath)
    huffman_codes = huffman_encoding(frequencies)

    for char in sorted(huffman_codes):
        print(f"{char} {huffman_codes[char]}")


if __name__ == "__main__":
    main('huffman.txt')
