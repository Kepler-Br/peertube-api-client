# peertube_api_client.VideoApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_live**](VideoApi.md#add_live) | **POST** /api/v1/videos/live | Create a live
[**add_view**](VideoApi.md#add_view) | **POST** /api/v1/videos/{id}/views | Notify user is watching a video
[**api_v1_videos_id_studio_edit_post**](VideoApi.md#api_v1_videos_id_studio_edit_post) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
[**api_v1_videos_id_watching_put**](VideoApi.md#api_v1_videos_id_watching_put) | **PUT** /api/v1/videos/{id}/watching | Set watching progress of a video
[**del_video**](VideoApi.md#del_video) | **DELETE** /api/v1/videos/{id} | Delete a video
[**get_account_videos**](VideoApi.md#get_account_videos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
[**get_categories**](VideoApi.md#get_categories) | **GET** /api/v1/videos/categories | List available video categories
[**get_languages**](VideoApi.md#get_languages) | **GET** /api/v1/videos/languages | List available video languages
[**get_licences**](VideoApi.md#get_licences) | **GET** /api/v1/videos/licences | List available video licences
[**get_live_id**](VideoApi.md#get_live_id) | **GET** /api/v1/videos/live/{id} | Get information about a live
[**get_video**](VideoApi.md#get_video) | **GET** /api/v1/videos/{id} | Get a video
[**get_video_channel_videos**](VideoApi.md#get_video_channel_videos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
[**get_video_desc**](VideoApi.md#get_video_desc) | **GET** /api/v1/videos/{id}/description | Get complete video description
[**get_video_privacy_policies**](VideoApi.md#get_video_privacy_policies) | **GET** /api/v1/videos/privacies | List available video privacy policies
[**get_video_source**](VideoApi.md#get_video_source) | **POST** /api/v1/videos/{id}/source | Get video source file metadata
[**get_videos**](VideoApi.md#get_videos) | **GET** /api/v1/videos | List videos
[**put_video**](VideoApi.md#put_video) | **PUT** /api/v1/videos/{id} | Update a video
[**request_video_token**](VideoApi.md#request_video_token) | **POST** /api/v1/videos/{id}/token | Request video token
[**update_live_id**](VideoApi.md#update_live_id) | **PUT** /api/v1/videos/live/{id} | Update information about a live
[**upload_legacy**](VideoApi.md#upload_legacy) | **POST** /api/v1/videos/upload | Upload a video
[**upload_resumable**](VideoApi.md#upload_resumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
[**upload_resumable_cancel**](VideoApi.md#upload_resumable_cancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
[**upload_resumable_init**](VideoApi.md#upload_resumable_init) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video


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
    api_instance = peertube_api_client.VideoApi(api_client)
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
        print("The response of VideoApi->add_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->add_live: %s\n" % e)
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

# **add_view**
> add_view(id, user_viewing_video)

Notify user is watching a video

Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video's viewers counter. If the user is authenticated, PeerTube will also store the current player time.

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user_viewing_video import UserViewingVideo
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    user_viewing_video = peertube_api_client.UserViewingVideo() # UserViewingVideo | 

    try:
        # Notify user is watching a video
        api_instance.add_view(id, user_viewing_video)
    except Exception as e:
        print("Exception when calling VideoApi->add_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **user_viewing_video** | [**UserViewingVideo**](UserViewingVideo.md)|  | 

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

# **api_v1_videos_id_studio_edit_post**
> api_v1_videos_id_studio_edit_post(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Create a studio task
        api_instance.api_v1_videos_id_studio_edit_post(id)
    except Exception as e:
        print("Exception when calling VideoApi->api_v1_videos_id_studio_edit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | incorrect parameters |  -  |
**404** | video not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_id_watching_put**
> api_v1_videos_id_watching_put(id, user_viewing_video)

Set watching progress of a video

This endpoint has been deprecated. Use `/videos/{id}/views` instead

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.user_viewing_video import UserViewingVideo
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    user_viewing_video = peertube_api_client.UserViewingVideo() # UserViewingVideo | 

    try:
        # Set watching progress of a video
        api_instance.api_v1_videos_id_watching_put(id, user_viewing_video)
    except Exception as e:
        print("Exception when calling VideoApi->api_v1_videos_id_watching_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **user_viewing_video** | [**UserViewingVideo**](UserViewingVideo.md)|  | 

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

# **del_video**
> del_video(id)

Delete a video

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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Delete a video
        api_instance.del_video(id)
    except Exception as e:
        print("Exception when calling VideoApi->del_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

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

# **get_account_videos**
> VideoListResponse get_account_videos(name, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos of an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
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
    api_instance = peertube_api_client.VideoApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    category_one_of = peertube_api_client.GetAccountVideosCategoryOneOfParameter() # GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    is_live = True # bool | whether or not the video is a live (optional)
    tags_one_of = peertube_api_client.GetAccountVideosTagsOneOfParameter() # GetAccountVideosTagsOneOfParameter | tag(s) of the video (optional)
    tags_all_of = peertube_api_client.GetAccountVideosTagsAllOfParameter() # GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video (optional)
    licence_one_of = peertube_api_client.GetAccountVideosLicenceOneOfParameter() # GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language_one_of = peertube_api_client.GetAccountVideosLanguageOneOfParameter() # GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)
    skip_count = 'false' # str | if you don't need the `total` in the response (optional) (default to 'false')
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str |  (optional)
    exclude_already_watched = True # bool | Whether or not to exclude videos that are in the user's video history (optional)

    try:
        # List videos of an account
        api_response = api_instance.get_account_videos(name, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of VideoApi->get_account_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_account_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **category_one_of** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **is_live** | **bool**| whether or not the video is a live | [optional] 
 **tags_one_of** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tags_all_of** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licence_one_of** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language_one_of** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skip_count** | **str**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**|  | [optional] 
 **exclude_already_watched** | **bool**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **get_categories**
> List[str] get_categories()

List available video categories

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoApi(api_client)

    try:
        # List available video categories
        api_response = api_instance.get_categories()
        print("The response of VideoApi->get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_categories: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_languages**
> List[str] get_languages()

List available video languages

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoApi(api_client)

    try:
        # List available video languages
        api_response = api_instance.get_languages()
        print("The response of VideoApi->get_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_languages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_licences**
> List[str] get_licences()

List available video licences

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoApi(api_client)

    try:
        # List available video licences
        api_response = api_instance.get_licences()
        print("The response of VideoApi->get_licences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_licences: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get information about a live
        api_response = api_instance.get_live_id(id)
        print("The response of VideoApi->get_live_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_live_id: %s\n" % e)
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

# **get_video**
> VideoDetails get_video(id)

Get a video

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_details import VideoDetails
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get a video
        api_response = api_instance.get_video(id)
        print("The response of VideoApi->get_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**VideoDetails**](VideoDetails.md)

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

# **get_video_channel_videos**
> VideoListResponse get_video_channel_videos(channel_handle, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos of a video channel

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
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
    api_instance = peertube_api_client.VideoApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    category_one_of = peertube_api_client.GetAccountVideosCategoryOneOfParameter() # GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    is_live = True # bool | whether or not the video is a live (optional)
    tags_one_of = peertube_api_client.GetAccountVideosTagsOneOfParameter() # GetAccountVideosTagsOneOfParameter | tag(s) of the video (optional)
    tags_all_of = peertube_api_client.GetAccountVideosTagsAllOfParameter() # GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video (optional)
    licence_one_of = peertube_api_client.GetAccountVideosLicenceOneOfParameter() # GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language_one_of = peertube_api_client.GetAccountVideosLanguageOneOfParameter() # GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)
    skip_count = 'false' # str | if you don't need the `total` in the response (optional) (default to 'false')
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str |  (optional)
    exclude_already_watched = True # bool | Whether or not to exclude videos that are in the user's video history (optional)

    try:
        # List videos of a video channel
        api_response = api_instance.get_video_channel_videos(channel_handle, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of VideoApi->get_video_channel_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_video_channel_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **category_one_of** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **is_live** | **bool**| whether or not the video is a live | [optional] 
 **tags_one_of** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tags_all_of** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licence_one_of** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language_one_of** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skip_count** | **str**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**|  | [optional] 
 **exclude_already_watched** | **bool**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **get_video_desc**
> str get_video_desc(id)

Get complete video description

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get complete video description
        api_response = api_instance.get_video_desc(id)
        print("The response of VideoApi->get_video_desc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_video_desc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

**str**

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

# **get_video_privacy_policies**
> List[str] get_video_privacy_policies()

List available video privacy policies

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoApi(api_client)

    try:
        # List available video privacy policies
        api_response = api_instance.get_video_privacy_policies()
        print("The response of VideoApi->get_video_privacy_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_video_privacy_policies: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_video_source**
> VideoSource get_video_source(id)

Get video source file metadata

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_source import VideoSource
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get video source file metadata
        api_response = api_instance.get_video_source(id)
        print("The response of VideoApi->get_video_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_video_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**VideoSource**](VideoSource.md)

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

# **get_videos**
> VideoListResponse get_videos(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
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
    api_instance = peertube_api_client.VideoApi(api_client)
    category_one_of = peertube_api_client.GetAccountVideosCategoryOneOfParameter() # GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    is_live = True # bool | whether or not the video is a live (optional)
    tags_one_of = peertube_api_client.GetAccountVideosTagsOneOfParameter() # GetAccountVideosTagsOneOfParameter | tag(s) of the video (optional)
    tags_all_of = peertube_api_client.GetAccountVideosTagsAllOfParameter() # GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video (optional)
    licence_one_of = peertube_api_client.GetAccountVideosLicenceOneOfParameter() # GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language_one_of = peertube_api_client.GetAccountVideosLanguageOneOfParameter() # GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)
    skip_count = 'false' # str | if you don't need the `total` in the response (optional) (default to 'false')
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str |  (optional)
    exclude_already_watched = True # bool | Whether or not to exclude videos that are in the user's video history (optional)

    try:
        # List videos
        api_response = api_instance.get_videos(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of VideoApi->get_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->get_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_one_of** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **is_live** | **bool**| whether or not the video is a live | [optional] 
 **tags_one_of** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tags_all_of** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licence_one_of** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language_one_of** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skip_count** | **str**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**|  | [optional] 
 **exclude_already_watched** | **bool**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **put_video**
> put_video(id, thumbnailfile=thumbnailfile, previewfile=previewfile, category=category, licence=licence, language=language, privacy=privacy, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, name=name, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update)

Update a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    thumbnailfile = None # bytearray | Video thumbnail file (optional)
    previewfile = None # bytearray | Video preview file (optional)
    category = 56 # int | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    licence = 56 # int | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language = 'language_example' # str | language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
    privacy = peertube_api_client.VideoPrivacySet() # VideoPrivacySet |  (optional)
    description = 'description_example' # str | Video description (optional)
    wait_transcoding = 'wait_transcoding_example' # str | Whether or not we wait transcoding before publish the video (optional)
    support = 'support_example' # str | A text tell the audience how to support the video creator (optional)
    nsfw = True # bool | Whether or not this video contains sensitive content (optional)
    name = 'name_example' # str | Video name (optional)
    tags = ['tags_example'] # List[str] | Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
    comments_enabled = True # bool | Enable or disable comments for this video (optional)
    download_enabled = True # bool | Enable or disable downloading for this video (optional)
    originally_published_at = '2013-10-20T19:20:30+01:00' # datetime | Date when the content was originally published (optional)
    schedule_update = peertube_api_client.VideoScheduledUpdate() # VideoScheduledUpdate |  (optional)

    try:
        # Update a video
        api_instance.put_video(id, thumbnailfile=thumbnailfile, previewfile=previewfile, category=category, licence=licence, language=language, privacy=privacy, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, name=name, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update)
    except Exception as e:
        print("Exception when calling VideoApi->put_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **thumbnailfile** | **bytearray**| Video thumbnail file | [optional] 
 **previewfile** | **bytearray**| Video preview file | [optional] 
 **category** | **int**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **licence** | **int**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language** | **str**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **description** | **str**| Video description | [optional] 
 **wait_transcoding** | **str**| Whether or not we wait transcoding before publish the video | [optional] 
 **support** | **str**| A text tell the audience how to support the video creator | [optional] 
 **nsfw** | **bool**| Whether or not this video contains sensitive content | [optional] 
 **name** | **str**| Video name | [optional] 
 **tags** | [**List[str]**](str.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **comments_enabled** | **bool**| Enable or disable comments for this video | [optional] 
 **download_enabled** | **bool**| Enable or disable downloading for this video | [optional] 
 **originally_published_at** | **datetime**| Date when the content was originally published | [optional] 
 **schedule_update** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_video_token**
> VideoTokenResponse request_video_token(id)

Request video token

Request special tokens that expire quickly to use them in some context (like accessing private static files)

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_token_response import VideoTokenResponse
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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Request video token
        api_response = api_instance.request_video_token(id)
        print("The response of VideoApi->request_video_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->request_video_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**VideoTokenResponse**](VideoTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | incorrect parameters |  -  |
**404** | video not found |  -  |

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
    api_instance = peertube_api_client.VideoApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    live_video_update = peertube_api_client.LiveVideoUpdate() # LiveVideoUpdate |  (optional)

    try:
        # Update information about a live
        api_instance.update_live_id(id, live_video_update=live_video_update)
    except Exception as e:
        print("Exception when calling VideoApi->update_live_id: %s\n" % e)
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

# **upload_legacy**
> VideoUploadResponse upload_legacy(name, videofile, channel_id=channel_id, privacy=privacy, category=category, licence=licence, language=language, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update, thumbnailfile=thumbnailfile, previewfile=previewfile)

Upload a video

Uses a single request to upload a video.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate
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
    api_instance = peertube_api_client.VideoApi(api_client)
    name = 'name_example' # str | Video name
    videofile = None # bytearray | Video file
    channel_id = 56 # int | Channel id that will contain this video (optional)
    privacy = peertube_api_client.VideoPrivacySet() # VideoPrivacySet |  (optional)
    category = 56 # int | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    licence = 56 # int | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language = 'language_example' # str | language id of the video (see [/videos/languages](#operation/getLanguages)) (optional)
    description = 'description_example' # str | Video description (optional)
    wait_transcoding = True # bool | Whether or not we wait transcoding before publish the video (optional)
    support = 'support_example' # str | A text tell the audience how to support the video creator (optional)
    nsfw = True # bool | Whether or not this video contains sensitive content (optional)
    tags = ['tags_example'] # List[str] | Video tags (maximum 5 tags each between 2 and 30 characters) (optional)
    comments_enabled = True # bool | Enable or disable comments for this video (optional)
    download_enabled = True # bool | Enable or disable downloading for this video (optional)
    originally_published_at = '2013-10-20T19:20:30+01:00' # datetime | Date when the content was originally published (optional)
    schedule_update = peertube_api_client.VideoScheduledUpdate() # VideoScheduledUpdate |  (optional)
    thumbnailfile = None # bytearray | Video thumbnail file (optional)
    previewfile = None # bytearray | Video preview file (optional)

    try:
        # Upload a video
        api_response = api_instance.upload_legacy(name, videofile, channel_id=channel_id, privacy=privacy, category=category, licence=licence, language=language, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update, thumbnailfile=thumbnailfile, previewfile=previewfile)
        print("The response of VideoApi->upload_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->upload_legacy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Video name | 
 **videofile** | **bytearray**| Video file | 
 **channel_id** | **int**| Channel id that will contain this video | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **category** | **int**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **licence** | **int**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language** | **str**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **description** | **str**| Video description | [optional] 
 **wait_transcoding** | **bool**| Whether or not we wait transcoding before publish the video | [optional] 
 **support** | **str**| A text tell the audience how to support the video creator | [optional] 
 **nsfw** | **bool**| Whether or not this video contains sensitive content | [optional] 
 **tags** | [**List[str]**](str.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **comments_enabled** | **bool**| Enable or disable comments for this video | [optional] 
 **download_enabled** | **bool**| Enable or disable downloading for this video | [optional] 
 **originally_published_at** | **datetime**| Date when the content was originally published | [optional] 
 **schedule_update** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] 
 **thumbnailfile** | **bytearray**| Video thumbnail file | [optional] 
 **previewfile** | **bytearray**| Video preview file | [optional] 

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
**403** | video didn&#39;t pass upload filter |  -  |
**408** | upload has timed out |  -  |
**413** | If the response has no body, it means the reverse-proxy didn&#39;t let it through. Otherwise disambiguate via &#x60;type&#x60;: - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  * X-File-Maximum-Size - Maximum file size for the banner <br>  |
**415** | video type unsupported |  -  |
**422** | video unreadable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resumable**
> VideoUploadResponse upload_resumable(upload_id, content_range, content_length, body=body)

Send chunk for the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
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
    api_instance = peertube_api_client.VideoApi(api_client)
    upload_id = 'upload_id_example' # str | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
    content_range = 'bytes 0-262143/2469036' # str | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
    content_length = 262144 # float | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
    body = None # bytearray |  (optional)

    try:
        # Send chunk for the resumable upload of a video
        api_response = api_instance.upload_resumable(upload_id, content_range, content_length, body=body)
        print("The response of VideoApi->upload_resumable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoApi->upload_resumable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  | 
 **content_range** | **str**| Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/2469036&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  | 
 **content_length** | **float**| Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  | 
 **body** | **bytearray**|  | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | last chunk received |  * Content-Length -  <br>  |
**308** | resume incomplete |  * Range -  <br>  * Content-Length -  <br>  |
**403** | video didn&#39;t pass upload filter |  -  |
**404** | upload not found |  -  |
**409** | chunk doesn&#39;t match range |  -  |
**422** | video unreadable |  -  |
**429** | too many concurrent requests |  -  |
**503** | upload is already being processed |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resumable_cancel**
> upload_resumable_cancel(upload_id, content_length)

Cancel the resumable upload of a video, deleting any data uploaded so far

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video

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
    api_instance = peertube_api_client.VideoApi(api_client)
    upload_id = 'upload_id_example' # str | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
    content_length = 0 # float | 

    try:
        # Cancel the resumable upload of a video, deleting any data uploaded so far
        api_instance.upload_resumable_cancel(upload_id, content_length)
    except Exception as e:
        print("Exception when calling VideoApi->upload_resumable_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  | 
 **content_length** | **float**|  | 

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
**204** | upload cancelled |  * Content-Length -  <br>  |
**404** | upload not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resumable_init**
> upload_resumable_init(x_upload_content_length, x_upload_content_type, video_upload_request_resumable=video_upload_request_resumable)

Initialize the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_upload_request_resumable import VideoUploadRequestResumable
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
    api_instance = peertube_api_client.VideoApi(api_client)
    x_upload_content_length = 2469036 # float | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
    x_upload_content_type = 'video/mp4' # str | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
    video_upload_request_resumable = peertube_api_client.VideoUploadRequestResumable() # VideoUploadRequestResumable |  (optional)

    try:
        # Initialize the resumable upload of a video
        api_instance.upload_resumable_init(x_upload_content_length, x_upload_content_type, video_upload_request_resumable=video_upload_request_resumable)
    except Exception as e:
        print("Exception when calling VideoApi->upload_resumable_init: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_upload_content_length** | **float**| Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. | 
 **x_upload_content_type** | **str**| MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. | 
 **video_upload_request_resumable** | [**VideoUploadRequestResumable**](VideoUploadRequestResumable.md)|  | [optional] 

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
**200** | file already exists, send a [&#x60;resume&#x60;](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) request instead |  -  |
**201** | created |  * Location -  <br>  * Content-Length -  <br>  |
**413** | Disambiguate via &#x60;type&#x60;: - &#x60;max_file_size_reached&#x60; for the absolute file size limit - &#x60;quota_reached&#x60; for quota limits whether daily or global  |  -  |
**415** | video type unsupported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

