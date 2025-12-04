import streamlit as st
import os
import time
from PIL import Image
import glob

def main():
    st.title("Advent of Code 2025 - Day 4 Image Player")
    
    # Path to the outputs folder
    outputs_path = "/Users/jeremy.nadal/repos/perso/adventofcode/adventofcode2025/outputs/"
    
    # Get all image files from the outputs folder
    image_extensions = ["*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"]
    image_files = []
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join(outputs_path, extension)))
    

    image_files.sort()  # Sort files for consistent order
    image_files = [f for f in image_files if "REAL" not in f]
    
    if not image_files:
        st.error(f"No images found in {outputs_path}")
        return
    
    st.write(f"Found {len(image_files)} images")
    
    # Controls
    col1, col2, col3 = st.columns(3)
    with col1:
        play = st.button("Play")
    with col2:
        stop = st.button("Stop")
    with col3:
        interval = st.slider("Interval (seconds)", 0.1, 5.0, 1.0, 0.1)
    
    # Image display container
    image_container = st.empty()
    
    # Initialize session state
    if 'playing' not in st.session_state:
        st.session_state.playing = False
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    
    # Control logic
    if play:
        st.session_state.playing = True
    if stop:
        st.session_state.playing = False
    
    # Display images
    if st.session_state.playing:
        for i in range(len(image_files)):
            if not st.session_state.playing:
                break
            
            try:
                image = Image.open(image_files[i])
                image_container.image(image, caption=f"Frame {i+1}/{len(image_files)}: {os.path.basename(image_files[i])}")
                time.sleep(interval)
            except Exception as e:
                st.error(f"Error loading image {image_files[i]}: {e}")
    else:
        # Show first image when stopped
        if image_files:
            try:
                image = Image.open(image_files[0])
                image_container.image(image, caption=f"Frame 1/{len(image_files)}: {os.path.basename(image_files[0])}")
            except Exception as e:
                st.error(f"Error loading image: {e}")

if __name__ == "__main__":
    main()