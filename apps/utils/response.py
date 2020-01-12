from rest_framework.response import Response
from django.utils import six
from .constant import CODE_SUCCESS, MSG_SUCCESS
from rest_framework import status
from rest_framework.serializers import Serializer


class BaseResponse(Response):
    def __init__(self, code=CODE_SUCCESS, msg=MSG_SUCCESS, success=False, data={}, status=status.HTTP_200_OK,
                 template_name=None, headers=None, exception=False, content_type='application/json'):
        super(Response, self).__init__(None, status=status)
        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)
        self._code = code
        self._message = msg
        self._success = success
        self._data = data

        self.data = {"code": code, "message": msg,
                     success: success, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
