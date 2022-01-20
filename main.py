import os
import datetime
import cv2 as cv
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image


start_time = datetime.datetime.now()

video_file_name = input("Enter the name of the video (with the extension): ")
video_name = video_file_name.split(".")[0]

# make a folder with the name of the video
# if the folder already exists, delete it

if os.path.exists(video_name):
    print("Deleting the folder...")
    os.system("rm -r " + video_name)  # if you are using Windows, use rmdir instead of rm

if not os.path.exists('./output'):
    os.makedirs('./output')

os.mkdir(f'./{video_name}')
os.mkdir(f'./{video_name}/frames')

video_path = f'./input/{video_name}'
frames_path = f'./{video_name}/frames/'

seconds_interval = int(input("Enter the seconds interval: "))
frames_interval = seconds_interval * 30

start_frame = int(input("Enter the start frame: "))

# # # # # # # # #

capture = cv.VideoCapture(f'./input/{video_file_name}')
total_frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))

end_frame = total_frames - frames_interval

prev_frame = None
diff_threshold = (1 - .05)

width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f'Width: {width}')
print(f'Height: {height}')

# if you want to crop the video, enter the coordinates of the top left corner
# and the bottom right corner of the rectangle

res = input('\nDo you want to crop the video? (y/n) ')

top_left_x = 0
top_left_y = 0
bottom_right_x = width
bottom_right_y = height

if res == 'y':
    top_left_x = int(input("Enter the top left x coordinate: "))
    top_left_y = int(input("Enter the top left y coordinate: "))
    bottom_right_x = int(input("Enter the bottom right x coordinate: "))
    bottom_right_y = int(input("Enter the bottom right y coordinate: "))

x1, y1, x2, y2 = top_left_x, top_left_y, bottom_right_x, bottom_right_y

print('Extracting frames...')

for i in range(start_frame, end_frame, frames_interval):
    capture.set(cv.CAP_PROP_POS_FRAMES, i)
    ret, frame = capture.read()

    if ret:
        roi = frame[y1:y2, x1:x2]

        if prev_frame is not None:
            # convert the frames to grayscale
            gray_prev = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
            gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

            # compute the Structural Similarity Index (SSIM) between the two
            # frames
            (score, _) = compare_ssim(gray_roi, gray_prev, full=True)

            # if the frames are not similar enough, the program will
            # capture the frame and save it
            if score < diff_threshold:
                cv.imwrite(frames_path + str(i) + '.jpg', roi)
                # print('Captured frame: ' + str(i))

                prev_frame = roi
        else:
            cv.imwrite(frames_path + str(i) + '.jpg', roi)
            # print('First Frame: ' + str(i) + ' saved')

            prev_frame = roi


# write a pdf file with all the images
images = []
for file in os.listdir(frames_path):
    if file.endswith(".jpg"):
        images.append(Image.open(frames_path + file))

cape = Image.open(f'input/{video_name}_cape.png')

cape.save(
    './output/' + video_name + '.pdf',
    'PDF',
    resolution=100.0,
    save_all=True,
    append_images=images
)

end_time = datetime.datetime.now()

print('Elapsed time: ' + str(end_time - start_time))
