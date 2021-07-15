from rest_framework.renderers import JSONRenderer


class APIRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'success': data.get('success', True),
            'path': renderer_context['request'].path,
            'message': data.get('message', None),
            'result': data.get('result', None),
        }
        return super(APIRenderer, self).render(response, accepted_media_type, renderer_context)
