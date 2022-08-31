from re import X
import numpy as np
import random as rnd
import cv2

#width = 1920
#height = 1080
ids = np.linspace(1,500, num=500)


def generate_positions(sum, height, width):
    X = np.rint(np.random.randint(height, size=sum))
    print(X)
    Y = np.rint(np.random.randint(width, size=sum))
    print(Y)
    coordinates= []
    for (x,y) in zip(X,Y):
        coordinates.append((x,y))
    print(coordinates)
    return coordinates

def draw_image(coordinates, img):
    rnd.shuffle(ids)
    for (coordinate, id) in zip(coordinates, ids):
        cv2.putText(img, str(int(id)), (int(coordinate[0]), int(coordinate[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA, False)
    cv2.imshow("guide", img)
    cv2.waitKey()


if __name__=="__main__":
    img = cv2.imread("/home/daniel/generate_image_guide/conveyor_belt.jpg")
    sum = rnd.randint(3,15)
    print(sum)
    coordinates = generate_positions(sum, img.shape[0], img.shape[1])
    draw_image(coordinates, img)

