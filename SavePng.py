#!/usr/bin/python3

import cv2
import time
from picamera2 import Picamera2, Preview

import os
os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")


picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
config = picam2.create_still_configuration(main={"size": (9152, 6944), "format": "RGB888"}, buffer_count=1)

picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)

picam2.start()
time.sleep(1)
picam2.stop()

picam2.configure(config)
picam2.start()
time.sleep(5)
RGB888 = picam2.capture_array("main")
cv2.imwrite("test.png", RGB888)
