import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib
import numpy as np

FRUITS_DIR = '/Users/cayler/Downloads/fruits-360/'

if __name__ == "__main__":
    # Device configuration
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # Hyper parameters
    num_epochs = 5
    num_classes = 10
    batch_size = 100
    learning_rate = 0.001
