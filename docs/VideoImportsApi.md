# peertube_api_client.VideoImportsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_videos_imports_id_cancel_post**](VideoImportsApi.md#api_v1_videos_imports_id_cancel_post) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import
[**api_v1_videos_imports_id_delete**](VideoImportsApi.md#api_v1_videos_imports_id_delete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import
[**import_video**](VideoImportsApi.md#import_video) | **POST** /api/v1/videos/imports | Import a video


# **api_v1_videos_imports_id_cancel_post**
> api_v1_videos_imports_id_cancel_post(id)

Cancel video import

Cancel a pending video import

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
    api_instance = peertube_api_client.VideoImportsApi(api_client)
    id = 56 # int | Entity id

    try:
        # Cancel video import
        api_instance.api_v1_videos_imports_id_cancel_post(id)
    except Exception as e:
        print("Exception when calling VideoImportsApi->api_v1_videos_imports_id_cancel_post: %s\n" % e)
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

# **api_v1_videos_imports_id_delete**
> api_v1_videos_imports_id_delete(id)

Delete video import

Delete ended video import

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
    api_instance = peertube_api_client.VideoImportsApi(api_client)
    id = 56 # int | Entity id

    try:
        # Delete video import
        api_instance.api_v1_videos_imports_id_delete(id)
    except Exception as e:
        print("Exception when calling VideoImportsApi->api_v1_videos_imports_id_delete: %s\n" % e)
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

# **import_video**
> VideoUploadResponse import_video(name, channel_id, privacy=privacy, category=category, licence=licence, language=language, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update, thumbnailfile=thumbnailfile, previewfile=previewfile)

Import a video

Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)

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
    api_instance = peertube_api_client.VideoImportsApi(api_client)
    name = 'name_example' # str | Video name
    channel_id = 56 # int | Channel id that will contain this video
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
        # Import a video
        api_response = api_instance.import_video(name, channel_id, privacy=privacy, category=category, licence=licence, language=language, description=description, wait_transcoding=wait_transcoding, support=support, nsfw=nsfw, tags=tags, comments_enabled=comments_enabled, download_enabled=download_enabled, originally_published_at=originally_published_at, schedule_update=schedule_update, thumbnailfile=thumbnailfile, previewfile=previewfile)
        print("The response of VideoImportsApi->import_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoImportsApi->import_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Video name | 
 **channel_id** | **int**| Channel id that will contain this video | 
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
**400** | &#x60;magnetUri&#x60; or &#x60;targetUrl&#x60; or a torrent file missing |  -  |
**403** | video didn&#39;t pass pre-import filter |  -  |
**409** | HTTP or Torrent/magnetURI import not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

