#!/bin/bash

# Paths
CUSTOM_PATHS=("mininet/custom" "pox/pox/misc")

for FOLDER in "${CUSTOM_PATHS[@]}"; do
    # Check the source folders exists and creates destination folder
    if [ ! -d "$FOLDER" ]; then
        echo "Source folder $FOLDER not found."
        exit 1
    fi
    if [ ! -d "/home/mininet/$FOLDER" ]; then
        echo "Creating destination directory /home/mininet/$FOLDER."
        mkdir -p /home/mininet/$FOLDER
    fi

    # Copies folders contents into destination
    echo "Copying ./$FOLDER to /home/mininet/$FOLDER."
    cp -f "./$FOLDER/"* "/home/mininet/$FOLDER"
    
    # Check if the copy was successful
    if [ $? -eq 0 ]; then
        echo "Folder copied successfully."
    else
        echo "Failed to copy the folder."
        exit 1
    fi
done

