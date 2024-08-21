import cv2


def convert_to_gray(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Fixed COLOR_BGB2GRAY to COLOR_BGR2GRAY
    return gray


if __name__ == '__main__':
    img_path = "./test_img_bgr.png"  # Fixed '==' to '=' for assignment

    img = cv2.imread(img_path)

    if img is not None:  # Added check to ensure image is loaded
        img_gray = convert_to_gray(img)
        cv2.imwrite("./test_img_gray.png", img_gray)
    else:
        print("Error: Image not found.")