# peertube_api_client.AccountsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_accounts_name_ratings_get**](AccountsApi.md#api_v1_accounts_name_ratings_get) | **GET** /api/v1/accounts/{name}/ratings | List ratings of an account
[**api_v1_accounts_name_video_channel_syncs_get**](AccountsApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**api_v1_accounts_name_video_channels_get**](AccountsApi.md#api_v1_accounts_name_video_channels_get) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
[**api_v1_accounts_name_video_playlists_get**](AccountsApi.md#api_v1_accounts_name_video_playlists_get) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
[**get_account**](AccountsApi.md#get_account) | **GET** /api/v1/accounts/{name} | Get an account
[**get_account_followers**](AccountsApi.md#get_account_followers) | **GET** /api/v1/accounts/{name}/followers | List followers of an account
[**get_account_videos**](AccountsApi.md#get_account_videos) | **GET** /api/v1/accounts/{name}/videos | List videos of an account
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /api/v1/accounts | List accounts


# **api_v1_accounts_name_ratings_get**
> List[VideoRating] api_v1_accounts_name_ratings_get(name, start=start, count=count, sort=sort, rating=rating)

List ratings of an account

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_rating import VideoRating
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    rating = 'rating_example' # str | Optionally filter which ratings to retrieve (optional)

    try:
        # List ratings of an account
        api_response = api_instance.api_v1_accounts_name_ratings_get(name, start=start, count=count, sort=sort, rating=rating)
        print("The response of AccountsApi->api_v1_accounts_name_ratings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->api_v1_accounts_name_ratings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **rating** | **str**| Optionally filter which ratings to retrieve | [optional] 

### Return type

[**List[VideoRating]**](VideoRating.md)

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

# **api_v1_accounts_name_video_channel_syncs_get**
> VideoChannelSyncList api_v1_accounts_name_video_channel_syncs_get(name, start=start, count=count, sort=sort)

List the synchronizations of video channels of an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_sync_list import VideoChannelSyncList
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List the synchronizations of video channels of an account
        api_response = api_instance.api_v1_accounts_name_video_channel_syncs_get(name, start=start, count=count, sort=sort)
        print("The response of AccountsApi->api_v1_accounts_name_video_channel_syncs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->api_v1_accounts_name_video_channel_syncs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelSyncList**](VideoChannelSyncList.md)

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

# **api_v1_accounts_name_video_channels_get**
> VideoChannelList api_v1_accounts_name_video_channels_get(name, with_stats=with_stats, start=start, count=count, sort=sort)

List video channels of an account

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    with_stats = True # bool | include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List video channels of an account
        api_response = api_instance.api_v1_accounts_name_video_channels_get(name, with_stats=with_stats, start=start, count=count, sort=sort)
        print("The response of AccountsApi->api_v1_accounts_name_video_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->api_v1_accounts_name_video_channels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **with_stats** | **bool**| include daily view statistics for the last 30 days and total views (only if authentified as the account user) | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelList**](VideoChannelList.md)

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

# **api_v1_accounts_name_video_playlists_get**
> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response api_v1_accounts_name_video_playlists_get(name, start=start, count=count, sort=sort, search=search, playlist_type=playlist_type)

List playlists of an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_video_channels_channel_handle_video_playlists_get200_response import ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
from peertube_api_client.models.video_playlist_type_set import VideoPlaylistTypeSet
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)
    playlist_type = peertube_api_client.VideoPlaylistTypeSet() # VideoPlaylistTypeSet |  (optional)

    try:
        # List playlists of an account
        api_response = api_instance.api_v1_accounts_name_video_playlists_get(name, start=start, count=count, sort=sort, search=search, playlist_type=playlist_type)
        print("The response of AccountsApi->api_v1_accounts_name_video_playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->api_v1_accounts_name_video_playlists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 
 **playlist_type** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response**](ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response.md)

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

# **get_account**
> Account get_account(name)

Get an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.account import Account
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account

    try:
        # Get an account
        api_response = api_instance.get_account(name)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | account not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_followers**
> GetAccountFollowers200Response get_account_followers(name, start=start, count=count, sort=sort, search=search)

List followers of an account

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_account_followers200_response import GetAccountFollowers200Response
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort followers by criteria (optional)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)

    try:
        # List followers of an account
        api_response = api_instance.get_account_followers(name, start=start, count=count, sort=sort, search=search)
        print("The response of AccountsApi->get_account_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort followers by criteria | [optional] 
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

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
    api_instance = peertube_api_client.AccountsApi(api_client)
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
        print("The response of AccountsApi->get_account_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_videos: %s\n" % e)
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

# **get_accounts**
> GetAccounts200Response get_accounts(start=start, count=count, sort=sort)

List accounts

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_accounts200_response import GetAccounts200Response
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
    api_instance = peertube_api_client.AccountsApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List accounts
        api_response = api_instance.get_accounts(start=start, count=count, sort=sort)
        print("The response of AccountsApi->get_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**GetAccounts200Response**](GetAccounts200Response.md)

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

