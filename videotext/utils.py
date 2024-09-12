import logging
import re
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
from django.conf import settings

from videotext.models import VideoRequest

logging.basicConfig(level=logging.INFO)


def clear_text(text):
    """Удаляет недопустимые символы из текста для безопасного использования в имени файла."""
    text = re.sub(r'[^\w\s-]', '', text, flags=re.U)
    text = re.sub(r'[\s_]+', '_', text).strip()  # Замена пробелов и подчеркиваний на одно подчеркивание
    return text


def generate_video(text):
    cleared_text = clear_text(text)
    logging.basicConfig(level=logging.INFO)
    try:

        # Форматируем время, например, "20240830_235959"
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Имя файла с таймстампом
        file_name = f'{cleared_text}_{current_time}.mp4'

        file_path = os.path.join(settings.MEDIA_ROOT, 'videos', file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        logging.info(f"Сохранение видео по пути: {file_path}")

        # Параметры видео
        height, width = 100, 100
        fps = 30
        duration = 3
        num_frames = duration * fps

        # Создаем видео
        video = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        # Загружаем шрифт, который поддерживает кириллицу
        font_path = "Rostov.ttf"  # путь к файлу шрифта, размещен в папке с файлом скрипта
        font_size = 24

        # Создание изображения
        image = Image.new('RGB', (200, 100), color='white')
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype(font_path, font_size)

        for i in range(num_frames):
            img = np.zeros((height, width, 3), dtype=np.uint8)
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)

            # Получаем bounding box текста
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x_position = width - i * (width + text_width) // num_frames  # Расчет позиции текста

            draw.text((x_position, (height - text_height) // 2), text, font=font, fill=(255, 255, 255))

            # Конвертируем обратно в формат OpenCV
            img = np.array(img_pil)
            video.write(img)

        video.release()
        logging.info("Видео сформировано успешно и сохранено по пути: {}".format(file_path))

        video_request = VideoRequest(text=text, video_file=file_path)
        video_request.save()

    except Exception as e:
        logging.error("Ошибка при генерации видео: {}".format(e))
        return None

    return file_path
