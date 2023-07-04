# peertube_api_client.MyNotificationsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_me_notification_settings_put**](MyNotificationsApi.md#api_v1_users_me_notification_settings_put) | **PUT** /api/v1/users/me/notification-settings | Update my notification settings
[**api_v1_users_me_notifications_get**](MyNotificationsApi.md#api_v1_users_me_notifications_get) | **GET** /api/v1/users/me/notifications | List my notifications
[**api_v1_users_me_notifications_read_all_post**](MyNotificationsApi.md#api_v1_users_me_notifications_read_all_post) | **POST** /api/v1/users/me/notifications/read-all | Mark all my notification as read
[**api_v1_users_me_notifications_read_post**](MyNotificationsApi.md#api_v1_users_me_notifications_read_post) | **POST** /api/v1/users/me/notifications/read | Mark notifications as read by their id


# **api_v1_users_me_notification_settings_put**
> api_v1_users_me_notification_settings_put(api_v1_users_me_notification_settings_put_request=api_v1_users_me_notification_settings_put_request)

Update my notification settings

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_notification_settings_put_request import ApiV1UsersMeNotificationSettingsPutRequest
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
    api_instance = peertube_api_client.MyNotificationsApi(api_client)
    api_v1_users_me_notification_settings_put_request = peertube_api_client.ApiV1UsersMeNotificationSettingsPutRequest() # ApiV1UsersMeNotificationSettingsPutRequest |  (optional)

    try:
        # Update my notification settings
        api_instance.api_v1_users_me_notification_settings_put(api_v1_users_me_notification_settings_put_request=api_v1_users_me_notification_settings_put_request)
    except Exception as e:
        print("Exception when calling MyNotificationsApi->api_v1_users_me_notification_settings_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_users_me_notification_settings_put_request** | [**ApiV1UsersMeNotificationSettingsPutRequest**](ApiV1UsersMeNotificationSettingsPutRequest.md)|  | [optional] 

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

# **api_v1_users_me_notifications_get**
> NotificationListResponse api_v1_users_me_notifications_get(unread=unread, start=start, count=count, sort=sort)

List my notifications

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.notification_list_response import NotificationListResponse
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
    api_instance = peertube_api_client.MyNotificationsApi(api_client)
    unread = True # bool | only list unread notifications (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List my notifications
        api_response = api_instance.api_v1_users_me_notifications_get(unread=unread, start=start, count=count, sort=sort)
        print("The response of MyNotificationsApi->api_v1_users_me_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyNotificationsApi->api_v1_users_me_notifications_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unread** | **bool**| only list unread notifications | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**NotificationListResponse**](NotificationListResponse.md)

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

# **api_v1_users_me_notifications_read_all_post**
> api_v1_users_me_notifications_read_all_post()

Mark all my notification as read

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
    api_instance = peertube_api_client.MyNotificationsApi(api_client)

    try:
        # Mark all my notification as read
        api_instance.api_v1_users_me_notifications_read_all_post()
    except Exception as e:
        print("Exception when calling MyNotificationsApi->api_v1_users_me_notifications_read_all_post: %s\n" % e)
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

# **api_v1_users_me_notifications_read_post**
> api_v1_users_me_notifications_read_post(api_v1_users_me_notifications_read_post_request=api_v1_users_me_notifications_read_post_request)

Mark notifications as read by their id

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_notifications_read_post_request import ApiV1UsersMeNotificationsReadPostRequest
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
    api_instance = peertube_api_client.MyNotificationsApi(api_client)
    api_v1_users_me_notifications_read_post_request = peertube_api_client.ApiV1UsersMeNotificationsReadPostRequest() # ApiV1UsersMeNotificationsReadPostRequest |  (optional)

    try:
        # Mark notifications as read by their id
        api_instance.api_v1_users_me_notifications_read_post(api_v1_users_me_notifications_read_post_request=api_v1_users_me_notifications_read_post_request)
    except Exception as e:
        print("Exception when calling MyNotificationsApi->api_v1_users_me_notifications_read_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_users_me_notifications_read_post_request** | [**ApiV1UsersMeNotificationsReadPostRequest**](ApiV1UsersMeNotificationsReadPostRequest.md)|  | [optional] 

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

