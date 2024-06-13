import rembg
import numpy as np
from loguru import logger

class BackgroundRemover:
    def __init__(self) -> None:
        logger.info("Initialized BackgroundRemover")
        
    def remove(self, img: np.ndarray) -> np.ndarray:
        """
        For a given image return the new image with white background
        """
        return rembg.remove(img, bgcolor=(255, 255, 255, 255))
