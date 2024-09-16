import logging
from django.shortcuts import render
from videotext.forms import TextForm
from videotext.utils import generate_video
import os
from urllib.parse import quote
from django.http import FileResponse, HttpResponse


def video_form(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            try:
                video_path = generate_video(text)
                logging.info(f"Путь к видео: {video_path}")

                if os.path.exists(video_path):
                    file_name = os.path.basename(video_path)
                    safe_filename = quote(file_name)  # Кодируем имя файла для использования в HTTP заголовках
                    response = FileResponse(open(video_path, 'rb'), content_type='video/mp4')
                    response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{safe_filename}'
                    return response
                else:
                    return HttpResponse("Файл не найден", status=404)
            except Exception as e:
                logging.error(f"Ошибка при обработке видео: {str(e)}")
                return HttpResponse(f"Возникла ошибка: {str(e)}", status=500)
    else:
        form = TextForm()
    return render(request, 'videotext/video_form.html', {'form': form})
