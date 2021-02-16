
# PARAMETER
MOUTH_RELATION_PUFFER = 1.2 # 1.1 = 10% devation is valid
EYES_SLIT = 0.8 # 0.5 = eye slit detected if eyes height 50% of neutral height

class FacepartAnalysis:
    def __init__(self):
        self.emotion = "neutral"
        # lip corner puller
        self.neutral_mouth_relation_sum = 0
        self.neutral_mouth_relation = 0
        self.lip_corner_puller = False
        # eye slit
        self.eyes_slit = False

        self.left_eye_height_sum = 0
        self.left_eye_height = 0
        self.right_eye_height_sum = 0
        self.right_eye_height = 0

    # lip corner puller:
    def addNeutralMouthRelation(self, mouth):
        self.neutral_mouth_relation_sum += mouth.relation

    def setNeutralMouthRelation(self, frames):
        self.neutral_mouth_relation = self.neutral_mouth_relation_sum/frames

    def checkLipCornerPuller(self, mouth):
        if mouth.relation > self.neutral_mouth_relation * MOUTH_RELATION_PUFFER:
            self.lip_corner_puller = True
        else: 
            self.lip_corner_puller = False

    # eyes slit:
    def addEyesHeight(self, left_eye, right_eye):
        self.left_eye_height_sum += left_eye.height
        self.right_eye_height_sum += right_eye.height

    def setEyesHeight(self, frames):
        self.left_eye_height = self.left_eye_height_sum/frames
        self.right_eye_height = self.right_eye_height_sum/frames

    def checkEyesSlit(self, left_eye, right_eye):
        if (left_eye.height < self.left_eye_height * EYES_SLIT) and (right_eye.height < self.right_eye_height * EYES_SLIT):
            self.eyes_slit = True
        else: 
            self.eyes_slit = False

    # emotion
    def setEmotion(self):
        if self.lip_corner_puller and self.eyes_slit:
            self.emotion = "happy"
        else:
            self.emotion = "neutral"
    

    