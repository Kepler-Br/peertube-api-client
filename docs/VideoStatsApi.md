# peertube_api_client.VideoStatsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_videos_id_stats_overall_get**](VideoStatsApi.md#api_v1_videos_id_stats_overall_get) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video
[**api_v1_videos_id_stats_retention_get**](VideoStatsApi.md#api_v1_videos_id_stats_retention_get) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video
[**api_v1_videos_id_stats_timeseries_metric_get**](VideoStatsApi.md#api_v1_videos_id_stats_timeseries_metric_get) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video


# **api_v1_videos_id_stats_overall_get**
> VideoStatsOverall api_v1_videos_id_stats_overall_get(id, start_date=start_date, end_date=end_date)

Get overall stats of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_stats_overall import VideoStatsOverall
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
    api_instance = peertube_api_client.VideoStatsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter stats by start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter stats by end date (optional)

    try:
        # Get overall stats of a video
        api_response = api_instance.api_v1_videos_id_stats_overall_get(id, start_date=start_date, end_date=end_date)
        print("The response of VideoStatsApi->api_v1_videos_id_stats_overall_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoStatsApi->api_v1_videos_id_stats_overall_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **start_date** | **datetime**| Filter stats by start date | [optional] 
 **end_date** | **datetime**| Filter stats by end date | [optional] 

### Return type

[**VideoStatsOverall**](VideoStatsOverall.md)

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

# **api_v1_videos_id_stats_retention_get**
> VideoStatsRetention api_v1_videos_id_stats_retention_get(id)

Get retention stats of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_stats_retention import VideoStatsRetention
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
    api_instance = peertube_api_client.VideoStatsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Get retention stats of a video
        api_response = api_instance.api_v1_videos_id_stats_retention_get(id)
        print("The response of VideoStatsApi->api_v1_videos_id_stats_retention_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoStatsApi->api_v1_videos_id_stats_retention_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**VideoStatsRetention**](VideoStatsRetention.md)

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

# **api_v1_videos_id_stats_timeseries_metric_get**
> VideoStatsTimeserie api_v1_videos_id_stats_timeseries_metric_get(id, metric, start_date=start_date, end_date=end_date)

Get timeserie stats of a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_stats_timeserie import VideoStatsTimeserie
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
    api_instance = peertube_api_client.VideoStatsApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    metric = 'metric_example' # str | The metric to get
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter stats by start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter stats by end date (optional)

    try:
        # Get timeserie stats of a video
        api_response = api_instance.api_v1_videos_id_stats_timeseries_metric_get(id, metric, start_date=start_date, end_date=end_date)
        print("The response of VideoStatsApi->api_v1_videos_id_stats_timeseries_metric_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoStatsApi->api_v1_videos_id_stats_timeseries_metric_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **metric** | **str**| The metric to get | 
 **start_date** | **datetime**| Filter stats by start date | [optional] 
 **end_date** | **datetime**| Filter stats by end date | [optional] 

### Return type

[**VideoStatsTimeserie**](VideoStatsTimeserie.md)

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

