from sortKeypoints import getPointBetween

# PARAMETER
MOUTH_RELATION_PUFFER = 1.2 # 1.2 = 20% devation is valid
EYES_SLIT = 1.2 # 0.5 = eye slit detected if eyes relation 20% bigger than neutral
CORNER_DEPRESSOR = 1.25
BROW_LOWERER = 0.85

class FacepartAnalysis:
    def __init__(self):
        self.emotion = "neutral"
        # lip corner puller
        self.neutral_mouth_relation_sum = 0
        self.neutral_mouth_relation = 0
        self.lip_corner_puller = False
        # eye slit = cheek raiser
        self.left_eye_relation_sum = 0
        self.left_eye_relation = 0
        self.right_eye_relation_sum = 0
        self.right_eye_relation = 0
        self.eyes_slit = False
        # lip corner depressor
        self.neutral_distance_sum = 0
        self.neutral_distance = 0
        self.lip_corner_depressor = False
        # brow lowerer
        self.neutral_brow_distance_sum = 0
        self.neutral_brow_distance = 0
        self.brow_lowerer = False

    # lip corner puller:
    def addNeutralMouthRelation(self, mouth):
        self.neutral_mouth_relation_sum += mouth.relation

    def setNeutralMouthRelation(self, frames):
        self.neutral_mouth_relation = self.neutral_mouth_relation_sum/frames

    def checkLipCornerPuller(self, mouth):
        # check if point beween corner higher than point in the middle of top lip OR mouth realation greater than neutral mouth relation
        if (mouth.between_lip_corners.y < mouth.top.y) | (mouth.relation > self.neutral_mouth_relation * MOUTH_RELATION_PUFFER):
            self.lip_corner_puller = True
        else:
            self.lip_corner_puller = False

    # lip corner depressor
    def addNeutralDistance(self, mouth):
        distance = mouth.between_lip_corners.y - mouth.top.y
        self.neutral_distance_sum += distance
    
    def setNeutralDistance(self, frames):
        self.neutral_distance = self.neutral_distance_sum/frames

    def checkLipCornerDepressor(self, mouth):
        distance = mouth.between_lip_corners.y - mouth.top.y
        if distance > self.neutral_distance * CORNER_DEPRESSOR:
            self.lip_corner_depressor = True
        else:
            self.lip_corner_depressor = False

    # eyes slit:
    def addEyesRelation(self, left_eye, right_eye):
        self.left_eye_relation_sum += left_eye.relation
        self.right_eye_relation_sum += right_eye.relation

    def setEyesRelation(self, frames):
        self.left_eye_relation = self.left_eye_relation_sum/frames
        self.right_eye_relation = self.right_eye_relation_sum/frames

    def checkEyesSlit(self, left_eye, right_eye):
        if (left_eye.relation > self.left_eye_relation * EYES_SLIT) and (right_eye.relation > self.right_eye_relation * EYES_SLIT):
            self.eyes_slit = True
        else: 
            self.eyes_slit = False

    # brow lowerer
    def addNeutralBrowDistance(self, keypoints_eyebrows, keypoints_eyes):
        point_between_eyebrows = getPointBetween(keypoints_eyebrows[4], keypoints_eyebrows[5])
        point_between_eyes = getPointBetween(keypoints_eyes[6], keypoints_eyes[3])
        distance = point_between_eyes.y - point_between_eyebrows.y
        self.neutral_brow_distance_sum += distance

    def setNeutralBrowDistance(self, frames):
        self.neutral_brow_distance = self.neutral_brow_distance_sum/frames

    def checkBrowLowerer(self, keypoints_eyebrows, keypoints_eyes):
        point_between_eyebrows = getPointBetween(keypoints_eyebrows[4], keypoints_eyebrows[5])
        point_between_eyes = getPointBetween(keypoints_eyes[6], keypoints_eyes[3])
        distance = point_between_eyes.y - point_between_eyebrows.y

        if distance < self.neutral_brow_distance * BROW_LOWERER:
            self.brow_lowerer = True
        else:
            self.brow_lowerer = False

    # emotion
    def setEmotion(self):
        if self.lip_corner_puller and self.eyes_slit:
            self.emotion = "happy"
        elif self.brow_lowerer and self.lip_corner_depressor:
            self.emotion = "sad"
        else:
            self.emotion = "neutral"
    

    