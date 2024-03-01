from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
            "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
            "It has survived not only five centuries, but also the leap into electronic typesetting, "
            "remaining essentially unchanged.")
    html = f"""
    <h1>Мой первый Django-сайт</h1>
    <p>
        <b>{text}</b>
    </p>
    <br>
    """
    logger.info(f'Была посещена страница {request.path}')
    return HttpResponse(html)


def about(request):
    text = ("It is a long established fact that a reader will be distracted by the readable content of a page when "
            "looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution "
            "of letters, as opposed to using 'Content here, content here', making it look like readable English.")
    html = f"""
    <h1>Обо мне</h1>
    <p>
        <b>{text}</b>
    </p>
    <br>
    """
    logger.info(f'Была посещена страница {request.path}')
    return HttpResponse(html)
