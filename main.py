#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

# KV language string defining the app's UI
KV_STRING = '''
BoxLayout:
    orientation: 'vertical'
    padding: '8dp'

    MDLabel:
        text: "Number of Frames to Capture:"
        halign: 'center'
        theme_text_color: "Secondary"

    MDTextField:
        id: num_frames
        hint_text: "Enter the number of frames"
        helper_text: "Press 'Capture' to start capturing frames"
        helper_text_mode: "on_focus"

    MDRaisedButton:
        text: "Capture"
        on_release: app.capture_frames()
'''

# Function to process a single frame
def process_frame(frame, image_name, sift):
    # Detect and compute SIFT features for the frame
    kp, des = sift.detectAndCompute(frame, None)

    # Take only the first 128 columns of SIFT descriptors
    max_descriptors = 128
    if des is not None and des.shape[1] > max_descriptors:
        des = des[:, :max_descriptors]

    # Compute the average value for each column of SIFT descriptors
    average_values = des.mean(axis=0) if des is not None else [0] * max_descriptors

    # Create a dictionary to hold the SIFT data for this image
    sift_data_dict = {"Image Name": image_name}

    # Populate the dictionary with SIFT descriptor average values
    for j, avg_value in enumerate(average_values):
        column_name = f"SIFT_{j + 1}"
        sift_data_dict[column_name] = avg_value

    return sift_data_dict

# Create the KivyMD app class
class SiftCaptureApp(MDApp):

    def build(self):
        self.title = "SIFT Descriptor Capture"
        return Builder.load_string(KV_STRING)

    def capture_frames(self):
        num_frames_text = self.root.ids.num_frames.text
        try:
            num_frames = int(num_frames_text)
        except ValueError:
            MDLabel(text="Please enter a valid number of frames.", halign="center").open()
            return

        # Create a folder to save captured images (if it doesn't exist)
        output_folder = 'captured_images'
        os.makedirs(output_folder, exist_ok=True)

        # Initialize video capture from the default camera (usually camera index 0)
        cap = cv2.VideoCapture(0)

        # Initialize SIFT detector
        sift = cv2.SIFT_create()

        # List to hold futures for concurrent processing
        futures = []

        with ThreadPoolExecutor() as executor:
            for i in range(num_frames):
                # Capture a frame from the camera
                ret, frame = cap.read()

                # Generate a unique image name based on the current time
                image_name = f"frame_{i}.jpg"

                # Save the captured frame as an image
                cv2.imwrite(os.path.join(output_folder, image_name), frame)

                # Submit the frame processing task to the thread pool
                futures.append(executor.submit(process_frame, frame.copy(), image_name, sift))

        # Create an empty DataFrame with column names (limited to 128 columns)
        column_names = [f"SIFT_{i + 1}" for i in range(128)]
        sift_data = pd.DataFrame(columns=["Image Name"] + column_names)

        # Retrieve and append the processed data from futures
        for future in futures:
            sift_data = sift_data.append(future.result(), ignore_index=True)

        # Save the SIFT data to an Excel file
        excel_file = 'captured_sift_descriptors_with_avg.xlsx'
        sift_data.to_excel(excel_file, index=False)

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

        MDLabel(text=f"Captured {num_frames} frames. SIFT descriptors and images saved. SIFT data saved to '{excel_file}'. Images saved in '{output_folder}'.",
                halign="center").open()

if __name__ == '__main__':
    SiftCaptureApp().run()


# In[ ]:




