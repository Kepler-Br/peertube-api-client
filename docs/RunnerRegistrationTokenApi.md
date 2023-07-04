# peertube_api_client.RunnerRegistrationTokenApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_runners_registration_tokens_generate_post**](RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_generate_post) | **POST** /api/v1/runners/registration-tokens/generate | Generate registration token
[**api_v1_runners_registration_tokens_get**](RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_get) | **GET** /api/v1/runners/registration-tokens | List registration tokens
[**api_v1_runners_registration_tokens_registration_token_id_delete**](RunnerRegistrationTokenApi.md#api_v1_runners_registration_tokens_registration_token_id_delete) | **DELETE** /api/v1/runners/registration-tokens/{registrationTokenId} | Remove registration token


# **api_v1_runners_registration_tokens_generate_post**
> api_v1_runners_registration_tokens_generate_post()

Generate registration token

Generate a new runner registration token

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
    api_instance = peertube_api_client.RunnerRegistrationTokenApi(api_client)

    try:
        # Generate registration token
        api_instance.api_v1_runners_registration_tokens_generate_post()
    except Exception as e:
        print("Exception when calling RunnerRegistrationTokenApi->api_v1_runners_registration_tokens_generate_post: %s\n" % e)
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
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_runners_registration_tokens_get**
> ApiV1RunnersRegistrationTokensGet200Response api_v1_runners_registration_tokens_get(start=start, count=count, sort=sort)

List registration tokens

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_registration_tokens_get200_response import ApiV1RunnersRegistrationTokensGet200Response
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
    api_instance = peertube_api_client.RunnerRegistrationTokenApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort registration tokens by criteria (optional)

    try:
        # List registration tokens
        api_response = api_instance.api_v1_runners_registration_tokens_get(start=start, count=count, sort=sort)
        print("The response of RunnerRegistrationTokenApi->api_v1_runners_registration_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerRegistrationTokenApi->api_v1_runners_registration_tokens_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort registration tokens by criteria | [optional] 

### Return type

[**ApiV1RunnersRegistrationTokensGet200Response**](ApiV1RunnersRegistrationTokensGet200Response.md)

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

# **api_v1_runners_registration_tokens_registration_token_id_delete**
> api_v1_runners_registration_tokens_registration_token_id_delete(registration_token_id)

Remove registration token

Remove a registration token. Runners that used this token for their registration are automatically removed.

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
    api_instance = peertube_api_client.RunnerRegistrationTokenApi(api_client)
    registration_token_id = 56 # int | 

    try:
        # Remove registration token
        api_instance.api_v1_runners_registration_tokens_registration_token_id_delete(registration_token_id)
    except Exception as e:
        print("Exception when calling RunnerRegistrationTokenApi->api_v1_runners_registration_tokens_registration_token_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_token_id** | **int**|  | 

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

