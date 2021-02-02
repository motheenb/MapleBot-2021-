import cv2 as cv
import numpy as np


class Vision:

    def draw_rectangles(self, screen_shot, rectangles):
        if len(rectangles):
            # these colors are actually BGR
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            for (x, y, w, h) in rectangles:
                # determine the box positions
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # draw the box
                cv.rectangle(screen_shot, top_left, bottom_right, line_color, lineType=line_type)
        return screen_shot

    def find_all_rectangles(self, screen_shot, image, threshold):
        result = cv.matchTemplate(screen_shot, image, cv.TM_CCOEFF_NORMED)
        img_w = image.shape[1]
        img_h = image.shape[0]
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        rectangles = []
        if len(locations):
            #print(locations)

            # print(rectangles)
            for loc in locations:
                #print(loc)
                rect = [int(loc[0]), int(loc[1]), img_w, img_h]
                rectangles.append(rect)
                rectangles.append(rect)
                # #print(rectangles)
            if len(rectangles):
                rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
        return rectangles
        #print(rectangles)
        '''
        if len(rectangles):
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            for (x, y, w, h) in rectangles:
                # determine the box positions
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # draw the box
                cv.rectangle(screen_shot, top_left, bottom_right, line_color, lineType=line_type)
        '''
