# peertube_api_client.VideoFeedsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_syndicated_comments**](VideoFeedsApi.md#get_syndicated_comments) | **GET** /feeds/video-comments.{format} | Comments on videos feeds
[**get_syndicated_subscription_videos**](VideoFeedsApi.md#get_syndicated_subscription_videos) | **GET** /feeds/subscriptions.{format} | Videos of subscriptions feeds
[**get_syndicated_videos**](VideoFeedsApi.md#get_syndicated_videos) | **GET** /feeds/videos.{format} | Common videos feeds
[**get_videos_podcast_feed**](VideoFeedsApi.md#get_videos_podcast_feed) | **GET** /feeds/podcast/videos.xml | Videos podcast feed


# **get_syndicated_comments**
> List[VideoCommentsForXMLInner] get_syndicated_comments(format, video_id=video_id, account_id=account_id, account_name=account_name, video_channel_id=video_channel_id, video_channel_name=video_channel_name)

Comments on videos feeds

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_comments_for_xml_inner import VideoCommentsForXMLInner
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
    api_instance = peertube_api_client.VideoFeedsApi(api_client)
    format = 'format_example' # str | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    video_id = 'video_id_example' # str | limit listing to a specific video (optional)
    account_id = 'account_id_example' # str | limit listing to a specific account (optional)
    account_name = 'account_name_example' # str | limit listing to a specific account (optional)
    video_channel_id = 'video_channel_id_example' # str | limit listing to a specific video channel (optional)
    video_channel_name = 'video_channel_name_example' # str | limit listing to a specific video channel (optional)

    try:
        # Comments on videos feeds
        api_response = api_instance.get_syndicated_comments(format, video_id=video_id, account_id=account_id, account_name=account_name, video_channel_id=video_channel_id, video_channel_name=video_channel_name)
        print("The response of VideoFeedsApi->get_syndicated_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoFeedsApi->get_syndicated_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **video_id** | **str**| limit listing to a specific video | [optional] 
 **account_id** | **str**| limit listing to a specific account | [optional] 
 **account_name** | **str**| limit listing to a specific account | [optional] 
 **video_channel_id** | **str**| limit listing to a specific video channel | [optional] 
 **video_channel_name** | **str**| limit listing to a specific video channel | [optional] 

### Return type

[**List[VideoCommentsForXMLInner]**](VideoCommentsForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/rss+xml, text/xml, application/atom+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Cache-Control -  <br>  |
**400** | Arises when:   - videoId filter is mixed with a channel filter  |  -  |
**404** | video, video channel or account not found |  -  |
**406** | accept header unsupported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syndicated_subscription_videos**
> List[VideosForXMLInner] get_syndicated_subscription_videos(format, account_id, token, sort=sort, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files)

Videos of subscriptions feeds

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.videos_for_xml_inner import VideosForXMLInner
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
    api_instance = peertube_api_client.VideoFeedsApi(api_client)
    format = 'format_example' # str | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    account_id = 'account_id_example' # str | limit listing to a specific account
    token = 'token_example' # str | private token allowing access
    sort = '-createdAt' # str | Sort column (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)

    try:
        # Videos of subscriptions feeds
        api_response = api_instance.get_syndicated_subscription_videos(format, account_id, token, sort=sort, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files)
        print("The response of VideoFeedsApi->get_syndicated_subscription_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoFeedsApi->get_syndicated_subscription_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **account_id** | **str**| limit listing to a specific account | 
 **token** | **str**| private token allowing access | 
 **sort** | **str**| Sort column | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 

### Return type

[**List[VideosForXMLInner]**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/rss+xml, text/xml, application/atom+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Cache-Control -  <br>  |
**406** | accept header unsupported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_syndicated_videos**
> List[VideosForXMLInner] get_syndicated_videos(format, account_id=account_id, account_name=account_name, video_channel_id=video_channel_id, video_channel_name=video_channel_name, sort=sort, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files)

Common videos feeds

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.videos_for_xml_inner import VideosForXMLInner
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
    api_instance = peertube_api_client.VideoFeedsApi(api_client)
    format = 'format_example' # str | format expected (we focus on making `rss` the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss))
    account_id = 'account_id_example' # str | limit listing to a specific account (optional)
    account_name = 'account_name_example' # str | limit listing to a specific account (optional)
    video_channel_id = 'video_channel_id_example' # str | limit listing to a specific video channel (optional)
    video_channel_name = 'video_channel_name_example' # str | limit listing to a specific video channel (optional)
    sort = '-createdAt' # str | Sort column (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)

    try:
        # Common videos feeds
        api_response = api_instance.get_syndicated_videos(format, account_id=account_id, account_name=account_name, video_channel_id=video_channel_id, video_channel_name=video_channel_name, sort=sort, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files)
        print("The response of VideoFeedsApi->get_syndicated_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoFeedsApi->get_syndicated_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| format expected (we focus on making &#x60;rss&#x60; the most featureful ; it serves [Media RSS](https://www.rssboard.org/media-rss)) | 
 **account_id** | **str**| limit listing to a specific account | [optional] 
 **account_name** | **str**| limit listing to a specific account | [optional] 
 **video_channel_id** | **str**| limit listing to a specific video channel | [optional] 
 **video_channel_name** | **str**| limit listing to a specific video channel | [optional] 
 **sort** | **str**| Sort column | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 

### Return type

[**List[VideosForXMLInner]**](VideosForXMLInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/rss+xml, text/xml, application/atom+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Cache-Control -  <br>  |
**404** | video channel or account not found |  -  |
**406** | accept header unsupported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_videos_podcast_feed**
> get_videos_podcast_feed(video_channel_id)

Videos podcast feed

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
    api_instance = peertube_api_client.VideoFeedsApi(api_client)
    video_channel_id = 'video_channel_id_example' # str | Limit listing to a specific video channel

    try:
        # Videos podcast feed
        api_instance.get_videos_podcast_feed(video_channel_id)
    except Exception as e:
        print("Exception when calling VideoFeedsApi->get_videos_podcast_feed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_channel_id** | **str**| Limit listing to a specific video channel | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Cache-Control -  <br>  |
**404** | video channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

