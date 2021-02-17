import sys
import io
import argparse
from PIL import Image
import pyocr
import cv2
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main() -> None:
    tools = pyocr.get_available_tools()
    assert(len(tools) != 0)
    tool = tools[0]
    im = Image.open(r'C:\Users\himih\Pictures\10.jpg')
    result = tool.image_to_string(
        im,
        lang='jpn',
        builder=pyocr.builders.LineBoxBuilder(tesseract_layout=6)
    )

    img = cv2.imread(r'C:\Users\himih\Pictures\10.jpg')

    for res in result:
        print(res.position)
        print(res.content)
        upper = res.position[0][1]
        lower = res.position[1][1]
        im_crop = im.crop((0, upper, im.size[0], lower))
        cv2.imshow('', np.asarray(im_crop))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    cv2.imshow('', img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()


if __name__ == '__main__':

    main()