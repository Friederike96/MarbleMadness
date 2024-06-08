import pygame

from functions.frontend.get_font import get_monospaced_font


def calculate_text_size(size: int, text: str) -> tuple[int, int]:
    text_width, text_height = pygame.font.Font(get_monospaced_font(), size=size).size(text)
    return text_width, text_height
