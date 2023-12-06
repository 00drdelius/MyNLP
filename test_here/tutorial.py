import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self,hidden_size:int,vocab_size:int) -> None:
        super().__init__()
        self.embedding=nn.Embedding(vocab_size,hidden_size)
        self.linear=nn.Linear(hidden_size,hidden_size,bias=True)
