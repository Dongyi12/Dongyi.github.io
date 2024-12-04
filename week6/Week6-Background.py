from dorothy import Dorothy 
import numpy as np
from PIL import Image, ImageEnhance
from scipy import spatial

dot = Dorothy(1000, 800) 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup) 

    def setup(self):
        
        # Parameters
        src_image_path = 'week6\\images\\Picture01.png'
        dataset_path = "week6\\data\\animal_thumbnails\\land_mammals"
        thumbnail_size = (5, 5)
        downsample_amount = 5
        color_threshold = 230  # Colour threshold, above which images are considered to be close to white
        # Get template
        src_image = np.array(Image.open(src_image_path))
        mosaic_template = src_image[::downsample_amount, ::downsample_amount]

        # Load dataset
        dataset = dot.get_images(dataset_path, thumbnail_size=thumbnail_size)
        mean_image = np.apply_over_axes(np.mean, dataset, [0])
        mean_image = np.squeeze(mean_image).astype(np.uint8)
        mean_rgb_dataset = np.apply_over_axes(np.mean, dataset, [1, 2]).reshape(len(dataset), 3)
        
        # Enhance color saturation of the dataset images
        enhanced_dataset = []
        for img in dataset:
            pil_img = Image.fromarray(img)
            enhancer = ImageEnhance.Color(pil_img)
            enhanced_img = enhancer.enhance(1.5)  # Increase color saturation by a factor of 1.5
            enhanced_dataset.append(np.array(enhanced_img))
        
        enhanced_dataset = np.array(enhanced_dataset)

        # Match images
        tree = spatial.KDTree(mean_rgb_dataset)
        mosaic_template = np.swapaxes(mosaic_template, 0, 1)
        w, h = mosaic_template.shape[0:2]
        matched_images = np.zeros((w, h), dtype=np.uint32)
        
        # Go through each pixel and find the closest matching thumbnail image by mean colour and assign the index into the 2D array
        k = 40  # select the top 40 closest matches
        for row in range(w):
            for col in range(h):
                pixel = mosaic_template[row, col]
                # Get the match
                match = tree.query(pixel, k=k)
                pick = np.random.randint(k)  # randomly select one of the top k matches
                matched_images[row, col] = match[1][pick]
        
        # Paste together
        for i in range(w):
            for j in range(h):
                matched_image = enhanced_dataset[matched_images[i, j], :, :, :]
                mean_color = np.mean(matched_image)
                if mean_color < color_threshold:  # Fill only non-white images
                    # Coordinates to place the thumbnail
                    x, y = i * thumbnail_size[0], j * thumbnail_size[1]
                    dot.paste(dot.canvas, matched_image, (x, y))
                else:
                    # Replace near-white images with white
                    white_image = np.full((thumbnail_size[0], thumbnail_size[1], 3), 255, dtype=np.uint8)
                    x, y = i * thumbnail_size[0], j * thumbnail_size[1]
                    dot.paste(dot.canvas, white_image, (x, y))

MySketch()