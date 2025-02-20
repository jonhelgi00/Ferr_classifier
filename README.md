# Ferritico_classifier

The repository contains code used for extracting a dataset with different images of calculus equations, connected graphs and lewis structure diagrams and training a neural network image classifier.

## Data

The images used for this assignment were scraped from Google and Bing in order to provide the variety needed to hopefully train a robust classifier.

- Images are scraped using GoogleImageCrawler and BingImageCrawler
- After download, images are organized into directories based on their query names.
- A separate script further processes these images by:
  - Resizing and cropping each image using the `resize_and_crop` function from `img_utils.py`.
  - Converting processed images to PyTorch tensors with `img2tensor`.
  - Splitting data (80% training and 20% validation) into corresponding directories under `dataset/Train` and `dataset/Validation`.


## Classifier

After initial experiments with EfficientNet and Swin transformers, I decided to use a ConvNeXt-small as the network structure for the classifier. 

Experiments were run with different training approaches and hyperparameters, such as including the last convolutional block in the finetuning or only training the classifier head. Details can be found in 'ConvNeXt_classifier.ipynb'.

The network was trained in Google Colab for access to slightly more powerful compute. 

As the model was saved, it is too large to push to this github repository. 

<!-- Learning rate: 0.001
Augmentation: True
Training last conv: True -->
<!-- 0.9238095238095239 -->