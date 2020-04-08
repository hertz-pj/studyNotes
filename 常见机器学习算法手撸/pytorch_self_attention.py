import torch
import torch.nn.functional as F

def attention(Q: torch.tensor, K: torch.tensor, V: torch.tensor):

    score = Q.matmul(K.transpose(1, 2))
    p_attn = F.softmax(score, dim=-1)

    return p_attn.matmul(V)