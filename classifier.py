import torch
from PIL import Image
import torchvision
from torchvision import transforms
from torchvision.models import convnext_small
import torch.nn as nn

class Ferritico_classifier():
  def __init__(self, path_to_model):
    # self.model = convnext_small(weights=None) 
    self.model = self.initialize_convnext()
    self.model.load_state_dict(torch.load(path_to_model, map_location=torch.device('cpu')))
    self.model.eval()
    self.idx2cls = {0:'equation', 1:'graph', 2:'lewis'}
      
  def transform(self, image):
    transform_image = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                          std=[0.229, 0.224, 0.225])  # ImageNet stats
    ])
    transf_img = transform_image(image)
    return transf_img
    
  def classify(self, path_to_png):
    image = Image.open(path_to_png)
    transformed_image = self.transform(image)
    transformed_image = transformed_image.unsqueeze(0)  # Add batch dimension
    outputs = self.model(transformed_image)
    _, pred = torch.max(outputs, 1)
    class_name = self.idx2cls[pred.item()]
    return class_name
  
  def initialize_convnext(self, num_classes=3):
    model = convnext_small(weights=None)
    
    model.classifier = nn.Sequential(
        nn.Flatten(1),
        nn.Linear(768, num_classes)
    )
    return model
  

# if __name__ == '__main__':
#   classifier = Ferritico_classifier('/Users/jonhelgi/Projects/Ferr_classifier/convnext_best_model.pt')
#   print(classifier.classify('/Users/jonhelgi/Projects/Ferr_classifier/data/dataset/raw_img/google/calculus_equation/000001.png'))
