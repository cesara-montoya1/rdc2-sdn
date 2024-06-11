#!/bin/bash

# Variables
REPO_PATH="."
MININET_CUSTOM_FOLDER="mininet/custom"
DEST_PATH="/home/mininet/$MININET_CUSTOM_FOLDER"

# Check if the source folder exists
if [ ! -d "$REPO_PATH/$MININET_CUSTOM_FOLDER" ]; then
    echo "Source folder $REPO_PATH/$MININET_CUSTOM_FOLDER does not exist."
    exit 1
fi

# Create the destination directory if it doesn't exist
if [ ! -d "$DEST_PATH" ]; then
    echo "Creating destination directory $DEST_PATH."
    mkdir -p "$DEST_PATH"
fi

# Copy the custom folder
echo "Copying $REPO_PATH/$MININET_CUSTOM_FOLDER to $DEST_PATH."
cp -r "$REPO_PATH/$MININET_CUSTOM_FOLDER/"* "$DEST_PATH/"

# Check if the copy was successful
if [ $? -eq 0 ]; then
    echo "Folder copied successfully."
else
    echo "Failed to copy the folder."
    exit 1
fi

