from cv2 import line

def draw_bars(canvas, bars=2, beats=4):
    total_beats = bars * beats
    width = canvas.shape[1]
    height = canvas.shape[0]
    beat_spacing = width // total_beats
    bar_spacing = beat_spacing * beats
    for i in range(bars):
        # Draw bar line (thicker line for bars)
        x_pos_bar = i * bar_spacing
        line(canvas, (x_pos_bar, 0), (x_pos_bar, height), (0, 0, 255), 15)
        # Draw beat lines within each bar (thinner lines for beats)
        for j in range(1, beats):
            x_pos_beat = x_pos_bar + j * beat_spacing
            line(canvas, (x_pos_beat, 0), (x_pos_beat, height), (255, 0, 0), 8)