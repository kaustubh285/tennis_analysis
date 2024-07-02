from utils import read_video, save_video


def main():
    video_path = "input/input_video.mp4"
    saved_video_path = "output/input_video.mp4"
    frames = read_video(video_path)
    print("Hello!!")

    save_video(frames, saved_video_path)


if __name__ == "__main__":
    main()
