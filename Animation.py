class Animation:
    # frames - список кадров анимации.
    # fps    - количество кадров, сменяющихся за секунду
    def __init__(self, frames, fps):
        self.frames = frames
        self.current_frame = 0
        self.fps = fps
        self.time = 0

    def get_current_frame(self):
        return self.frames[self.current_frame]

    # вызывается перед отрисовкой для обновления номера текущего кадра
    def update(self, ticks):
        self.time += ticks
        self.current_frame += self.time // (1000 // self.fps)
        self.time %= 1000 // self.fps
        self.current_frame %= len(self.frames)
