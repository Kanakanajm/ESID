# Sample views to try out oauth access token (jwt) validation
# codes are provided by
# https://auth0.com/docs/quickstart/backend/django/interactive#create-the-api-views


from authlib.integrations.django_oauth2 import ResourceProtector
from django.http import JsonResponse
from . import validator
import os

require_auth = ResourceProtector()

# As configured in https://manage.auth0.com/ under Applications>APIs>ESID Backend Auth Test
validator = validator.Auth0JWTBearerTokenValidator(
    os.getenv('OAUTH_DOMAIN'),
    os.getenv('OAUTH_AUDIENCE'),
)
require_auth.register_token_validator(validator)


def public(request):
    """No access token required to access this route
    """
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return JsonResponse(dict(message=response))


@require_auth(None)
def private(request):
    """A valid access token is required to access this route
    """
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return JsonResponse(dict(message=response))


@require_auth("read:admin-messages")
def private_scoped(request):
    """A valid access token and an appropriate scope are required to access this route
    """
    response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:admin-messages to see this."
    return JsonResponse(dict(message=response))