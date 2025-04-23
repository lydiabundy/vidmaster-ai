# ai_style_transfer.py

import moviepy.editor as mp
from scenedetect import VideoManager, SceneManager
from scenedetect.dectectors import ContentDetector
import os
import uuid

def detect_scenes(video_path):
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.set_downscale_factor()


    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()

    # return tiemcode cut points
    return [scene[0].get_seconds() for scene in scene_list]
def match_cut_timing(reference_vido_path, raw_vidoe_path, output_path):
    # Detect scenes in the refrence and raw videos
    refrence_cuts = detect_scenes(refrence_video_path)
    raw_video = mp.VideoFileClip(raw_video_path)

    #Get the average scne length from the refrence video
    cut_intervals = [j - i for i, j in zip(refrence_cuts[:-1], refrence_cuts[1:])]
    avg_scene_length = sum(cut_intervals) / len(cut_intervals)


    # Trim raw footage into clips based on refrence pacing
    edited_clips = []
    t = 0
    while t < raw_video.duration:
        end = min(t + avg_scene_length, raw_video.duration)
        edited_clips.append(raw_video.subclip(t, end))
        t = end
        
        final = mp.concatenate_vidoeclips(edited_clips)
        final.write_videofile(output_path)

        return output_path
    
    # Example usage ( to test locally)
    # match_cut_timing("refence.mp4", "raw.mp4", "output_edited.mp4")



