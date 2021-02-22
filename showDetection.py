import json
import numpy as np
import cv2
import math
from sortKeypoints import getPointBetween

# plotting as image
def initImage():
  w, h = 1280, 720
  image = np.zeros((h, w, 3), dtype=np.uint8)
  return image

# show image
def showImage(image):
  cv2.imshow("Keypoints", image)
  cv2.waitKey(1)

def textImage(image, emotion, lcp, es, lcd, bl):
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(image,f'mimic:{emotion}',(1000,25), font, 1, (200,255,155), 1, cv2.LINE_AA)
  cv2.putText(image,f'lip corner puller:{lcp}',(0,25), font, 1, (200,255,155), 1, cv2.LINE_AA)
  cv2.putText(image,f'eyes slit:{es}',(0,50), font, 1, (200,255,155), 1, cv2.LINE_AA)
  cv2.putText(image,f'lip corner depressor:{lcd}',(0,75), font, 1, (200,255,155), 1, cv2.LINE_AA)
  cv2.putText(image,f'brow lowerer:{bl}',(0,100), font, 1, (200,255,155), 1, cv2.LINE_AA)

def calibrationText(image):
  font = cv2.FONT_HERSHEY_SIMPLEX
  cv2.putText(image,'CALIBRATION!',(500,500), font, 2, (255,255,0), 2, cv2.LINE_AA)

def drawPoints(image, keypoints):
  for keypoint in keypoints:
      x1 = round(keypoint.x) - 2
      x2 = round(keypoint.x) + 2
      y1 = round(keypoint.y) - 2
      y2 = round(keypoint.y) + 2
      image[y1:y2, x1:x2] = [255, 255, 255]

def drawKeypoints(image, keypoints_eyebrows, keypoints_mouth, keypoints_eyes, mouth, eye):
  # clear image
  image[:,:] = [0, 0, 0]
  # draw white points on keypoints
  if keypoints_eyebrows:
    drawPoints(image, keypoints_eyebrows)
  if keypoints_eyes:
    drawPoints(image, keypoints_eyes)
  if keypoints_mouth:
    drawPoints(image, keypoints_mouth)

  # draw mouth width and height
  point_between_lip_corners = getPointBetween(mouth.left, mouth.right)
  if False:
    cv2.line(image, (mouth.left.x, mouth.left.y), (mouth.right.x, mouth.right.y), (255, 0, 0), 2)
    cv2.line(image, (mouth.top.x, mouth.top.y), (mouth.bot.x, mouth.bot.y), (0, 0, 255), 2)
    cv2.circle(image, (mouth.top.x, mouth.top.y), 10, (0, 255, 0), 2)
    cv2.circle(image, (point_between_lip_corners.x, point_between_lip_corners.y), 10, (255, 0, 0), 2)
  
  if eye:
    cv2.line(image, (lefteye_left.x, lefteye_left.y), (lefteye_right.x, lefteye_right.y), (255, 0, 0), 2)
    cv2.line(image, (righteye_left.x, righteye_left.y), (righteye_right.x, righteye_right.y), (255, 0, 0), 2)

    cv2.line(image, (lefteye_top.x, lefteye_top.y), (lefteye_bot.x, lefteye_bot.y), (255, 0, 0), 2)
    cv2.line(image, (righteye_top.x, righteye_top.y), (righteye_bot.x, righteye_bot.y), (255, 0, 0), 2)
  
  return image

