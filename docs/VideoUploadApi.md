# peertube_api_client.VideoUploadApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_video**](VideoUploadApi.md#import_video) | **POST** /api/v1/videos/imports | Import a video
[**upload_legacy**](VideoUploadApi.md#upload_legacy) | **POST** /api/v1/videos/upload | Upload a video
[**upload_resumable**](VideoUploadApi.md#upload_resumable) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video
[**upload_resumable_cancel**](VideoUploadApi.md#upload_resumable_cancel) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
[**upload_resumable_init**](VideoUploadApi.md#upload_resumable_init) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video


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
    api_instance = peertube_api_client.VideoUploadApi(api_client)
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
        print("The response of VideoUploadApi->import_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoUploadApi->import_video: %s\n" % e)
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
    api_instance = peertube_api_client.VideoUploadApi(api_client)
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
        print("The response of VideoUploadApi->upload_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoUploadApi->upload_legacy: %s\n" % e)
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
    api_instance = peertube_api_client.VideoUploadApi(api_client)
    upload_id = 'upload_id_example' # str | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
    content_range = 'bytes 0-262143/2469036' # str | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
    content_length = 262144 # float | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
    body = None # bytearray |  (optional)

    try:
        # Send chunk for the resumable upload of a video
        api_response = api_instance.upload_resumable(upload_id, content_range, content_length, body=body)
        print("The response of VideoUploadApi->upload_resumable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoUploadApi->upload_resumable: %s\n" % e)
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
    api_instance = peertube_api_client.VideoUploadApi(api_client)
    upload_id = 'upload_id_example' # str | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
    content_length = 0 # float | 

    try:
        # Cancel the resumable upload of a video, deleting any data uploaded so far
        api_instance.upload_resumable_cancel(upload_id, content_length)
    except Exception as e:
        print("Exception when calling VideoUploadApi->upload_resumable_cancel: %s\n" % e)
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
    api_instance = peertube_api_client.VideoUploadApi(api_client)
    x_upload_content_length = 2469036 # float | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
    x_upload_content_type = 'video/mp4' # str | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
    video_upload_request_resumable = peertube_api_client.VideoUploadRequestResumable() # VideoUploadRequestResumable |  (optional)

    try:
        # Initialize the resumable upload of a video
        api_instance.upload_resumable_init(x_upload_content_length, x_upload_content_type, video_upload_request_resumable=video_upload_request_resumable)
    except Exception as e:
        print("Exception when calling VideoUploadApi->upload_resumable_init: %s\n" % e)
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

