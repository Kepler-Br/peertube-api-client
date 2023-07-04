# peertube_api_client.LiveVideosApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_live**](LiveVideosApi.md#add_live) | **POST** /api/v1/videos/live | Create a live
[**api_v1_videos_id_live_session_get**](LiveVideosApi.md#api_v1_videos_id_live_session_get) | **GET** /api/v1/videos/{id}/live-session | Get live session of a replay
[**api_v1_videos_live_id_sessions_get**](LiveVideosApi.md#api_v1_videos_live_id_sessions_get) | **GET** /api/v1/videos/live/{id}/sessions | List live sessions
[**get_live_id**](LiveVideosApi.md#get_live_id) | **GET** /api/v1/videos/live/{id} | Get information about a live
[**update_live_id**](LiveVideosApi.md#update_live_id) | **PUT** /api/v1/videos/live/{id} | Update information about a live


# **add_live**
> VideoUploadResponse add_live(channel_id, name, save_replay=save_replay, replay_settings=replay_settings, permanent_live=permanent_live, latency_mode=latency_mode, thumbnailfile=thumbnailfile, previewfile=previewfile, privacy=privacy, category=category, licence=licence, language=language, description=description, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled)

Create a live

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.live_video_latency_mode import LiveVideoLatencyMode
from peertube_api_client.models.live_video_replay_settings import LiveVideoReplaySettings
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_upload_response import VideoUploadResponse
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
    api_instance = peertube_api_client.LiveVideosApi(api_client)
    channel_id = 56 # int | Channel id that will contain this live video
    name = 'name_example' # str | Live video/replay name
    save_replay = True # bool |  (optional)
    replay_settings = peertube_api_client.LiveVideoReplaySettings() # LiveVideoReplaySettings |  (optional)
    permanent_live = True # bool | User can stream multiple times in a permanent live (optional)
    latency_mode = peertube_api_client.LiveVideoLatencyMode() # LiveVideoLatencyMode |  (optional)
    thumbnailfile = None # bytearray | Live video/replay thumbnail file (optional)
    previewfile = None # bytearray | Live video/replay preview file (optional)
    privacy = peertube_api_client.VideoPrivacySet() # VideoPrivacySet |  (optional)
    category = 56 # int | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    licence = 56 # int | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language = 'language_example' # str | language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
    description = 'description_example' # str | Live video/replay description (optional)
    support = 'support_example' # str | A text tell the audience how to support the creator (optional)
    nsfw = True # bool | Whether or not this live video/replay contains sensitive content (optional)
    tags = ['tags_example'] # List[str] | Live video/replay tags (maximum 5 tags each between 2 and 30 characters) (optional)
    comments_enabled = True # bool | Enable or disable comments for this live video/replay (optional)
    download_enabled = True # bool | Enable or disable downloading for the replay of this live video (optional)

    try:
        # Create a live
        api_response = api_instance.add_live(channel_id, name, save_replay=save_replay, replay_settings=replay_settings, permanent_live=permanent_live, latency_mode=latency_mode, thumbnailfile=thumbnailfile, previewfile=previewfile, privacy=privacy, category=category, licence=licence, language=language, description=description, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled)
        print("The response of LiveVideosApi->add_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveVideosApi->add_live: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **int**| Channel id that will contain this live video | 
 **name** | **str**| Live video/replay name | 
 **save_replay** | **bool**|  | [optional] 
 **replay_settings** | [**LiveVideoReplaySettings**](LiveVideoReplaySettings.md)|  | [optional] 
 **permanent_live** | **bool**| User can stream multiple times in a permanent live | [optional] 
 **latency_mode** | [**LiveVideoLatencyMode**](LiveVideoLatencyMode.md)|  | [optional] 
 **thumbnailfile** | **bytearray**| Live video/replay thumbnail file | [optional] 
 **previewfile** | **bytearray**| Live video/replay preview file | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **category** | **int**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **licence** | **int**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language** | **str**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **description** | **str**| Live video/replay description | [optional] 
 **support** | **str**| A text tell the audience how to support the creator | [optional] 
 **nsfw** | **bool**| Whether or not this live video/replay contains sensitive content | [optional] 
 **tags** | [**List[str]**](str.md)| Live video/replay tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **comments_enabled** | **bool**| Enable or disable comments for this live video/replay | [optional] 
 **download_enabled** | **bool**| Enable or disable downloading for the replay of this live video | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Disambiguate via &#x60;type&#x60;: - default type for a validation error - &#x60;live_conflicting_permanent_and_save_replay&#x60; for conflicting parameters set  |  -  |
**403** | Disambiguate via &#x60;type&#x60;: - &#x60;live_not_enabled&#x60; for a disabled live feature - &#x60;live_not_allowing_replay&#x60; for a disabled replay feature - &#x60;max_instance_lives_limit_reached&#x60; for the absolute concurrent live limit - &#x60;max_user_lives_limit_reached&#x60; for the user concurrent live limit  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_id_live_session_get**
> LiveVideoSessionResponse api_v1_videos_id_live_session_get(id)

Get live session of a replay

If the video is a replay of a live, you can find the associated live session using this endpoint

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.live_video_session_response import LiveVideoSessionResponse
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
    api_instance = peertube_api_client.LiveVideosApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get live session of a replay
        api_response = api_instance.api_v1_videos_id_live_session_get(id)
        print("The response of LiveVideosApi->api_v1_videos_id_live_session_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveVideosApi->api_v1_videos_id_live_session_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**LiveVideoSessionResponse**](LiveVideoSessionResponse.md)

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

# **api_v1_videos_live_id_sessions_get**
> ApiV1VideosLiveIdSessionsGet200Response api_v1_videos_live_id_sessions_get(id)

List live sessions

List all sessions created in a particular live

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_videos_live_id_sessions_get200_response import ApiV1VideosLiveIdSessionsGet200Response
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
    api_instance = peertube_api_client.LiveVideosApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # List live sessions
        api_response = api_instance.api_v1_videos_live_id_sessions_get(id)
        print("The response of LiveVideosApi->api_v1_videos_live_id_sessions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveVideosApi->api_v1_videos_live_id_sessions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**ApiV1VideosLiveIdSessionsGet200Response**](ApiV1VideosLiveIdSessionsGet200Response.md)

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

# **get_live_id**
> LiveVideoResponse get_live_id(id)

Get information about a live

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.live_video_response import LiveVideoResponse
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
    api_instance = peertube_api_client.LiveVideosApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get information about a live
        api_response = api_instance.get_live_id(id)
        print("The response of LiveVideosApi->get_live_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LiveVideosApi->get_live_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**LiveVideoResponse**](LiveVideoResponse.md)

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

# **update_live_id**
> update_live_id(id, live_video_update=live_video_update)

Update information about a live

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.live_video_update import LiveVideoUpdate
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
    api_instance = peertube_api_client.LiveVideosApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    live_video_update = peertube_api_client.LiveVideoUpdate() # LiveVideoUpdate |  (optional)

    try:
        # Update information about a live
        api_instance.update_live_id(id, live_video_update=live_video_update)
    except Exception as e:
        print("Exception when calling LiveVideosApi->update_live_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **live_video_update** | [**LiveVideoUpdate**](LiveVideoUpdate.md)|  | [optional] 

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
**400** | bad parameters or trying to update a live that has already started |  -  |
**403** | trying to save replay of the live but saving replay is not enabled on the instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

