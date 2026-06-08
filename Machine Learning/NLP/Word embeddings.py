import numpy as np
from numpy.typing import NDArray


class Solution:
    def lookup(self, embeddings: NDArray[np.float64], token_ids: NDArray[np.int64]) -> NDArray[np.float64]:
        # embeddings: (vocab_size, embed_dim) matrix
        # token_ids: 1D array of integer token IDs
        # Return the embedding vectors for the given token IDs
        # return np.round(your_answer, 5)
        return np.round(embeddings[token_ids], 5)
    
#the output has shape (len(token_ids), embed_dim) because we are selecting the rows of the embeddings matrix corresponding to the token IDs. Each row in the output corresponds to the embedding vector for a specific token ID, and there are as many rows as there are token IDs in the input array.