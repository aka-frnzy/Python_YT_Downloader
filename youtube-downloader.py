from pytube import YouTube


# Functions for audio or video
def download_audio(url, output_path):
    video = YouTube(url)
    stream = video.streams.get_audio_only()
    stream.download(output_path)


def download_hvideo(url, output_path):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path)


def download_lvideo(url, output_path):
    video = YouTube(url)
    stream = video.streams.get_by_resolution("360p")
    stream.download(output_path)


# main program
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output path: ")
    print(
        """What do you want to download
    1.Audio only
    2.Video -High res
    3.Video -Low res
    """
    )
    ch = int(input())
    match ch:
        case 1:
            download_audio(video_url, output_path)
        case 2:
            download_hvideo(video_url, output_path)
        case 3:
            download_lvideo(video_url, output_path)
