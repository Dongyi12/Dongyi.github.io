# Week 6
According to the week6-mosaic mosaic code, is it possible to have the image overlay only areas of a certain colour and do other effects on other areas?

## Enhanced saturation

I started by enhancing the saturation of the images by ``enhanced_dataset``, first using a for loop for each image in the dataset. Convert the images in NumPy array format to PIL image objects using Image.fromarray. Create a colour enhancer object to enhance the colour saturation of the image.
```python
enhancer = ImageEnhance.Color(pil_img)
```
Increase the colour saturation of the image by a factor of 3 using the enhancer.enhance(3) method. so that these colours can be better distinguished.
```python
enhanced_dataset.append(np.array(enhanced_img))
```
Finally the enhanced image is converted back to NumPy array format and added to the enhanced_dataset list.

## Black Cover

colour_threshold can determine whether or not to fill the image. Setting a value can be used as a threshold for determining whether a picture has a colour or not. Thus setting a threshold value can exclude some colours.
```python
color_threshold = 110 
```
``np.mean(matched_image)``
The average colour value of all pixels of matched_image can be calculated. This value is a scalar for the overall brightness or colour intensity of the image
``if mean_color > color_threshold:`` Indicates that only coloured images are filled

Original Picture
E:\\vscode\\STEM-4-Creatives-24-25\\week6\\images\\2.jpg
It's turned into

![Picture of camera shake](week6\images\1.jpg)

![Picture of camera shake](week6\week6\images\Picture01.png)
([see code](E:\vscode\STEM-4-Creatives-24-25\week6\Week6-Background.py)).

## Error.
Ensure that the argument k to ``np.random.randint(k)`` is valid and within reasonable limits.

## Conclusion
``color_threshold`` The larger the numeric parameter the more dark colours may be removed. This code implements the functionality I've been exploring, but I should have paid more attention to adding an error handling mechanism to ensure that the program doesn't crash if the image fails to load.
I will keep trying different colour enhancement parameters to explore the best visual results.