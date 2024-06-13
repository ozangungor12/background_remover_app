import cv2
from modules.bg_remover import BackgroundRemover

if __name__ == "__main__":
    img = cv2.imread("assets/ship.jpg")
    bg_remover = BackgroundRemover()
    result = bg_remover.remove(img)
    cv2.imwrite("assets/ship_result.jpg", result)
    

