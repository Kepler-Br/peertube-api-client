# peertube_api_client.VideoCommentsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_videos_id_comment_threads_get**](VideoCommentsApi.md#api_v1_videos_id_comment_threads_get) | **GET** /api/v1/videos/{id}/comment-threads | List threads of a video
[**api_v1_videos_id_comment_threads_post**](VideoCommentsApi.md#api_v1_videos_id_comment_threads_post) | **POST** /api/v1/videos/{id}/comment-threads | Create a thread
[**api_v1_videos_id_comment_threads_thread_id_get**](VideoCommentsApi.md#api_v1_videos_id_comment_threads_thread_id_get) | **GET** /api/v1/videos/{id}/comment-threads/{threadId} | Get a thread
[**api_v1_videos_id_comments_comment_id_delete**](VideoCommentsApi.md#api_v1_videos_id_comments_comment_id_delete) | **DELETE** /api/v1/videos/{id}/comments/{commentId} | Delete a comment or a reply
[**api_v1_videos_id_comments_comment_id_post**](VideoCommentsApi.md#api_v1_videos_id_comments_comment_id_post) | **POST** /api/v1/videos/{id}/comments/{commentId} | Reply to a thread of a video


# **api_v1_videos_id_comment_threads_get**
> CommentThreadResponse api_v1_videos_id_comment_threads_get(id, start=start, count=count, sort=sort)

List threads of a video

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.comment_thread_response import CommentThreadResponse
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
    api_instance = peertube_api_client.VideoCommentsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort comments by criteria (optional)

    try:
        # List threads of a video
        api_response = api_instance.api_v1_videos_id_comment_threads_get(id, start=start, count=count, sort=sort)
        print("The response of VideoCommentsApi->api_v1_videos_id_comment_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoCommentsApi->api_v1_videos_id_comment_threads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort comments by criteria | [optional] 

### Return type

[**CommentThreadResponse**](CommentThreadResponse.md)

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

# **api_v1_videos_id_comment_threads_post**
> CommentThreadPostResponse api_v1_videos_id_comment_threads_post(id, api_v1_videos_id_comment_threads_post_request=api_v1_videos_id_comment_threads_post_request)

Create a thread

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_videos_id_comment_threads_post_request import ApiV1VideosIdCommentThreadsPostRequest
from peertube_api_client.models.comment_thread_post_response import CommentThreadPostResponse
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
    api_instance = peertube_api_client.VideoCommentsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    api_v1_videos_id_comment_threads_post_request = peertube_api_client.ApiV1VideosIdCommentThreadsPostRequest() # ApiV1VideosIdCommentThreadsPostRequest |  (optional)

    try:
        # Create a thread
        api_response = api_instance.api_v1_videos_id_comment_threads_post(id, api_v1_videos_id_comment_threads_post_request=api_v1_videos_id_comment_threads_post_request)
        print("The response of VideoCommentsApi->api_v1_videos_id_comment_threads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoCommentsApi->api_v1_videos_id_comment_threads_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **api_v1_videos_id_comment_threads_post_request** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] 

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | video does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_id_comment_threads_thread_id_get**
> VideoCommentThreadTree api_v1_videos_id_comment_threads_thread_id_get(id, thread_id)

Get a thread

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_comment_thread_tree import VideoCommentThreadTree
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
    api_instance = peertube_api_client.VideoCommentsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    thread_id = 56 # int | The thread id (root comment id)

    try:
        # Get a thread
        api_response = api_instance.api_v1_videos_id_comment_threads_thread_id_get(id, thread_id)
        print("The response of VideoCommentsApi->api_v1_videos_id_comment_threads_thread_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoCommentsApi->api_v1_videos_id_comment_threads_thread_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **thread_id** | **int**| The thread id (root comment id) | 

### Return type

[**VideoCommentThreadTree**](VideoCommentThreadTree.md)

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

# **api_v1_videos_id_comments_comment_id_delete**
> api_v1_videos_id_comments_comment_id_delete(id, comment_id)

Delete a comment or a reply

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
    api_instance = peertube_api_client.VideoCommentsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    comment_id = 56 # int | The comment id

    try:
        # Delete a comment or a reply
        api_instance.api_v1_videos_id_comments_comment_id_delete(id, comment_id)
    except Exception as e:
        print("Exception when calling VideoCommentsApi->api_v1_videos_id_comments_comment_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **comment_id** | **int**| The comment id | 

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
**403** | cannot remove comment of another user |  -  |
**404** | comment or video does not exist |  -  |
**409** | comment is already deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_id_comments_comment_id_post**
> CommentThreadPostResponse api_v1_videos_id_comments_comment_id_post(id, comment_id, api_v1_videos_id_comment_threads_post_request=api_v1_videos_id_comment_threads_post_request)

Reply to a thread of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_videos_id_comment_threads_post_request import ApiV1VideosIdCommentThreadsPostRequest
from peertube_api_client.models.comment_thread_post_response import CommentThreadPostResponse
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
    api_instance = peertube_api_client.VideoCommentsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    comment_id = 56 # int | The comment id
    api_v1_videos_id_comment_threads_post_request = peertube_api_client.ApiV1VideosIdCommentThreadsPostRequest() # ApiV1VideosIdCommentThreadsPostRequest |  (optional)

    try:
        # Reply to a thread of a video
        api_response = api_instance.api_v1_videos_id_comments_comment_id_post(id, comment_id, api_v1_videos_id_comment_threads_post_request=api_v1_videos_id_comment_threads_post_request)
        print("The response of VideoCommentsApi->api_v1_videos_id_comments_comment_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoCommentsApi->api_v1_videos_id_comments_comment_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **comment_id** | **int**| The comment id | 
 **api_v1_videos_id_comment_threads_post_request** | [**ApiV1VideosIdCommentThreadsPostRequest**](ApiV1VideosIdCommentThreadsPostRequest.md)|  | [optional] 

### Return type

[**CommentThreadPostResponse**](CommentThreadPostResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | thread or video does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

