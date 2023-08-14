import datetime
import time
from django.http import StreamingHttpResponse

from .models import Notification

from django.contrib.auth.models import User


def stream(request):
    def event_stream():
        while True:
            time.sleep(3)
            yield 'data: The server time is: %s\n\n' % datetime.datetime.now()

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

# @login_required
# def stream(request):
#     def event_stream():
#         while True:
#             time.sleep(3)
#             notification = Notification.objects.filter(
#                 sent=False, user=User.objects.get(username='admin')
#             ).first()
#
#             text = ''
#
#             if notification:
#                 text = notification.text
#                 notification.sent = True
#                 notification.save()
#
#             yield 'data: %s\n\n' % text
#
#     return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
