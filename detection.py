import cv2 as cv
from threading import Thread, Lock
from vision import Vision


class Detection:

    # threading properties
    stopped = True
    lock = None
    rectangles = []
    # properties
    img = None
    vision = Vision()
    screenshot = None

    def __init__(self, img_path):
        self.lock = Lock()
        self.img = cv.imread(img_path, cv.IMREAD_UNCHANGED)

    def update(self, screenshot):
        if screenshot is not None:
            rectangles = self.vision.find_all_rectangles(screenshot, self.img, threshold=0.7)
        self.lock.acquire()
        self.screenshot = screenshot
        if len(rectangles):
            self.rectangles = rectangles
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:

            if self.screenshot is not None:
                pass
                rectangles = self.vision.find_all_rectangles(self.screenshot, self.img, threshold=0.7)
                if len(rectangles):
                    self.lock.acquire()
                    self.rectangles = rectangles
                    self.lock.release()

