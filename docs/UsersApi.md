# peertube_api_client.UsersApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /api/v1/users | Create a user
[**confirm_two_factor_request**](UsersApi.md#confirm_two_factor_request) | **POST** /api/v1/users/{id}/two-factor/confirm-request | Confirm two factor auth
[**del_user**](UsersApi.md#del_user) | **DELETE** /api/v1/users/{id} | Delete a user
[**disable_two_factor**](UsersApi.md#disable_two_factor) | **POST** /api/v1/users/{id}/two-factor/disable | Disable two factor auth
[**get_user**](UsersApi.md#get_user) | **GET** /api/v1/users/{id} | Get a user
[**get_users**](UsersApi.md#get_users) | **GET** /api/v1/users | List users
[**put_user**](UsersApi.md#put_user) | **PUT** /api/v1/users/{id} | Update a user
[**request_two_factor**](UsersApi.md#request_two_factor) | **POST** /api/v1/users/{id}/two-factor/request | Request two factor auth
[**resend_email_to_verify_user**](UsersApi.md#resend_email_to_verify_user) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
[**verify_user**](UsersApi.md#verify_user) | **POST** /api/v1/users/{id}/verify-email | Verify a user


# **add_user**
> AddUserResponse add_user(add_user)

Create a user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_user import AddUser
from peertube_api_client.models.add_user_response import AddUserResponse
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
    api_instance = peertube_api_client.UsersApi(api_client)
    add_user = peertube_api_client.AddUser() # AddUser | If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first. 

    try:
        # Create a user
        api_response = api_instance.add_user(add_user)
        print("The response of UsersApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->add_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user** | [**AddUser**](AddUser.md)| If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user created |  -  |
**403** | insufficient authority to create an admin or moderator |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_two_factor_request**
> confirm_two_factor_request(id, confirm_two_factor_request_request=confirm_two_factor_request_request)

Confirm two factor auth

Confirm a two factor authentication request

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.confirm_two_factor_request_request import ConfirmTwoFactorRequestRequest
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    confirm_two_factor_request_request = peertube_api_client.ConfirmTwoFactorRequestRequest() # ConfirmTwoFactorRequestRequest |  (optional)

    try:
        # Confirm two factor auth
        api_instance.confirm_two_factor_request(id, confirm_two_factor_request_request=confirm_two_factor_request_request)
    except Exception as e:
        print("Exception when calling UsersApi->confirm_two_factor_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **confirm_two_factor_request_request** | [**ConfirmTwoFactorRequestRequest**](ConfirmTwoFactorRequestRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**403** | invalid request token or OTP token |  -  |
**404** | user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_user**
> del_user(id)

Delete a user

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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id

    try:
        # Delete a user
        api_instance.del_user(id)
    except Exception as e:
        print("Exception when calling UsersApi->del_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 

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
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_two_factor**
> disable_two_factor(id, request_two_factor_request=request_two_factor_request)

Disable two factor auth

Disable two factor authentication of a user

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.request_two_factor_request import RequestTwoFactorRequest
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    request_two_factor_request = peertube_api_client.RequestTwoFactorRequest() # RequestTwoFactorRequest |  (optional)

    try:
        # Disable two factor auth
        api_instance.disable_two_factor(id, request_two_factor_request=request_two_factor_request)
    except Exception as e:
        print("Exception when calling UsersApi->disable_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **request_two_factor_request** | [**RequestTwoFactorRequest**](RequestTwoFactorRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**403** | invalid password |  -  |
**404** | user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUser200Response get_user(id, with_stats=with_stats)

Get a user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_user200_response import GetUser200Response
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    with_stats = True # bool | include statistics about the user (only available as a moderator/admin) (optional)

    try:
        # Get a user
        api_response = api_instance.get_user(id, with_stats=with_stats)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **with_stats** | **bool**| include statistics about the user (only available as a moderator/admin) | [optional] 

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> GetUsers200Response get_users(search=search, blocked=blocked, start=start, count=count, sort=sort)

List users

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_users200_response import GetUsers200Response
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
    api_instance = peertube_api_client.UsersApi(api_client)
    search = 'search_example' # str | Plain text search that will match with user usernames or emails (optional)
    blocked = True # bool | Filter results down to (un)banned users (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort users by criteria (optional)

    try:
        # List users
        api_response = api_instance.get_users(search=search, blocked=blocked, start=start, count=count, sort=sort)
        print("The response of UsersApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Plain text search that will match with user usernames or emails | [optional] 
 **blocked** | **bool**| Filter results down to (un)banned users | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort users by criteria | [optional] 

### Return type

[**GetUsers200Response**](GetUsers200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user**
> put_user(id, update_user)

Update a user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.update_user import UpdateUser
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    update_user = peertube_api_client.UpdateUser() # UpdateUser | 

    try:
        # Update a user
        api_instance.put_user(id, update_user)
    except Exception as e:
        print("Exception when calling UsersApi->put_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **update_user** | [**UpdateUser**](UpdateUser.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_two_factor**
> List[RequestTwoFactorResponse] request_two_factor(id, request_two_factor_request=request_two_factor_request)

Request two factor auth

Request two factor authentication for a user

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.request_two_factor_request import RequestTwoFactorRequest
from peertube_api_client.models.request_two_factor_response import RequestTwoFactorResponse
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    request_two_factor_request = peertube_api_client.RequestTwoFactorRequest() # RequestTwoFactorRequest |  (optional)

    try:
        # Request two factor auth
        api_response = api_instance.request_two_factor(id, request_two_factor_request=request_two_factor_request)
        print("The response of UsersApi->request_two_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->request_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **request_two_factor_request** | [**RequestTwoFactorRequest**](RequestTwoFactorRequest.md)|  | [optional] 

### Return type

[**List[RequestTwoFactorResponse]**](RequestTwoFactorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | invalid password |  -  |
**404** | user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_to_verify_user**
> resend_email_to_verify_user(resend_email_to_verify_user_request=resend_email_to_verify_user_request)

Resend user verification link

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.resend_email_to_verify_user_request import ResendEmailToVerifyUserRequest
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
    api_instance = peertube_api_client.UsersApi(api_client)
    resend_email_to_verify_user_request = peertube_api_client.ResendEmailToVerifyUserRequest() # ResendEmailToVerifyUserRequest |  (optional)

    try:
        # Resend user verification link
        api_instance.resend_email_to_verify_user(resend_email_to_verify_user_request=resend_email_to_verify_user_request)
    except Exception as e:
        print("Exception when calling UsersApi->resend_email_to_verify_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_email_to_verify_user_request** | [**ResendEmailToVerifyUserRequest**](ResendEmailToVerifyUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> verify_user(id, verify_user_request=verify_user_request)

Verify a user

Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.verify_user_request import VerifyUserRequest
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
    api_instance = peertube_api_client.UsersApi(api_client)
    id = 56 # int | Entity id
    verify_user_request = peertube_api_client.VerifyUserRequest() # VerifyUserRequest |  (optional)

    try:
        # Verify a user
        api_instance.verify_user(id, verify_user_request=verify_user_request)
    except Exception as e:
        print("Exception when calling UsersApi->verify_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Entity id | 
 **verify_user_request** | [**VerifyUserRequest**](VerifyUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**403** | invalid verification string |  -  |
**404** | user not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

