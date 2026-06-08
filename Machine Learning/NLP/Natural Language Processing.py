import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        combined = positive + negative # Combine the positive and negative sentences into one list
        vocabulary = sorted({word for sentence in combined for word in sentence.split()}) # Build a sorted vocabulary of unique words
        word_to_id = {word: idx + 1 for idx, word in enumerate(vocabulary)} # Create a mapping from words to integer IDs, starting at 1
        encoded = [torch.tensor([word_to_id[w] for w in s.split()]) for s in combined] # Encode each sentence by replacing words with their corresponding IDs
        return nn.utils.rnn.pad_sequence(encoded, batch_first=True) # Pad the encoded sentences to have the same length, using 0s for padding. The output will be a tensor of shape (num_sentences, max_sentence_length) where num_sentences is the total number of sentences (positive + negative) and max_sentence_length is the length of the longest sentence in the combined list.


