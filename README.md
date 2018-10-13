# Smart-Mirror
This is a system that records video when user face is not in front of the mirror and plays the video when face comes in front of the mirror. This gives the user an experience of an eye on the back of the skull. This helps while shaving or applying makeup.

An option to see the magnified face on a part of the mirror is also added. This helps in examining pimples on the face.

Technology/library used : OpenCV, Haarcascade pretrained classifier for face detection


- shave.py
 run "python shave.py"
 turn your face to left and press "a" 
 then turn your face to right and press "s"
 
 - magnifier.py
  run "python mirror_v2.py"
  magnifier of the mirror is activated
  
 - mirror_v2.py
  run "python mirror_v2.py"
  Each frame is inspected for face in it.
  If a face is found it just shows blank screen. This means you are looking at a mirror because a black surface beneath one-way   mirror will reflect the light. When you turn your face i.e. your face is no more detected by the mirror. It starts recording. When again your face comes in front of the mirror, it plays the recorded video. This way you can see yourself from all side.
