import cv2


def sort_contours(counts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    bounding_boxes = [cv2.boundingRect(c) for c in counts]
    # 用一个最小的矩形，把找到的形状包起来x,y,h,w
    (counts, bounding_boxes) = zip(*sorted(zip(counts, bounding_boxes), key=lambda b: b[1][i], reverse=reverse))

    return counts, bounding_boxes


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resize_ = cv2.resize(image, dim, interpolation=inter)
    return resize_
