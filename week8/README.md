# Week 8 Week 5

My source of inspiration is related to the history of feminism, and the rise of technological advancement has had a complex impact on feminism. On the one hand, the internet has provided a platform for women to display themselves and express their views, enhancing their voice and social influence.

However, there are also some problems with online platforms. Some of the content focuses too much on appearance and body display, reinforcing certain stereotypes and consumerist tendencies. In addition, some may cater to popular tastes in order to attract traffic, ignoring the core values of feminism.
(Accepted：https://interactive.unwomen.org/multimedia/timeline/womenunite/en/index.html#/2000)

## Adaptation of audio

Use librosa to load three audio files, stored in audio, audio2, and audio3, cut samples of the first two beats from audio2, and overwrite them with the second and third beat positions of audio.

```python
cut = audio2[:samples_in_beat * 2]
audio[samples_in_beat:samples_in_beat * 3] = cut
```
To do beat tracking on it. We can then ``is_beat()`` call this function in the draw() loop, which will tell us if there is a beat in this frame, so we can check if the value of ``self.show_beat`` is greater than 3. Inputting different colours to overlay the image

```python
        if dot.music.is_beat():
            self.show_beat = 10

        if self.show_beat > 3:
```
I use dot.music.start_sample_stream(audio + drums, sr=sr) to combine the three voices together ramp way to fade into audio2
 ([see code](week8\Week 8 Week)) 5-sculpture-blue
```python
        ramp = np.linspace(0,1,len(audio2))
        audio_output = audio2 * ramp
```
Updating the background colour in a draw() loop with is_beat()

``self.show_beat`` is used to trigger a change in the background colour when a beat is detected and gradually return to the original colour over several frames. This effect synchronises the visuals with the audio beat, adding interactivity and visual impact.

## Rotational 

In order to achieve the desired effect on the screen, I changed ``theta = (factor * (i/num_faces)) * 2 * np.pi`` from its original function type
``theta = factor * 2 * np.pi``

Use to convert factor to an angle (\theta) ranging from 0 to (2\pi) radians. Rotate 360° by multiplying factor by (2\pi).

I was very interested in the possibility of drawing some characteristic items with the base model, so I drew an eye in an ellipse and rotated it.

Define the centre of rotation ``origin = (dot.width // 2, dot.height // 2):`` set the centre point of the rotation to the centre of the canvas.
Apply rotation transformation ``new_canvas = dot.transform(new_canvas, rotate, origin):`` transforms the image using the rotation matrix.

Draw the image ``dot.draw_layer(new_canvas):``

E:\vscode\STEM-4-Creatives-24-25\week8\images\Sculpture.mp4

## Mistake

Initially the run failed because I often forget \\(‘E:\\vscode\\STEM-4-Creatives-24-25\\week8\\picture02’, thumbnail_size1)

## Conclusions 

Doing this work I found that introducing randomness can be an interesting way to compose new music, but if you have to much then even the randomness can become predictable. I approached this task considering a very rhythmic approach and my techniques only really worked because the sources I picked where the same tempo and already aligned, and with mainly percussive sounds harmonic clash was less of an issue. I wander how audio analysis could help me when there hasn't been so much preprocessing?

# Week 8 Week 3
([see code](week8\Week 8 Week3-Mouse.py)) 
通过鼠标移动让我脑海里有了一个不断增值并且鼠标带动无数个小球移动的画面。首先需要确保每个球之间不会重叠，我们需要不断计算他们是否重叠，一旦两个圆的距离小于两个圆形半径之和，则认为它们重叠。我们需要不断更新重复。
这里我引用
因此我使用 ``self.is_overlapping(new_circle)`` 方法检查新圆形是否与现有圆形重叠，重叠返回 True；否则返回 False。如果不重叠，则将其添加到 ``self.circles`` 列表中。
```python
def is_overlapping(self, new_circle):
    x_new, y_new, radius_new, _ = new_circle
    for x, y, radius, _ in self.circles:
        distance = ((x - x_new) ** 2 + (y - y_new) ** 2) ** 0.5
        if distance < radius + radius_new:
            return True
    return False
```
Here I chose to call the ``self.add_new_circle()`` method every 10 frames to generate a new circle. This keeps the frame growing in value.
Use a for loop to make the positions of all the circles move smoothly according to the mouse position. The new x and y positions are interpolated between the current coordinates and the mouse coordinates.
If they overlap ``if not self.is_overlappin(temp_circle):`` then update the position of the circle.

```python
def draw(self):
    dot.background((255, 0, 100))

    # Generate new circles at intervals
    if dot.frame % 10 == 0:
        self.add_new_circle()

    # Update and draw all circles, making them move smoothly towards the mouse
    for i, circle_data in enumerate(self.circles):
        x, y, radius, color = circle_data
        new_x = x + (dot.mouse_x - x) * 0.1  # Further reduce step size for smoother movement
        new_y = y + (dot.mouse_y - y) * 0.1
        temp_circle = [new_x, new_y, radius, color]

        # Check if the new position overlaps
        if not self.is_overlapping(temp_circle):
            self.circles[i][0] = new_x
            self.circles[i][1] = new_y

        circle(dot.canvas, (int(self.circles[i][0]), int(self.circles[i][1])), radius, color, -1)
```
## Mistake
It is easy to experience logical errors such as the omission of certain details, the judgement of ``if distance > 1`` if conditional clauses, and so on.
## Conclusions
This code requires a change in the original logic, from the screen it looks like some circles are added but many methods (add_new_circle, is_overlapping, draw) and several properties (num_circles, min_radius, max_radius, circles) need to be added.