import math
from getKeypoints import Keypoint
from classes import Mouth, Eye

# helper functions
def get_line_length(start_x, start_y, end_x, end_y):
  """
  takes x and y of start and end point
  returns distance of those points
  """
  a = end_x - start_x
  g = end_y - start_y
  length = math.sqrt(a**2+g**2)
  return length

def getPointBetween(point1, point2):
  x = (point1.x + point2.x)/2
  y = (point1.y + point2.y)/2
  c = (point1.c + point2.c)/2
  return Keypoint(x, y, c)


# --- mouth analyze ---
def getMouth(keypoints_mouth):
    # width
    mouth_left = keypoints_mouth[0] # mouth keypoint which is most left
    mouth_right = keypoints_mouth[6] # mouth keypoint which is most right
    mouth_width = get_line_length(mouth_left.x, mouth_left.y, mouth_right.x, mouth_right.y)

    # height
    mouth_top = getPointBetween(keypoints_mouth[2], keypoints_mouth[4])
    mouth_bot = keypoints_mouth[9]
    mouth_height = get_line_length(mouth_top.x, mouth_top.y, mouth_bot.x, mouth_bot.y)

    # relation
    mouth_relation = mouth_width/mouth_height

    # mouth object
    mouth_object = Mouth(mouth_left, mouth_right, mouth_top, mouth_bot, mouth_width, mouth_height, mouth_relation)

    # log:
    # print(f"Mouth width:{mouth_width:.2f}")
    # print(f"Mouth height: {mouth_height:.2f}")

    return mouth_object

def getEyes(keypoints_eyes):
    # --- eyes analyze ---
    # width
    lefteye_left = keypoints_eyes[0]
    lefteye_right = keypoints_eyes[3]
    lefteye_width = get_line_length(lefteye_left.x, lefteye_left.y, lefteye_right.x, lefteye_right.y)

    righteye_left = keypoints_eyes[6]
    righteye_right = keypoints_eyes[9]
    righteye_width = get_line_length(righteye_left.x, righteye_left.y, righteye_right.x, righteye_right.y)
    # height
    lefteye_top = getPointBetween(keypoints_eyes[1], keypoints_eyes[2])
    lefteye_bot = getPointBetween(keypoints_eyes[4], keypoints_eyes[5])
    lefteye_height = get_line_length(lefteye_top.x, lefteye_top.y, lefteye_bot.x, lefteye_bot.y)

    righteye_top = getPointBetween(keypoints_eyes[7], keypoints_eyes[8])
    righteye_bot = getPointBetween(keypoints_eyes[10], keypoints_eyes[11])
    righteye_height = get_line_length(righteye_top.x, righteye_top.y, righteye_bot.x, righteye_bot.y)

    # eye objects
    lefteye_object = Eye(lefteye_left, lefteye_right, lefteye_top, lefteye_bot, lefteye_width, lefteye_height)
    righteye_object = Eye(righteye_left, righteye_right, righteye_top, righteye_bot, righteye_width, righteye_height)

    # log:
    # print(f"Left eye width: {lefteye_width:.2f}")
    # print(f"Right eye width: {righteye_width:.2f}")
    # print(f"Left eye height: {lefteye_height:.2f}")
    # print(f"Right eye height: {righteye_height:.2f}")
    return lefteye_object, righteye_object