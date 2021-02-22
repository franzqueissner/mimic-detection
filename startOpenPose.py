import os

def get_run_number():
    os.chdir('keypoints')
    if os.listdir():
        old_run_number = os.listdir()[-1][-1]
        run_number = int(old_run_number) + 1
    else:
        run_number = 0
    os.chdir('..')
    return run_number

def start_openpose(run_number):
    run = "run" + str(run_number)
    os.chdir("openpose-1.7.0-binaries-win64-gpu-python3.7-flir-3d_recommended\openpose")
    print(f'Starting OpenPose and collecting keypoints in run{run_number}')
    os.system(f"bin\OpenPoseDemo.exe --face --render_pose 0 --display -1 --net_resolution -1x128 --write_json ..\..\keypoints\\{run}")
    # os.system(f"bin\OpenPoseDemo.exe --face --render_pose 0 --display 0 --net_resolution -1x128 --write_json ..\..\keypoints\\{run}")
    os.chdir("../..")


run_number = get_run_number()
start_openpose(run_number)