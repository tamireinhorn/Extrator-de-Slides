# Rewriting code for simplicity's sake.
import mimetypes
from tkinter import filedialog as fd
import cv2
from skimage.metrics import structural_similarity
import os 

def receive_input() -> int:
    """Asks the user for the minimal time, in seconds, that makes a slide relevant. Only accepts positive numbers.

    Raises:
        ValueError: If the provided input is not convertible to int.
        ValueError: If the provided input is negative or equal to 0.
    Returns:
        int: The int value in seconds inputed by the user.
    """
    raw_seconds = input("Quanto deve durar um slide (em segundos) para que seja relevante? ")
    try:
        seconds = int(raw_seconds)
    except ValueError:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    if seconds <= 0:
        raise ValueError("Valor inválido. Segundos são um número inteiro maior que 0.")
    return seconds


def choose_video() -> str:
    """Prompts the user with a dialog to choose a file to be processed by the program. Expects a video.

    Raises:
        ValueError: If the file extension is not recognized as a valid video type.

    Returns:
        str: The full path to the file chosen by the user.
    """
    filename: str = fd.askopenfilename(title= 'Escolha um arquivo de vídeo.')  # noqa: E251
    if not os.path.exists(filename):
        raise ValueError('The file does not exist')
    # mypy can't see the library where this is properly defined
    # Verifies for valid video file
    if not mimetypes.guess_type(filename)[0].startswith('video'):  # type: ignore[union-attr]
        raise ValueError("O programa apenas suporta arquivos de vídeo. Escolha um arquivo de vídeo.")
    return filename


def calculate_length_video(video: cv2.VideoCapture) -> int:
    """Calculates the approximate length, in minutes, of a given video file.

    Args:
        video (cv2.VideoCapture): Video file previously chosen by user.

    Returns:
        int: Duration of the video in seconds.
    """
    fps = video.get(cv2.CAP_PROP_FPS)      #
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = int(frame_count / fps)
    return duration


def calculate_iterations(video_length: int, seconds: int) -> int:
    """Calculate the number of loops to be used in the processing of the video.

    Args:
        video_length (int): Size of video in seconds, calculated in calculate_length_video().
        seconds (int): Nunber of seconds, received as input in receive_input().

    Raises:
        ValueError: If the quantity of seconds is superior to the length of the video in itself.

    Returns:
        int: Returns the number of times the processing and comparing of frames will be done.
    """
    if video_length < seconds:
        raise ValueError(f"Você escolheu {seconds} para um slide ser relevante, mas o vídeo dura menos {video_length} segundos")
    return (video_length // seconds) + 1


def image_comparison(imageA: cv2.VideoCapture, imageB: cv2.VideoCapture, threshold: float = 0.9) -> bool:
    """Compares video frames by greyscaling them and then applying the structural similarity algorithm.


    Args:
        imageA (cv2.VideoCapture): First frame for comparison
        imageB (cv2.VideoCapture): Second frame for comparison
        threshold (float, optional): Minimal score to define that images are different. Defaults to 0.9.

    Raises:
        ValueError: If the threshold is outside the range of (0,1). If minimal score is 1, even the same image is different from itself.
        If the minimal score is 0, no image is different enough.

    Returns:
        bool: Returns True if the images are considered to be different.
    """
    if threshold >= 1 or threshold <= 0:
        raise ValueError("A tolerância para similaridade tem que ser um número positivo entre 0 e 1.")
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    score: float = structural_similarity(grayA, grayB)  # The closer to 1 in absolute, the more similar they are. 0.9 is my arbitrary threshold.
    return abs(score) < threshold  # If the similarity is not that close to 1, they're different.
