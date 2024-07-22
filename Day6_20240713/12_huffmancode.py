from collections import Counter, defaultdict
import heapq


text = """i found a love, for me
darling, just dive right in and follow my lead
well, i found a girl, beautiful and sweet
oh, i never knew you were the someone waiting for me"""


frequency = Counter(text)

heap = [[weight, [char, ""]] for char, weight in frequency.items()]
heapq.heapify(heap)

while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
huffman_dict = {char: code for char, code in huffman_codes}

encoded_text = ''.join(huffman_dict[char] for char in text)

huffman_encoded_bits = len(encoded_text)

original_bits = len(text) * 8


compression_ratio = original_bits / huffman_encoded_bits

print("Huffman Codes:")
for char, code in huffman_dict.items():
    print(f"'{char}': {code}")

print(f"Original text length (in bits): {original_bits}")
print(f"Encoded text length (in bits): {huffman_encoded_bits}")
print(f"Compression ratio: {compression_ratio:.2f}")
