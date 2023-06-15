from video2images import Video2Images
from SoccerNet.utils import getListGames
import os
import shutil



# Extract Frames from video at 2 FPS
split = 'train'
games = getListGames(split)
video_prefix = "/path_to_video/"

for game in games:
    print(game)

    for i in range(2):
        idx = i + 1
        video = video_prefix+game+ "/"+ str(idx)+"_720p.mkv"
        output_path = video_prefix+game+ "/"+ str(idx)+"_720p"
        if os.path.exists(output_path):
            shutil.rmtree(output_path)

        os.mkdir(output_path)

        Video2Images(video_filepath=video,
                     capture_rate=2,
                     out_dir=output_path)