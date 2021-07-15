from rest_framework.views import exception_handler


def custom_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {
            'success': False,
            'path': context['request'].path,
            'message': response.data['detail'],
            'result': None,
        }

    return response
