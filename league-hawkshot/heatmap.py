from typing import List
from collections.abc import MutableMapping
import matplotlib.pyplot as plt


class HeatmapFrame:
    def __init__(self, posx: int, posy: int, time: int) -> None:
        self.posx = posx
        self.posy = posy
        self.time = time


class HeatmapTimeline:
    def __init__(self, identifier: str, colour: str, frames: List[HeatmapFrame]) -> None:
        self.identifier = identifier
        self.colour = colour
        self.frames = frames


class HeatMapTimelineCollection(MutableMapping):
    def __init__(self, *args, **kwargs) -> None:
        self.key = None
        self.store = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[self.key]

    def __setitem__(self, key, value):
        if self.store.get(self.key) is not None:
            raise HeatMapTimelineCollection.DuplicateKeyError(key)
        self.store[self.key] = value

    def __delitem__(self, key):
        del self.store[self.key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    class DuplicateKeyError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return f'An entry with key {self.value} already exists for this HeatMapTimelineCollection'


class Heatmap:
    def __init__(self, background_path: str, timelines: HeatMapTimelineCollection = None) -> None:
        self.background = plt.imread(fname=background_path, format=None)
        self.timelines = timelines

    def add_timeline(self, timeline: HeatmapTimeline) -> None:
        self.timelines[timeline.identifier] = timeline

    def get_timeline(self, identifier) -> HeatmapTimeline:
        return self.timelines.get(identifier)

    def draw(self, start, end) -> None:
        imgplot = plt.imshow(self.background)
        #plt.show()
