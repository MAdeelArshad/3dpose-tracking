import argparse

from src.PoseDetection import PoseEstimation

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')

    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    parser.add_argument('--model', type=str, default='cmu',
                        help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--option', type=str, default="camera", help="Camera / Kinect / image_path / camera_image")
    parser.add_argument('--tensorrt', type=str, default="True",
                        help='for tensorrt process.')
    args = parser.parse_args()
    pose = PoseEstimation(args, option=args.option)
    pose.animation()
