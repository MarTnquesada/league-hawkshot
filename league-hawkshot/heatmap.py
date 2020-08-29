import os
from typing import List


class HeatmapFrames:
    def __init__(self, posx: int, posy: int):
        self.posx = posx
        self.posy = posy


class HeatmapTimeline:
    def __init__(self, identifier: str, colour: str, frames: List[HeatmapFrames]):
        pass


class Heatmap:
    def __init__(self, background, timelines: List[HeatmapTimeline] = None):
        self.background = background
        self.timelines = []
        if timelines:
            self.timelines = timelines

    def add_timeline(self, identifier, colour):
        pass

    def draw(self, start, end):
        pass
