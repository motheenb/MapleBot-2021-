import threading
from threading import Lock
import cv2 as cv
from windowcapture import WindowCapture
from vision import Vision
from detection import Detection


class Main(threading.Thread):

    lock = None
    window_capture = None
    vision = Vision()
    player_minimap = None
    '''
    game_portal = None
    floor_portal = None
    monster = None
    ladder_top = None
    loop_time = None
    '''
    screen_shot = None

    def __init__(self, client_name):
        threading.Thread.__init__(self)
        self.lock = Lock()
        self.window_capture = WindowCapture(client_name)
        self.player_minimap = Detection('player_minimap.jpg')
        '''
        self.game_portal = Detection('maple_portal.jpg')
        self.floor_portal = Detection('floor_portal.jpg')
        '''
        self.monster = Detection('npc.jpg')
        '''
        self.ladder_top = Detection('ladder_top.jpg')
        '''

    def run(self):
        self.window_capture.start()
        self.player_minimap.start()
        self.monster.start()
        '''
        self.game_portal.start()
        self.floor_portal.start()
        self.ladder_top.start()
        '''
        while True:
            if self.window_capture.screen_shot is None:
                continue

            self.monster.update(self.window_capture.screen_shot)
            self.player_minimap.update(self.window_capture.screen_shot)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.monster.rectangles)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.player_minimap.rectangles)


            '''
            self.game_portal.update(self.window_capture.screen_shot)
            self.floor_portal.update(self.window_capture.screen_shot)
            
            self.ladder_top.update(self.window_capture.screen_shot)
            #print(self.player_minimap.rectangles)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.game_portal.rectangles)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.floor_portal.rectangles)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.monster.rectangles)
            self.vision.draw_rectangles(self.window_capture.screen_shot, self.ladder_top.rectangles)
            #self.floor_portal.rectangles = []
            '''
            cv.imshow('Bot', self.window_capture.screen_shot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break


def main():
    m = Main('MapleStory')
    m.start()


if __name__ == '__main__':
    main()
