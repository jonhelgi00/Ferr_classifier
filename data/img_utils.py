from PIL import Image
import torch
from torchvision import transforms

def resize_and_crop(image, target_size=224):
  width, height = image.size
  w_h_ratio = width / height

  if width > height:
    new_h = target_size
    new_w = int(target_size * w_h_ratio)
  elif width < height:
    new_w = target_size
    new_h = int(target_size / w_h_ratio)
  else:
    new_w = width
    new_h = height

  resized_img = image.resize((new_w, new_h))

  remove_h = int((resized_img.height - target_size) / 2)
  remove_w = int((resized_img.width - target_size) / 2)

  cropped_img = resized_img.crop((remove_w, remove_h, remove_w + target_size, remove_h + target_size))
  # cropped_img.show()
  return cropped_img

def img2tensor(image):
  """Convert PIL image to PyTorch tensor"""
  image = image.convert("RGB")
  transform = transforms.Compose([
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406],
                          std=[0.229, 0.224, 0.225])
  ])
  
  # Convert to tensor
  tensor = transform(image)
  return tensor

  

# if __name__ == 'main':
# test_image = Image.open('/Users/jonhelgi/Desktop/Screenshot 2024-12-22 at 00.19.14.png')
# resized_image = resize_and_crop(test_image)
# image_before = resized_image.convert("RGB")
# transform__ = transforms.Compose([
#       transforms.ToTensor()
#   ])
# tensor_before = transform__(image_before)
# mean_before = tensor_before.mean(dim=(1, 2))  # Compute mean per channel
# std_before = tensor_before.std(dim=(1, 2))  # Compute mean per channel
# print(f"Mean before normalization: {mean_before}")
# print(f"std before normalization: {std_before}")
# # resized_image.show()
# normalize = transforms.Compose([
#     transforms.Normalize(mean=[0.6612, 0.3841, 0.3590], std=[0.1644, 0.1922, 0.1649])  # Use dataset's stats
# ])
# tensor_after = normalize(tensor_before)
# print(f"mean: {tensor_after.mean(dim=(1,2))}")
# print(f"std: {tensor_after.std(dim=(1,2))}")

# tensor_image = img2tensor(resized_image)
# print(f"Tensor shape: {tensor_image.shape}")
# print(f"mean: {tensor_image.mean(dim=(1,2))}")
# print(f"std: {tensor_image.std(dim=(1,2))}")
# # print(f"max: {tensor_image.max}")
# print(f"max: {tensor_image.max()}")
# print(f"min: {tensor_image.min()}")
# # print(f"min: {tensor_image.min}")
  


#Test
# fpath = '/Users/jonhelgi/Desktop/Cls.png'
# fpath = '/Users/jonhelgi/Projects/Ferr_classifier/data/dataset/raw_img/combined/connected_graph/000012.jpg'
# image_test = Image.open(fpath)
# cropped_image = resize_and_crop(image_test)
# rgb = cropped_image.convert("RGB")
# rgb.show()
# cropped_image.show()
# cropped_image.save('/Users/jonhelgi/Desktop/Cls_cropped.png')
