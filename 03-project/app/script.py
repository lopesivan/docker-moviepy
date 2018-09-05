from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
import numpy as np

# animating image
img_character_doctor = '/code/app/media/hair_loss/png/doctor_1-01.png'
img_comment_box = '/code/app/media/hair_loss/png/comment.png'
text_comment = 'Hello Doctor'
video_size = (600,600)

# SLIDE FUNCTIONS
# slides from right to left
def arrive(screenpos,i):
    v = np.array([-1,0])
    print(v)
    d = lambda t : max(0, 3-3*t)
    print(d)
    return lambda t: screenpos-400*v*d(t-0.2*i)

# slides from left to right
def arrive_opposite(screenpos,i):
    v = np.array([-1,0])
    d = lambda t : max(0, 3-3*t)
    return lambda t: screenpos+400*v*d(t-0.2*i)

# empty video
videoMain = ColorClip(video_size, duration=3)

# character 1: doctor
clipImgCharacterDoctor = ImageClip(img_character_doctor)
# comment box
clipImgCommentBox = ImageClip(img_comment_box)
# comment text
txtClipCommentText = TextClip(text_comment, color='red', font='Amiri-Bold', kerning=5, fontsize=60)

# PREPARING CLIP ANIMATIONS
# animate doctor character clip
animate_clipImgCharacterDoctor = (clipImgCharacterDoctor.set_position(arrive_opposite(5,5), 0).set_duration(5))
animate_clipImgCharacterDoctor.fps = 24
# animate comment box
animate_clipImgCommentBox = (clipImgCommentBox.set_position(arrive(200,0), 0).set_duration(3).set_start(2))
animate_clipImgCommentBox.fps = 24
# animate text
animate_txtClipCommentText = (txtClipCommentText.set_position(arrive(100, 0),0).set_duration(2).set_start(3))
# animate_txtClipCommentText = (txtClipCommentText.set_pos(arrive(350,2), 0).set_duration(2).set_start(3))

output_clip = CompositeVideoClip([
    animate_clipImgCharacterDoctor,
    animate_clipImgCommentBox,
    animate_txtClipCommentText
])
output_clip.fps = 24

output_clip.write_videofile('/code/app/animate_doctor.avi', fps=24, codec='mpeg4')
#output_clip.ipython_display(width=500)
