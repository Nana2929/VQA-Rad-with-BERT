"""
This code is modified based on Jin-Hwa Kim's repository (Bilinear Attention Networks - https://github.com/jnhwkim/ban-vqa) by Xuan B. Nguyen
"""
import torch.nn as nn
from torch.nn.utils.weight_norm import weight_norm

class SimpleClassifier(nn.Module):
    def __init__(self, in_dim, hid_dim, out_dim,cfg):
        super(SimpleClassifier, self).__init__()
        # print(cfg)
        activation_dict = {'relu': nn.ReLU(inplace=False)}
        try:
            activation_func = activation_dict[cfg.TRAIN.ACTIVATION]
        except:
            # print(cfg.TRAIN.ACTIVATION)
            raise AssertionError(cfg.TRAIN.ACTIVATION + " is not supported yet!")
        layers = [
            weight_norm(nn.Linear(in_dim, hid_dim), dim=None),
            activation_func,
            nn.Dropout(cfg.TRAIN.DROPOUT, inplace=False),
            weight_norm(nn.Linear(hid_dim, out_dim), dim=None)
        ]
        self.main = nn.Sequential(*layers)

    def forward(self, x):
        logits = self.main(x)
        return logits
