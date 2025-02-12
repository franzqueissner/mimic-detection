from getKeypoints import *
from sortKeypoints import *
from analyseFaceparts import FacepartAnalysis
from showDetection import *

# constants
OPENPOSE_ADVANCE = 1 # i give openpose an advance of 1 frame so i can be sure that the keypoint json is ready(i was getting errors sometimes)
MAX_FRAMES = 300 # amount of frames to analyse
CALIBRATION_FRAMES = 30 # amount of frames for calibration

# ---- main loop: -----
facepart_analysis = FacepartAnalysis()
image = initImage()
frames_count = 0
wait_for_frames()

while frames_count < MAX_FRAMES:
    frames = get_frames()
    if frames_count + OPENPOSE_ADVANCE < len(frames):
        frame = frames[frames_count]
        print(f"Analysing frame {frames_count}")
        # get keypoints
        keypoints_face_raw = collect_keypoints(frame)
        if not keypoints_face_raw:
            frames_count += 1
        else:
            keypoints_eyebrows, keypoints_nosebridge, keypoints_nostrils, keypoints_eyes, keypoints_mouth = filter_keypoints(keypoints_face_raw)
            # get face parts
            mouth = getMouth(keypoints_mouth)
            left_eye, right_eye = getEyes(keypoints_eyes)
            left_eyebrow, right_eyebrow = getEyebrows(keypoints_eyebrows)
            # create image
            image = drawKeypoints(image, keypoints_eyebrows, keypoints_mouth, keypoints_eyes, mouth, False)
            # analyse
 
            # collect information for neutral emotion
            if frames_count < CALIBRATION_FRAMES:
                facepart_analysis.addNeutralMouthRelation(mouth)
                facepart_analysis.addNeutralDistance(mouth)
                facepart_analysis.addEyesRelation(left_eye, right_eye)#
                facepart_analysis.addNeutralBrowDistance(keypoints_eyebrows, keypoints_eyes)
                calibrationText(image)
            # set neutral emotion
            if frames_count == CALIBRATION_FRAMES:
                facepart_analysis.setNeutralMouthRelation(CALIBRATION_FRAMES)
                facepart_analysis.setNeutralDistance(CALIBRATION_FRAMES)
                facepart_analysis.setEyesRelation(CALIBRATION_FRAMES)
                facepart_analysis.setNeutralBrowDistance(CALIBRATION_FRAMES)
            # check and set facial action codes facs
            if frames_count > CALIBRATION_FRAMES:
                facepart_analysis.checkLipCornerPuller(mouth)
                facepart_analysis.checkEyesSlit(left_eye, right_eye)
                facepart_analysis.checkLipCornerDepressor(mouth)
                facepart_analysis.checkBrowLowerer(keypoints_eyebrows, keypoints_eyes)

                facepart_analysis.setEmotion()


            # show data
            textImage(image, facepart_analysis.emotion, facepart_analysis.lip_corner_puller, facepart_analysis.eyes_slit, facepart_analysis.lip_corner_depressor, facepart_analysis.brow_lowerer)
            showImage(image)

            frames_count += 1