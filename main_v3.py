from importlib.resources import path
from re import X
import numpy as np
import random as rnd
import cv2


#width = 1920
#height = 1080
ids = np.linspace(1,500, num=500)


def generate_patches(sum, height, width):
    patch_height = int(height/sum)
    patch_width = int(width/sum)

    # TUPLE - x_min, y_min, x_max, y_max
    patches = []
    for i in range(sum):
        if i == 0:
            print("pass")
            pass
        elif i == sum:
            print("break")
            break
        else:
            x_min = i*patch_height
            x_max = (i+1)*patch_height
            for j in range(sum):
                y_min = j*patch_width
                y_max = (j+1)*patch_width
                patches.append((x_min, y_min, x_max, y_max))
    print(len(patches))
    return patches


def generate_positions(sum, patches):
    #generate_patch size
    coordinates = []
    rnd.shuffle(patches)
    for i in range(sum):
        patch = patches[i]
        x = int((patch[0] + patch[2])/2)
        y = int((patch[1] + patch[3])/2)
        #x = rnd.randint(patch[0], patch[2])
        #y = rnd.randint(patch[1], patch[3])
        coordinates.append((x,y))
    return coordinates


def draw_image(coordinates, img):
    rnd.shuffle(ids)
    for (coordinate, id) in zip(coordinates, ids):
        cv2.putText(img, str(int(id)), (coordinate[1], coordinate[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (125,125,255), 1, cv2.LINE_AA, False)
    cv2.imshow("guide", img)
    cv2.waitKey()


if __name__=="__main__":
    img = cv2.imread("/home/daniel/generate_image_guide/conveyor_belt.jpg")
    sum = rnd.randint(3,15)
    #sum = 4
    print(sum)
    patches = generate_patches(sum, img.shape[0], img.shape[1])
    coordinates = generate_positions(sum, patches)
    draw_image(coordinates, img)

