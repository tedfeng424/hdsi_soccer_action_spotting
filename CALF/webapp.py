from asyncio import subprocess
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import tempfile
import os
import logging
from datetime import datetime
import time
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import json
import subprocess

#import torch

#from dataset import SoccerNetClipsTesting
#from model import ContextAwareModel
#from train import test



def action_spotting_visualization(file, prediction):
    cap = cv2.VideoCapture(file)
    with open(prediction, "r") as f:
        predictions = json.load(f)
    output_video_path = "output_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_index = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        labeled_frame = frame.copy()
    
        frame_predictions = predictions.get('predictions')
    
        for i in range(len(frame_predictions)):
            if int(frame_index/1000)*1000==int(int(frame_predictions[i]['position'])/1000)*1000:
                label = frame_predictions[i]["label"]
                confidence = frame_predictions[i]["confidence"]

                cv2.putText(labeled_frame, label, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_8)
                cv2.putText(labeled_frame, confidence, (50,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_8)

        out.write(labeled_frame)
    #if cv2.waitKey(1) & 0xFF == ord("q"):
    #    break


    cap.release()
    out.release()

#def predict(video_file):

#    subprocess.run(["python", "inference/main.py", "--video_path="+video_file, "--model_name", "CALF_benchmark"])

def main():
    """Action Spotting WebApp"""


    html_temp = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Action Spotting WebApp</h2>
    </div>
    </body>
    """
    #st.markdown(html_temp, unsafe_allow_html=True)

    st.title("Action Spotting")
    """\n"""


    f = st.file_uploader("Upload Video", type=['mp4'])


    if f is not None:
        st.text("Original Video")
        st.video(f)

        video_file = tempfile.NamedTemporaryFile(delete=False) 
        video_file.write(f.read())


    if st.button("Run prediction"):
        #predict(video_file)
        prediction = 'inference/outputs/'+f.name[:-4]+'_predictions.json'
        print(prediction)
        """Visualizing prediction results..."""
        action_spotting_visualization(video_file.name, prediction)

        """Converting to mp4..."""
        new_name = f.name[:-4]+'_out_put_video_playable.mp4'
        subprocess.run(["ffmpeg" ,"-i" ,"output_video.mp4", "-vcodec", "libx264", new_name])
        video_file = open(new_name, 'rb')

        video_bytes = video_file.read()
        """Succeeded!"""
        st.video(video_bytes)
    
    """Successful prediction demo"""
    video_file = open('good_playable.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    """"""
    video_file2 = open('good_2_playable.mp4', 'rb')
    video_bytes2 = video_file2.read()
    st.video(video_bytes2)
    #st.markdown(html_temp, unsafe_allow_html=True)

    """Failed prediction demo"""
    video_file3 = open('bad_playable.mp4', 'rb')
    video_bytes3 = video_file3.read()
    st.video(video_bytes3)
    """"""
    video_file4 = open('bad_2_playable.mp4', 'rb')
    video_bytes4 = video_file4.read()
    st.video(video_bytes4)
    #st.markdown(html_temp, unsafe_allow_html=True)
       
    


if __name__ == '__main__':
    main()