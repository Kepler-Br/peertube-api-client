# peertube_api_client.RunnerJobsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_runners_jobs_get**](RunnerJobsApi.md#api_v1_runners_jobs_get) | **GET** /api/v1/runners/jobs | List jobs
[**api_v1_runners_jobs_job_uuid_abort_post**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_abort_post) | **POST** /api/v1/runners/jobs/{jobUUID}/abort | Abort job
[**api_v1_runners_jobs_job_uuid_accept_post**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_accept_post) | **POST** /api/v1/runners/jobs/{jobUUID}/accept | Accept job
[**api_v1_runners_jobs_job_uuid_cancel_get**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_cancel_get) | **GET** /api/v1/runners/jobs/{jobUUID}/cancel | Cancel a job
[**api_v1_runners_jobs_job_uuid_error_post**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_error_post) | **POST** /api/v1/runners/jobs/{jobUUID}/error | Post job error
[**api_v1_runners_jobs_job_uuid_success_post**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_success_post) | **POST** /api/v1/runners/jobs/{jobUUID}/success | Post job success
[**api_v1_runners_jobs_job_uuid_update_post**](RunnerJobsApi.md#api_v1_runners_jobs_job_uuid_update_post) | **POST** /api/v1/runners/jobs/{jobUUID}/update | Update job
[**api_v1_runners_jobs_request_post**](RunnerJobsApi.md#api_v1_runners_jobs_request_post) | **POST** /api/v1/runners/jobs/request | Request a new job


# **api_v1_runners_jobs_get**
> ApiV1RunnersJobsGet200Response api_v1_runners_jobs_get(start=start, count=count, sort=sort, search=search)

List jobs

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_get200_response import ApiV1RunnersJobsGet200Response
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort runner jobs by criteria (optional)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)

    try:
        # List jobs
        api_response = api_instance.api_v1_runners_jobs_get(start=start, count=count, sort=sort, search=search)
        print("The response of RunnerJobsApi->api_v1_runners_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort runner jobs by criteria | [optional] 
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**ApiV1RunnersJobsGet200Response**](ApiV1RunnersJobsGet200Response.md)

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

# **api_v1_runners_jobs_job_uuid_abort_post**
> api_v1_runners_jobs_job_uuid_abort_post(job_uuid, api_v1_runners_jobs_job_uuid_abort_post_request=api_v1_runners_jobs_job_uuid_abort_post_request)

Abort job

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_abort_post_request import ApiV1RunnersJobsJobUUIDAbortPostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 
    api_v1_runners_jobs_job_uuid_abort_post_request = peertube_api_client.ApiV1RunnersJobsJobUUIDAbortPostRequest() # ApiV1RunnersJobsJobUUIDAbortPostRequest |  (optional)

    try:
        # Abort job
        api_instance.api_v1_runners_jobs_job_uuid_abort_post(job_uuid, api_v1_runners_jobs_job_uuid_abort_post_request=api_v1_runners_jobs_job_uuid_abort_post_request)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_abort_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 
 **api_v1_runners_jobs_job_uuid_abort_post_request** | [**ApiV1RunnersJobsJobUUIDAbortPostRequest**](ApiV1RunnersJobsJobUUIDAbortPostRequest.md)|  | [optional] 

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

# **api_v1_runners_jobs_job_uuid_accept_post**
> ApiV1RunnersJobsJobUUIDAcceptPost200Response api_v1_runners_jobs_job_uuid_accept_post(job_uuid, api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)

Accept job

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_accept_post200_response import ApiV1RunnersJobsJobUUIDAcceptPost200Response
from peertube_api_client.models.api_v1_runners_unregister_post_request import ApiV1RunnersUnregisterPostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 
    api_v1_runners_unregister_post_request = peertube_api_client.ApiV1RunnersUnregisterPostRequest() # ApiV1RunnersUnregisterPostRequest |  (optional)

    try:
        # Accept job
        api_response = api_instance.api_v1_runners_jobs_job_uuid_accept_post(job_uuid, api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)
        print("The response of RunnerJobsApi->api_v1_runners_jobs_job_uuid_accept_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_accept_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 
 **api_v1_runners_unregister_post_request** | [**ApiV1RunnersUnregisterPostRequest**](ApiV1RunnersUnregisterPostRequest.md)|  | [optional] 

### Return type

[**ApiV1RunnersJobsJobUUIDAcceptPost200Response**](ApiV1RunnersJobsJobUUIDAcceptPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_runners_jobs_job_uuid_cancel_get**
> api_v1_runners_jobs_job_uuid_cancel_get(job_uuid)

Cancel a job

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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 

    try:
        # Cancel a job
        api_instance.api_v1_runners_jobs_job_uuid_cancel_get(job_uuid)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_cancel_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 

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

# **api_v1_runners_jobs_job_uuid_error_post**
> api_v1_runners_jobs_job_uuid_error_post(job_uuid, api_v1_runners_jobs_job_uuid_error_post_request=api_v1_runners_jobs_job_uuid_error_post_request)

Post job error

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_error_post_request import ApiV1RunnersJobsJobUUIDErrorPostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 
    api_v1_runners_jobs_job_uuid_error_post_request = peertube_api_client.ApiV1RunnersJobsJobUUIDErrorPostRequest() # ApiV1RunnersJobsJobUUIDErrorPostRequest |  (optional)

    try:
        # Post job error
        api_instance.api_v1_runners_jobs_job_uuid_error_post(job_uuid, api_v1_runners_jobs_job_uuid_error_post_request=api_v1_runners_jobs_job_uuid_error_post_request)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_error_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 
 **api_v1_runners_jobs_job_uuid_error_post_request** | [**ApiV1RunnersJobsJobUUIDErrorPostRequest**](ApiV1RunnersJobsJobUUIDErrorPostRequest.md)|  | [optional] 

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

# **api_v1_runners_jobs_job_uuid_success_post**
> api_v1_runners_jobs_job_uuid_success_post(job_uuid, api_v1_runners_jobs_job_uuid_success_post_request=api_v1_runners_jobs_job_uuid_success_post_request)

Post job success

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_success_post_request import ApiV1RunnersJobsJobUUIDSuccessPostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 
    api_v1_runners_jobs_job_uuid_success_post_request = peertube_api_client.ApiV1RunnersJobsJobUUIDSuccessPostRequest() # ApiV1RunnersJobsJobUUIDSuccessPostRequest |  (optional)

    try:
        # Post job success
        api_instance.api_v1_runners_jobs_job_uuid_success_post(job_uuid, api_v1_runners_jobs_job_uuid_success_post_request=api_v1_runners_jobs_job_uuid_success_post_request)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_success_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 
 **api_v1_runners_jobs_job_uuid_success_post_request** | [**ApiV1RunnersJobsJobUUIDSuccessPostRequest**](ApiV1RunnersJobsJobUUIDSuccessPostRequest.md)|  | [optional] 

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

# **api_v1_runners_jobs_job_uuid_update_post**
> api_v1_runners_jobs_job_uuid_update_post(job_uuid, api_v1_runners_jobs_job_uuid_update_post_request=api_v1_runners_jobs_job_uuid_update_post_request)

Update job

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_job_uuid_update_post_request import ApiV1RunnersJobsJobUUIDUpdatePostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    job_uuid = 'job_uuid_example' # str | 
    api_v1_runners_jobs_job_uuid_update_post_request = peertube_api_client.ApiV1RunnersJobsJobUUIDUpdatePostRequest() # ApiV1RunnersJobsJobUUIDUpdatePostRequest |  (optional)

    try:
        # Update job
        api_instance.api_v1_runners_jobs_job_uuid_update_post(job_uuid, api_v1_runners_jobs_job_uuid_update_post_request=api_v1_runners_jobs_job_uuid_update_post_request)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_job_uuid_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uuid** | **str**|  | 
 **api_v1_runners_jobs_job_uuid_update_post_request** | [**ApiV1RunnersJobsJobUUIDUpdatePostRequest**](ApiV1RunnersJobsJobUUIDUpdatePostRequest.md)|  | [optional] 

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

# **api_v1_runners_jobs_request_post**
> ApiV1RunnersJobsRequestPost200Response api_v1_runners_jobs_request_post(api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)

Request a new job

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_jobs_request_post200_response import ApiV1RunnersJobsRequestPost200Response
from peertube_api_client.models.api_v1_runners_unregister_post_request import ApiV1RunnersUnregisterPostRequest
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
    api_instance = peertube_api_client.RunnerJobsApi(api_client)
    api_v1_runners_unregister_post_request = peertube_api_client.ApiV1RunnersUnregisterPostRequest() # ApiV1RunnersUnregisterPostRequest |  (optional)

    try:
        # Request a new job
        api_response = api_instance.api_v1_runners_jobs_request_post(api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)
        print("The response of RunnerJobsApi->api_v1_runners_jobs_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnerJobsApi->api_v1_runners_jobs_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_runners_unregister_post_request** | [**ApiV1RunnersUnregisterPostRequest**](ApiV1RunnersUnregisterPostRequest.md)|  | [optional] 

### Return type

[**ApiV1RunnersJobsRequestPost200Response**](ApiV1RunnersJobsRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

