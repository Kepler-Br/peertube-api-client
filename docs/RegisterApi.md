# peertube_api_client.RegisterApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_registration**](RegisterApi.md#accept_registration) | **POST** /api/v1/users/registrations/{registrationId}/accept | Accept registration
[**delete_registration**](RegisterApi.md#delete_registration) | **DELETE** /api/v1/users/registrations/{registrationId} | Delete registration
[**list_registrations**](RegisterApi.md#list_registrations) | **GET** /api/v1/users/registrations | List registrations
[**register_user**](RegisterApi.md#register_user) | **POST** /api/v1/users/register | Register a user
[**reject_registration**](RegisterApi.md#reject_registration) | **POST** /api/v1/users/registrations/{registrationId}/reject | Reject registration
[**request_registration**](RegisterApi.md#request_registration) | **POST** /api/v1/users/registrations/request | Request registration
[**resend_email_to_verify_registration**](RegisterApi.md#resend_email_to_verify_registration) | **POST** /api/v1/users/registrations/ask-send-verify-email | Resend verification link to registration email
[**resend_email_to_verify_user**](RegisterApi.md#resend_email_to_verify_user) | **POST** /api/v1/users/ask-send-verify-email | Resend user verification link
[**verify_registration_email**](RegisterApi.md#verify_registration_email) | **POST** /api/v1/users/registrations/{registrationId}/verify-email | Verify a registration email
[**verify_user**](RegisterApi.md#verify_user) | **POST** /api/v1/users/{id}/verify-email | Verify a user


# **accept_registration**
> accept_registration(registration_id, user_registration_accept_or_reject=user_registration_accept_or_reject)

Accept registration

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user_registration_accept_or_reject import UserRegistrationAcceptOrReject
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    registration_id = 56 # int | Registration ID
    user_registration_accept_or_reject = peertube_api_client.UserRegistrationAcceptOrReject() # UserRegistrationAcceptOrReject |  (optional)

    try:
        # Accept registration
        api_instance.accept_registration(registration_id, user_registration_accept_or_reject=user_registration_accept_or_reject)
    except Exception as e:
        print("Exception when calling RegisterApi->accept_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **int**| Registration ID | 
 **user_registration_accept_or_reject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] 

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

# **delete_registration**
> delete_registration(registration_id)

Delete registration

Delete the registration entry. It will not remove the user associated with this registration (if any)

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
    api_instance = peertube_api_client.RegisterApi(api_client)
    registration_id = 56 # int | Registration ID

    try:
        # Delete registration
        api_instance.delete_registration(registration_id)
    except Exception as e:
        print("Exception when calling RegisterApi->delete_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **int**| Registration ID | 

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

# **list_registrations**
> ListRegistrations200Response list_registrations(start=start, count=count, search=search, sort=sort)

List registrations

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.list_registrations200_response import ListRegistrations200Response
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    search = 'search_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)

    try:
        # List registrations
        api_response = api_instance.list_registrations(start=start, count=count, search=search, sort=sort)
        print("The response of RegisterApi->list_registrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegisterApi->list_registrations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **search** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**ListRegistrations200Response**](ListRegistrations200Response.md)

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

# **register_user**
> register_user(register_user)

Register a user

Signup has to be enabled and signup approval is not required

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.register_user import RegisterUser
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    register_user = peertube_api_client.RegisterUser() # RegisterUser | 

    try:
        # Register a user
        api_instance.register_user(register_user)
    except Exception as e:
        print("Exception when calling RegisterApi->register_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user** | [**RegisterUser**](RegisterUser.md)|  | 

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
**400** | request error |  -  |
**403** | user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin |  -  |
**409** | a user with this username, channel name or email already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_registration**
> reject_registration(registration_id, user_registration_accept_or_reject=user_registration_accept_or_reject)

Reject registration

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user_registration_accept_or_reject import UserRegistrationAcceptOrReject
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    registration_id = 56 # int | Registration ID
    user_registration_accept_or_reject = peertube_api_client.UserRegistrationAcceptOrReject() # UserRegistrationAcceptOrReject |  (optional)

    try:
        # Reject registration
        api_instance.reject_registration(registration_id, user_registration_accept_or_reject=user_registration_accept_or_reject)
    except Exception as e:
        print("Exception when calling RegisterApi->reject_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **int**| Registration ID | 
 **user_registration_accept_or_reject** | [**UserRegistrationAcceptOrReject**](UserRegistrationAcceptOrReject.md)|  | [optional] 

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

# **request_registration**
> UserRegistration request_registration(user_registration_request=user_registration_request)

Request registration

Signup has to be enabled and require approval on the instance

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user_registration import UserRegistration
from peertube_api_client.models.user_registration_request import UserRegistrationRequest
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    user_registration_request = peertube_api_client.UserRegistrationRequest() # UserRegistrationRequest |  (optional)

    try:
        # Request registration
        api_response = api_instance.request_registration(user_registration_request=user_registration_request)
        print("The response of RegisterApi->request_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegisterApi->request_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_registration_request** | [**UserRegistrationRequest**](UserRegistrationRequest.md)|  | [optional] 

### Return type

[**UserRegistration**](UserRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | request error or signup approval is not enabled on the instance |  -  |
**403** | user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin |  -  |
**409** | a user or registration with this username, channel name or email already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_to_verify_registration**
> resend_email_to_verify_registration(resend_email_to_verify_registration_request=resend_email_to_verify_registration_request)

Resend verification link to registration email

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.resend_email_to_verify_registration_request import ResendEmailToVerifyRegistrationRequest
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    resend_email_to_verify_registration_request = peertube_api_client.ResendEmailToVerifyRegistrationRequest() # ResendEmailToVerifyRegistrationRequest |  (optional)

    try:
        # Resend verification link to registration email
        api_instance.resend_email_to_verify_registration(resend_email_to_verify_registration_request=resend_email_to_verify_registration_request)
    except Exception as e:
        print("Exception when calling RegisterApi->resend_email_to_verify_registration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_email_to_verify_registration_request** | [**ResendEmailToVerifyRegistrationRequest**](ResendEmailToVerifyRegistrationRequest.md)|  | [optional] 

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
    api_instance = peertube_api_client.RegisterApi(api_client)
    resend_email_to_verify_user_request = peertube_api_client.ResendEmailToVerifyUserRequest() # ResendEmailToVerifyUserRequest |  (optional)

    try:
        # Resend user verification link
        api_instance.resend_email_to_verify_user(resend_email_to_verify_user_request=resend_email_to_verify_user_request)
    except Exception as e:
        print("Exception when calling RegisterApi->resend_email_to_verify_user: %s\n" % e)
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

# **verify_registration_email**
> verify_registration_email(registration_id, verify_registration_email_request=verify_registration_email_request)

Verify a registration email

Following a user registration request, the user will receive an email asking to click a link containing a secret. 

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.verify_registration_email_request import VerifyRegistrationEmailRequest
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
    api_instance = peertube_api_client.RegisterApi(api_client)
    registration_id = 56 # int | Registration ID
    verify_registration_email_request = peertube_api_client.VerifyRegistrationEmailRequest() # VerifyRegistrationEmailRequest |  (optional)

    try:
        # Verify a registration email
        api_instance.verify_registration_email(registration_id, verify_registration_email_request=verify_registration_email_request)
    except Exception as e:
        print("Exception when calling RegisterApi->verify_registration_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **int**| Registration ID | 
 **verify_registration_email_request** | [**VerifyRegistrationEmailRequest**](VerifyRegistrationEmailRequest.md)|  | [optional] 

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
**404** | registration not found |  -  |

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
    api_instance = peertube_api_client.RegisterApi(api_client)
    id = 56 # int | Entity id
    verify_user_request = peertube_api_client.VerifyUserRequest() # VerifyUserRequest |  (optional)

    try:
        # Verify a user
        api_instance.verify_user(id, verify_user_request=verify_user_request)
    except Exception as e:
        print("Exception when calling RegisterApi->verify_user: %s\n" % e)
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

