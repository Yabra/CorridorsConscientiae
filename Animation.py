class Animation:
    def __init__(self, frames, fps):
        self.frames = frames
        self.current_frame = 0
        self.fps = fps
        self.time = 0

    def get_current_frame(self):
        return self.frames[self.current_frame]

    def update(self, ticks):
        self.time += ticks
        self.current_frame += self.time // (1000 // self.fps)
        self.time %= 1000 // self.fps
        self.current_frame %= len(self.frames)
