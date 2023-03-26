import cv2 as cv2
import mediapipe as mp
import math

class handDetector():
    def __init__(self, mode = False, max_hands = 2, model_complexity=1, detection_confidence = 0.5, track_confidence = 0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_complexity, self.detection_confidence, self.track_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        
    def find_hands(self, img, draw = True):
        imgRGB = cv2.cvtColor( img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img
    
    def find_position(self, img, hand_num = 0, draw = True):
        self.lm_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hand_num]

            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h )
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 2, (255, 0 , 0), cv2.FILLED)
        return self.lm_list
    
    def find_angles(self, img,  positionsDict, draw=True):
        # Get the landmarks
        angleDict = {}
        for key in positionsDict:
            x1, y1 = self.lmList[positionsDict[key][0]][1:]
            x2, y2 = self.lmList[positionsDict[key][1]][1:]
            x3, y3 = self.lmList[positionsDict[key][2]][1:]
            # Calculate the Angle
            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                math.atan2(y1 - y2, x1 - x2))
            if angle < 0:
                angle += 360
                
            if draw:
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
                cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
                cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
                cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                
            angleDict[key] = angle
        return angleDict