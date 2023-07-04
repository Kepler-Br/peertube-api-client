# peertube_api_client.AbusesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_abuses_abuse_id_delete**](AbusesApi.md#api_v1_abuses_abuse_id_delete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse
[**api_v1_abuses_abuse_id_messages_abuse_message_id_delete**](AbusesApi.md#api_v1_abuses_abuse_id_messages_abuse_message_id_delete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message
[**api_v1_abuses_abuse_id_messages_get**](AbusesApi.md#api_v1_abuses_abuse_id_messages_get) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse
[**api_v1_abuses_abuse_id_messages_post**](AbusesApi.md#api_v1_abuses_abuse_id_messages_post) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse
[**api_v1_abuses_abuse_id_put**](AbusesApi.md#api_v1_abuses_abuse_id_put) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse
[**api_v1_abuses_post**](AbusesApi.md#api_v1_abuses_post) | **POST** /api/v1/abuses | Report an abuse
[**get_abuses**](AbusesApi.md#get_abuses) | **GET** /api/v1/abuses | List abuses
[**get_my_abuses**](AbusesApi.md#get_my_abuses) | **GET** /api/v1/users/me/abuses | List my abuses


# **api_v1_abuses_abuse_id_delete**
> api_v1_abuses_abuse_id_delete(abuse_id)

Delete an abuse

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
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id

    try:
        # Delete an abuse
        api_instance.api_v1_abuses_abuse_id_delete(abuse_id)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abuse_id** | **int**| Abuse id | 

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
**404** | block not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_abuses_abuse_id_messages_abuse_message_id_delete**
> api_v1_abuses_abuse_id_messages_abuse_message_id_delete(abuse_id, abuse_message_id)

Delete an abuse message

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
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id
    abuse_message_id = 56 # int | Abuse message id

    try:
        # Delete an abuse message
        api_instance.api_v1_abuses_abuse_id_messages_abuse_message_id_delete(abuse_id, abuse_message_id)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_messages_abuse_message_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abuse_id** | **int**| Abuse id | 
 **abuse_message_id** | **int**| Abuse message id | 

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

# **api_v1_abuses_abuse_id_messages_get**
> ApiV1AbusesAbuseIdMessagesGet200Response api_v1_abuses_abuse_id_messages_get(abuse_id)

List messages of an abuse

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_abuses_abuse_id_messages_get200_response import ApiV1AbusesAbuseIdMessagesGet200Response
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id

    try:
        # List messages of an abuse
        api_response = api_instance.api_v1_abuses_abuse_id_messages_get(abuse_id)
        print("The response of AbusesApi->api_v1_abuses_abuse_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_messages_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abuse_id** | **int**| Abuse id | 

### Return type

[**ApiV1AbusesAbuseIdMessagesGet200Response**](ApiV1AbusesAbuseIdMessagesGet200Response.md)

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

# **api_v1_abuses_abuse_id_messages_post**
> api_v1_abuses_abuse_id_messages_post(abuse_id, api_v1_abuses_abuse_id_messages_post_request)

Add message to an abuse

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_abuses_abuse_id_messages_post_request import ApiV1AbusesAbuseIdMessagesPostRequest
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id
    api_v1_abuses_abuse_id_messages_post_request = peertube_api_client.ApiV1AbusesAbuseIdMessagesPostRequest() # ApiV1AbusesAbuseIdMessagesPostRequest | 

    try:
        # Add message to an abuse
        api_instance.api_v1_abuses_abuse_id_messages_post(abuse_id, api_v1_abuses_abuse_id_messages_post_request)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_messages_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abuse_id** | **int**| Abuse id | 
 **api_v1_abuses_abuse_id_messages_post_request** | [**ApiV1AbusesAbuseIdMessagesPostRequest**](ApiV1AbusesAbuseIdMessagesPostRequest.md)|  | 

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
**200** | successful operation |  -  |
**400** | incorrect request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_abuses_abuse_id_put**
> api_v1_abuses_abuse_id_put(abuse_id, api_v1_abuses_abuse_id_put_request=api_v1_abuses_abuse_id_put_request)

Update an abuse

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_abuses_abuse_id_put_request import ApiV1AbusesAbuseIdPutRequest
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    abuse_id = 56 # int | Abuse id
    api_v1_abuses_abuse_id_put_request = peertube_api_client.ApiV1AbusesAbuseIdPutRequest() # ApiV1AbusesAbuseIdPutRequest |  (optional)

    try:
        # Update an abuse
        api_instance.api_v1_abuses_abuse_id_put(abuse_id, api_v1_abuses_abuse_id_put_request=api_v1_abuses_abuse_id_put_request)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_abuse_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **abuse_id** | **int**| Abuse id | 
 **api_v1_abuses_abuse_id_put_request** | [**ApiV1AbusesAbuseIdPutRequest**](ApiV1AbusesAbuseIdPutRequest.md)|  | [optional] 

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
**404** | abuse not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_abuses_post**
> ApiV1AbusesPost200Response api_v1_abuses_post(api_v1_abuses_post_request)

Report an abuse

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_abuses_post200_response import ApiV1AbusesPost200Response
from peertube_api_client.models.api_v1_abuses_post_request import ApiV1AbusesPostRequest
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    api_v1_abuses_post_request = peertube_api_client.ApiV1AbusesPostRequest() # ApiV1AbusesPostRequest | 

    try:
        # Report an abuse
        api_response = api_instance.api_v1_abuses_post(api_v1_abuses_post_request)
        print("The response of AbusesApi->api_v1_abuses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AbusesApi->api_v1_abuses_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_abuses_post_request** | [**ApiV1AbusesPostRequest**](ApiV1AbusesPostRequest.md)|  | 

### Return type

[**ApiV1AbusesPost200Response**](ApiV1AbusesPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | incorrect request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_abuses**
> GetMyAbuses200Response get_abuses(id=id, predefined_reason=predefined_reason, search=search, state=state, search_reporter=search_reporter, search_reportee=search_reportee, search_video=search_video, search_video_channel=search_video_channel, video_is=video_is, filter=filter, start=start, count=count, sort=sort)

List abuses

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.abuse_state_set import AbuseStateSet
from peertube_api_client.models.get_my_abuses200_response import GetMyAbuses200Response
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    id = 56 # int | only list the report with this id (optional)
    predefined_reason = ['predefined_reason_example'] # List[str] | predefined reason the listed reports should contain (optional)
    search = 'search_example' # str | plain search that will match with video titles, reporter names and more (optional)
    state = peertube_api_client.AbuseStateSet() # AbuseStateSet |  (optional)
    search_reporter = 'search_reporter_example' # str | only list reports of a specific reporter (optional)
    search_reportee = 'search_reportee_example' # str | only list reports of a specific reportee (optional)
    search_video = 'search_video_example' # str | only list reports of a specific video (optional)
    search_video_channel = 'search_video_channel_example' # str | only list reports of a specific video channel (optional)
    video_is = 'video_is_example' # str | only list deleted or blocklisted videos (optional)
    filter = 'filter_example' # str | only list account, comment or video reports (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort abuses by criteria (optional)

    try:
        # List abuses
        api_response = api_instance.get_abuses(id=id, predefined_reason=predefined_reason, search=search, state=state, search_reporter=search_reporter, search_reportee=search_reportee, search_video=search_video, search_video_channel=search_video_channel, video_is=video_is, filter=filter, start=start, count=count, sort=sort)
        print("The response of AbusesApi->get_abuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AbusesApi->get_abuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| only list the report with this id | [optional] 
 **predefined_reason** | [**List[str]**](str.md)| predefined reason the listed reports should contain | [optional] 
 **search** | **str**| plain search that will match with video titles, reporter names and more | [optional] 
 **state** | [**AbuseStateSet**](.md)|  | [optional] 
 **search_reporter** | **str**| only list reports of a specific reporter | [optional] 
 **search_reportee** | **str**| only list reports of a specific reportee | [optional] 
 **search_video** | **str**| only list reports of a specific video | [optional] 
 **search_video_channel** | **str**| only list reports of a specific video channel | [optional] 
 **video_is** | **str**| only list deleted or blocklisted videos | [optional] 
 **filter** | **str**| only list account, comment or video reports | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort abuses by criteria | [optional] 

### Return type

[**GetMyAbuses200Response**](GetMyAbuses200Response.md)

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

# **get_my_abuses**
> GetMyAbuses200Response get_my_abuses(id=id, state=state, sort=sort, start=start, count=count)

List my abuses

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.abuse_state_set import AbuseStateSet
from peertube_api_client.models.get_my_abuses200_response import GetMyAbuses200Response
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
    api_instance = peertube_api_client.AbusesApi(api_client)
    id = 56 # int | only list the report with this id (optional)
    state = peertube_api_client.AbuseStateSet() # AbuseStateSet |  (optional)
    sort = 'sort_example' # str | Sort abuses by criteria (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)

    try:
        # List my abuses
        api_response = api_instance.get_my_abuses(id=id, state=state, sort=sort, start=start, count=count)
        print("The response of AbusesApi->get_my_abuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AbusesApi->get_my_abuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| only list the report with this id | [optional] 
 **state** | [**AbuseStateSet**](.md)|  | [optional] 
 **sort** | **str**| Sort abuses by criteria | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]

### Return type

[**GetMyAbuses200Response**](GetMyAbuses200Response.md)

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

