import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.models as models

import captum
from captum.attr import IntegratedGradients, Occlusion, LayerGradCam, LayerAttribution
from captum.attr import visualization as viz

import os, sys
import json
 
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap



model = models.resnet101(pretrained=True)
model.eval()


test_img = Image.open("img/cat.jpg")
test_image_data = np.asarray(test_img)
plt.show(test_img)
plt.imshow(test_image_data)
plt.show()