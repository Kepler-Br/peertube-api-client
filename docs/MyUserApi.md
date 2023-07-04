# peertube_api_client.MyUserApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_me_avatar_delete**](MyUserApi.md#api_v1_users_me_avatar_delete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar
[**api_v1_users_me_avatar_pick_post**](MyUserApi.md#api_v1_users_me_avatar_pick_post) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar
[**api_v1_users_me_video_quota_used_get**](MyUserApi.md#api_v1_users_me_video_quota_used_get) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota
[**api_v1_users_me_videos_get**](MyUserApi.md#api_v1_users_me_videos_get) | **GET** /api/v1/users/me/videos | Get videos of my user
[**api_v1_users_me_videos_imports_get**](MyUserApi.md#api_v1_users_me_videos_imports_get) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
[**api_v1_users_me_videos_video_id_rating_get**](MyUserApi.md#api_v1_users_me_videos_video_id_rating_get) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
[**get_my_abuses**](MyUserApi.md#get_my_abuses) | **GET** /api/v1/users/me/abuses | List my abuses
[**get_user_info**](MyUserApi.md#get_user_info) | **GET** /api/v1/users/me | Get my user information
[**put_user_info**](MyUserApi.md#put_user_info) | **PUT** /api/v1/users/me | Update my user information


# **api_v1_users_me_avatar_delete**
> api_v1_users_me_avatar_delete()

Delete my avatar

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
    api_instance = peertube_api_client.MyUserApi(api_client)

    try:
        # Delete my avatar
        api_instance.api_v1_users_me_avatar_delete()
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_avatar_delete: %s\n" % e)
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

# **api_v1_users_me_avatar_pick_post**
> ApiV1UsersMeAvatarPickPost200Response api_v1_users_me_avatar_pick_post(avatarfile=avatarfile)

Update my user avatar

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_avatar_pick_post200_response import ApiV1UsersMeAvatarPickPost200Response
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
    api_instance = peertube_api_client.MyUserApi(api_client)
    avatarfile = None # bytearray | The file to upload (optional)

    try:
        # Update my user avatar
        api_response = api_instance.api_v1_users_me_avatar_pick_post(avatarfile=avatarfile)
        print("The response of MyUserApi->api_v1_users_me_avatar_pick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_avatar_pick_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatarfile** | **bytearray**| The file to upload | [optional] 

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the banner <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_me_video_quota_used_get**
> ApiV1UsersMeVideoQuotaUsedGet200Response api_v1_users_me_video_quota_used_get()

Get my user used quota

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_video_quota_used_get200_response import ApiV1UsersMeVideoQuotaUsedGet200Response
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
    api_instance = peertube_api_client.MyUserApi(api_client)

    try:
        # Get my user used quota
        api_response = api_instance.api_v1_users_me_video_quota_used_get()
        print("The response of MyUserApi->api_v1_users_me_video_quota_used_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_video_quota_used_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiV1UsersMeVideoQuotaUsedGet200Response**](ApiV1UsersMeVideoQuotaUsedGet200Response.md)

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

# **api_v1_users_me_videos_get**
> VideoListResponse api_v1_users_me_videos_get(start=start, count=count, sort=sort)

Get videos of my user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
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
    api_instance = peertube_api_client.MyUserApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # Get videos of my user
        api_response = api_instance.api_v1_users_me_videos_get(start=start, count=count, sort=sort)
        print("The response of MyUserApi->api_v1_users_me_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_videos_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **api_v1_users_me_videos_imports_get**
> VideoImportsList api_v1_users_me_videos_imports_get(start=start, count=count, sort=sort, target_url=target_url, video_channel_sync_id=video_channel_sync_id, search=search)

Get video imports of my user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_imports_list import VideoImportsList
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
    api_instance = peertube_api_client.MyUserApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    target_url = 'target_url_example' # str | Filter on import target URL (optional)
    video_channel_sync_id = 3.4 # float | Filter on imports created by a specific channel synchronization (optional)
    search = 'search_example' # str | Search in video names (optional)

    try:
        # Get video imports of my user
        api_response = api_instance.api_v1_users_me_videos_imports_get(start=start, count=count, sort=sort, target_url=target_url, video_channel_sync_id=video_channel_sync_id, search=search)
        print("The response of MyUserApi->api_v1_users_me_videos_imports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_videos_imports_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **target_url** | **str**| Filter on import target URL | [optional] 
 **video_channel_sync_id** | **float**| Filter on imports created by a specific channel synchronization | [optional] 
 **search** | **str**| Search in video names | [optional] 

### Return type

[**VideoImportsList**](VideoImportsList.md)

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

# **api_v1_users_me_videos_video_id_rating_get**
> GetMeVideoRating api_v1_users_me_videos_video_id_rating_get(video_id)

Get rate of my user for a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_me_video_rating import GetMeVideoRating
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
    api_instance = peertube_api_client.MyUserApi(api_client)
    video_id = 56 # int | The video id

    try:
        # Get rate of my user for a video
        api_response = api_instance.api_v1_users_me_videos_video_id_rating_get(video_id)
        print("The response of MyUserApi->api_v1_users_me_videos_video_id_rating_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->api_v1_users_me_videos_video_id_rating_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

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
    api_instance = peertube_api_client.MyUserApi(api_client)
    id = 56 # int | only list the report with this id (optional)
    state = peertube_api_client.AbuseStateSet() # AbuseStateSet |  (optional)
    sort = 'sort_example' # str | Sort abuses by criteria (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)

    try:
        # List my abuses
        api_response = api_instance.get_my_abuses(id=id, state=state, sort=sort, start=start, count=count)
        print("The response of MyUserApi->get_my_abuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->get_my_abuses: %s\n" % e)
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

# **get_user_info**
> List[User] get_user_info()

Get my user information

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user import User
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
    api_instance = peertube_api_client.MyUserApi(api_client)

    try:
        # Get my user information
        api_response = api_instance.get_user_info()
        print("The response of MyUserApi->get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyUserApi->get_user_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

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

# **put_user_info**
> put_user_info(update_me)

Update my user information

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.update_me import UpdateMe
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
    api_instance = peertube_api_client.MyUserApi(api_client)
    update_me = peertube_api_client.UpdateMe() # UpdateMe | 

    try:
        # Update my user information
        api_instance.put_user_info(update_me)
    except Exception as e:
        print("Exception when calling MyUserApi->put_user_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_me** | [**UpdateMe**](UpdateMe.md)|  | 

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

