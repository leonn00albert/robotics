#!/bin/bash

option="$1"

case "$option" in
  "motor")
    echo "Running test motors..."
    python3 /home/leon/robotics/Motor_Driver_HAT_Code/Motor_Driver_HAT_Code/Raspberry\ Pi/python/main.py
    ;;
  *)
    echo "Invalid option. Please provide a valid option."
    ;;
esac
