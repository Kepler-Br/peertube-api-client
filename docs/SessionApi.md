# peertube_api_client.SessionApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_o_auth_client**](SessionApi.md#get_o_auth_client) | **GET** /api/v1/oauth-clients/local | Login prerequisite
[**get_o_auth_token**](SessionApi.md#get_o_auth_token) | **POST** /api/v1/users/token | Login
[**revoke_o_auth_token**](SessionApi.md#revoke_o_auth_token) | **POST** /api/v1/users/revoke-token | Logout


# **get_o_auth_client**
> OAuthClient get_o_auth_client()

Login prerequisite

You need to retrieve a client id and secret before [logging in](#operation/getOAuthToken).

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.o_auth_client import OAuthClient
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.SessionApi(api_client)

    try:
        # Login prerequisite
        api_response = api_instance.get_o_auth_client()
        print("The response of SessionApi->get_o_auth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_o_auth_client: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_token**
> GetOAuthToken200Response get_o_auth_token(client_id, client_secret, grant_type, username, password, refresh_token)

Login

With your [client id and secret](#operation/getOAuthClient), you can retrieve an access and refresh tokens.

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_o_auth_token200_response import GetOAuthToken200Response
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.SessionApi(api_client)
    client_id = 'client_id_example' # str | 
    client_secret = 'client_secret_example' # str | 
    grant_type = 'password' # str |  (default to 'password')
    username = 'username_example' # str | immutable name of the user, used to find or mention its actor
    password = 'password_example' # str | 
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Login
        api_response = api_instance.get_o_auth_token(client_id, client_secret, grant_type, username, password, refresh_token)
        print("The response of SessionApi->get_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_o_auth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **client_secret** | **str**|  | 
 **grant_type** | **str**|  | [default to &#39;password&#39;]
 **username** | **str**| immutable name of the user, used to find or mention its actor | 
 **password** | **str**|  | 
 **refresh_token** | **str**|  | 

### Return type

[**GetOAuthToken200Response**](GetOAuthToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Disambiguate via &#x60;type&#x60;: - &#x60;invalid_client&#x60; for an unmatched &#x60;client_id&#x60; - &#x60;invalid_grant&#x60; for unmatched credentials  |  -  |
**401** | Disambiguate via &#x60;type&#x60;: - default value for a regular authentication failure - &#x60;invalid_token&#x60; for an expired token  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_o_auth_token**
> revoke_o_auth_token()

Logout

Revokes your access token and its associated refresh token, destroying your current session.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.SessionApi(api_client)

    try:
        # Logout
        api_instance.revoke_o_auth_token()
    except Exception as e:
        print("Exception when calling SessionApi->revoke_o_auth_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

