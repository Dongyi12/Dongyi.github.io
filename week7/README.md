# Week 7 Week 5 

## source of inspiration
### Author Related

I am inspired by the work of Tony Oursler, who uses artificial intelligence and multimedia to embed the the five sense organs or parts of the body with human characteristics into other materials.

### Works Analysis

In the exhibition b0t / flOw - ch@rt, robotic glass sculptures with artificial intelligence, miniature flat screens, exposed computer circuitry and a variety of materials figuratively arranged are shown next to two dimensional screens based on flow charts. The chimerical bots relate to Oursler's ongoing interest in our day to day interactions with technology and question the intelligence of the A.I.-systems.

## Background
([see code](week7\Week 7 Week 5-cutting .py))
(week7\images\cutting.png)
So I tried to see if the code could recognise each of the five sense organs and place them in the background. Or try some cutting, filter effects
I first tried to make the camera on a background, the basic background drawing could not be completed for output, so using NumPy array creation and manipulation, creating a white background would allow me to control the size and colour of the background and be able to seamlessly incorporate it with the image captured by the camera.

```python
        background_height = self.height + 200 
        background_width = self.width + 200  
        white_background = np.full((background_height, background_width, 3), 255, dtype=np.uint8)
```
## Camera Setting
([see code](week7\Week 7 Week 5-cutting .py))

Can a camera frame be cut into more than one, so I tried to cut the camera and created a `Tonytype` (Tony Oursler's method of cutting faces) storage list.
```python
 Tonytype = []
```
I tried to cut the screen into six equal parts, I tested two for loops, firstly on top of the two loops  `for`  the width cuts I added three equal parts corresponding to the height of the screen.
(week7\images\cutting.png)
```python
for i in range(3):
    for j in range(2):
        part = camera_feed[i * Tonytype_height:(i + 1) * Tonytype_height,
                        j * Tonytype_width:(j + 1) * Tonytype_width]
                    Tonytype_parts.append(part) 
```

## Color 
([see code](week7\Week 7 Week 5-Red And Blue Filter .py))

I wanted to try to make the image more colourful, so I tried converting the greyscale image to HSV, converting the binarised image to colour and changing the white pixels (foreground) to other colours (the colours here are just an experiment).

```python
cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)：
colored_thresholded[np.where((colored_thresholded == [255, 255, 255]).all(axis=2))] = [0, 0, 255]
(week7\images\Red and Blue.png)```

## An Error!

Then the code prompts me that the input image `hsv_image` for the `cv2.absdiff` function does not have the same size or number of channels as `self.model`.

So I created a three colour channel for storing colour images. And will convert the model image to HSV colour space.
From this I added a layer of special effects to the image, but the visual effect was not aesthetically pleasing and I tried to change the black colour in the image.

```python
            red_blue_effect = np.zeros_like(camera_feed)
            red_blue_effect[:, :, 0] = thresholded 
            red_blue_effect[:, :, 2] = thresholded 
```
(week7\images\Red and Blue.png)
## Face Recognition


Here I tried face recognition, with a method derived from the Internet.
(Available at:https://github.com/FontTian/DS-Exhibitio)

([see code](E:\\vscode\\STEM-4-Creatives-24-25\\week7\\week7-Week5-Face Recognition.py))

The basic principle uses the OpenCV approach of calculating the sum and difference of pixels in a rectangular region of an image to describe an image feature classifier for face and features (eyes, nose, mouth) detection.

Which utilises `haarcascade_frontalface_default.xml`: this is a pre-trained model file for detecting frontal faces.
This method haarcascade_eye, mcs_nose,mcs_mouth.xml for detecting eyes,nose,mouth.
```
faces=self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)
```
where `detectMultiScale` is a calculator Haar used to calculate the pixel sums and differences of rectangular regions in an image to describe the image features classifier into a cascade classifier a method for detecting multiple objects in an image (such as faces).
`camera_feed_grayscale` This is the input greyscale image.
1.1: The image scaling ratio, each time the image size is reduced by 10%.
4: this is the minimum number of neighbours that should be kept for each candidate rectangle. This parameter affects the quality of the detection results; the larger the value, the more accurate the results, but the fewer objects are detected.
```
for (face_x, face_y, face_w, face_h) in faces:
    roi_gray = camera_feed_grayscale[face_y:face_y+face_h, face_x:face_x+face_w]

```
faces: this is a list of all detected faces, each element is a rectangle representing the position and size of the face.
face_x, face_y, face_w, face_h: these variables represent the coordinates of the upper-left corner of the face rectangle (face_x, face_y), the width (face_w), and the height (face_h), respectively.
roi_gray: this is the face region extracted from the grey scale image
```
eyes = self.eye_cascade.detectMultiScale(roi_gray)
nose = self.nose_cascade.detectMultiScale(roi_gray)
mouth = self.mouth_cascade.detectMultiScale(roi_gray)

```

The principle of operation is firstly load the image classifier, secondly convert the input image to grey scale image for the classifier to process, thirdly use the face classifier to detect faces in the grey scale image, fourthly for each detected face, extract its region and finally in the extracted face region, detect it using eye, nose and mouth classifiers respectively.

## Error.

The syntax Tonytype= [] for creating an empty list defines it as a NumPy array, which has no append method. I defined Tonytype as a list to store image fragments. Change `Tonytype.append(Tonytype)` to `Tonytype_parts.append(part)` and define it as a list to add image segments using the append method.

When calling the `cv2.cvtColor function`, the input image has an incorrect number of channels. Specifically, the number of channels in the thresholded image is 3, while cv2.COLOR_GRAY2BGR expects the number of channels in the input image to be 1
([see code](week7\Week 7 Week 5-cutting .py))

## Conclusions
First attempt at this method with for loops, and face recognition.
The code lacks handling of camera reading failures or other possible errors, some parameters such as window size, thresholds, etc. are hard-coded, and random positioning lacks boundary checking for the output image.