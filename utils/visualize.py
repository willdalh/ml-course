import torchvision.transforms as transforms
from torchvision.utils import make_grid
from PIL import Image

def visualize(data, scale=6):
    # Check if there is a batch dimension
    if data.dim() == 4:
        batch_size = data.size(0)
        if batch_size == 1:
            # Remove the batch dimension if there's only one item in the batch
            data = data.squeeze(0)
        else:
            # Create a grid of images for multiple items in the batch
            data = make_grid(data, nrow=int(batch_size ** 0.5))
    
    h, w = data.shape[-2:]
    image = transforms.functional.resize((data + 1) / 2, (h * scale, w * scale), interpolation=transforms.InterpolationMode.NEAREST)
    
    # Convert to PIL image for visualization
    image = transforms.functional.to_pil_image(image)
    return image

