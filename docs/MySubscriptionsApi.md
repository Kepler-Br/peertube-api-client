# peertube_api_client.MySubscriptionsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_me_subscriptions_exist_get**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_exist_get) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user
[**api_v1_users_me_subscriptions_get**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_get) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions
[**api_v1_users_me_subscriptions_post**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_post) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user
[**api_v1_users_me_subscriptions_subscription_handle_delete**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_subscription_handle_delete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user
[**api_v1_users_me_subscriptions_subscription_handle_get**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_subscription_handle_get) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user
[**api_v1_users_me_subscriptions_videos_get**](MySubscriptionsApi.md#api_v1_users_me_subscriptions_videos_get) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user


# **api_v1_users_me_subscriptions_exist_get**
> object api_v1_users_me_subscriptions_exist_get(uris)

Get if subscriptions exist for my user

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
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
    uris = ['uris_example'] # List[str] | list of uris to check if each is part of the user subscriptions

    try:
        # Get if subscriptions exist for my user
        api_response = api_instance.api_v1_users_me_subscriptions_exist_get(uris)
        print("The response of MySubscriptionsApi->api_v1_users_me_subscriptions_exist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_exist_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**List[str]**](str.md)| list of uris to check if each is part of the user subscriptions | 

### Return type

**object**

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

# **api_v1_users_me_subscriptions_get**
> VideoChannelList api_v1_users_me_subscriptions_get(start=start, count=count, sort=sort)

Get my user subscriptions

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_list import VideoChannelList
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
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # Get my user subscriptions
        api_response = api_instance.api_v1_users_me_subscriptions_get(start=start, count=count, sort=sort)
        print("The response of MySubscriptionsApi->api_v1_users_me_subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelList**](VideoChannelList.md)

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

# **api_v1_users_me_subscriptions_post**
> api_v1_users_me_subscriptions_post(api_v1_users_me_subscriptions_post_request=api_v1_users_me_subscriptions_post_request)

Add subscription to my user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_subscriptions_post_request import ApiV1UsersMeSubscriptionsPostRequest
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
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
    api_v1_users_me_subscriptions_post_request = {"uri":"008a0e54-375d-49d0-8379-143202e24152@video.lqdn.fr"} # ApiV1UsersMeSubscriptionsPostRequest |  (optional)

    try:
        # Add subscription to my user
        api_instance.api_v1_users_me_subscriptions_post(api_v1_users_me_subscriptions_post_request=api_v1_users_me_subscriptions_post_request)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_users_me_subscriptions_post_request** | [**ApiV1UsersMeSubscriptionsPostRequest**](ApiV1UsersMeSubscriptionsPostRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_me_subscriptions_subscription_handle_delete**
> api_v1_users_me_subscriptions_subscription_handle_delete(subscription_handle)

Delete subscription of my user

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
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
    subscription_handle = 'my_username | my_username@example.com' # str | The subscription handle

    try:
        # Delete subscription of my user
        api_instance.api_v1_users_me_subscriptions_subscription_handle_delete(subscription_handle)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_subscription_handle_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_handle** | **str**| The subscription handle | 

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
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_me_subscriptions_subscription_handle_get**
> VideoChannel api_v1_users_me_subscriptions_subscription_handle_get(subscription_handle)

Get subscription of my user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel import VideoChannel
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
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
    subscription_handle = 'my_username | my_username@example.com' # str | The subscription handle

    try:
        # Get subscription of my user
        api_response = api_instance.api_v1_users_me_subscriptions_subscription_handle_get(subscription_handle)
        print("The response of MySubscriptionsApi->api_v1_users_me_subscriptions_subscription_handle_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_subscription_handle_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_handle** | **str**| The subscription handle | 

### Return type

[**VideoChannel**](VideoChannel.md)

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

# **api_v1_users_me_subscriptions_videos_get**
> VideoListResponse api_v1_users_me_subscriptions_videos_get(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos of subscriptions of my user

### Example

* OAuth Authentication (OAuth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.MySubscriptionsApi(api_client)
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
        # List videos of subscriptions of my user
        api_response = api_instance.api_v1_users_me_subscriptions_videos_get(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of MySubscriptionsApi->api_v1_users_me_subscriptions_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MySubscriptionsApi->api_v1_users_me_subscriptions_videos_get: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

