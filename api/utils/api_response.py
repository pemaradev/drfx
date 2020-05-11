from rest_framework.views import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
import logging

def api_response_handler(exc, context):
  # Call REST framework's default exception handler first,
  # to get the standard error response.
  response = exception_handler(exc, context)
  # Now add the HTTP status code to the response.
  if response is not None:
    logging.exception('Uncaught Exception', exc_info=exc)
    response.status_code    = response.status_code
    response.data['status'] = response.status_code
    response.data['code']   = response.status_text
    
    if 'detail' in response.data:
      response.data['error']  = response.data['detail']
      del response.data['detail']
    
    if 'errors' in response.data:
      # Significa que hay errores al procesar el modelo de datos
      response.data['status'] = status.HTTP_422_UNPROCESSABLE_ENTITY
      response.data['code']   = 'UNPROCESSABLE_ENTITY'
      details = response.data['errors']
      for key in details:
        details[key] = details[key][0]
      response.status_code = 422
      response.data['errors'] = details
    
    # response.content_type = 'application/json'
  return response
