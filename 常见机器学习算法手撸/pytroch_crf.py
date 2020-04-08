import torch
import torch.nn as nn

class CRF(nn.Module):

    def __init__(self, num_tags: int) -> None:
        assert num_tags > 0, "num tags must > 0"

        super().__init__()
        self.num_tags = num_tags
        self.start_transitions = nn.Parameter(torch.empty(num_tags))
        self.end_transitions = nn.Parameter(torch.empty(num_tags))
        self.transitions = nn.Parameter(torch.empty(num_tags,num_tags))

        # init parameters
        nn.init.uniform_(self.start_transitions, -0.1, 0.1)
        nn.init.uniform_(self.end_transitions, -0.1, 0.1)
        nn.init.uniform_(self.transitions, -0.1, 0.1)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(num_tags={self.num_tags})'

    def forward(
            self, 
            emissions: torch.Tensor,
            tags: torch.LongTensor,
            mask: Optional[torch.ByteTensor] = None,
            reduction: str="sum"
    ) -> torch.Tensor:
    """
    Compute the conditional log likelihood of a sequence 
    of tags given emission scores.
    """

    assert reduction in ('none','sum','mean','token_mean')
    if mask is None:
        mask = torch.ones_like(tags, dtype=torch.uint8)
    
    def _compute_score(emissions, tags, mask):

        # emission: (batch_size, seq_length, num_tags)
        # tags: (batch_size, seq_length)
        # mask: (batch_size, seq_length)
        assert emissions.dim() == 3 and tags.dim() == 2
        assert emissions.shape[:2] == tags.shape
        assert emissions.size(2) == self.num_tags
        assert mask.shape == tags.shape
        assert mask[0].all()

        batch_size, seq_length = tags.shape
        mask = mask.float()

        score = self.start_transitions[tags[0]]
        score += emissions[]



        


