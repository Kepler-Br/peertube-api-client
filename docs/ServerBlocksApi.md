# peertube_api_client.ServerBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_blocklist_status_get**](ServerBlocksApi.md#api_v1_blocklist_status_get) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
[**api_v1_server_blocklist_servers_get**](ServerBlocksApi.md#api_v1_server_blocklist_servers_get) | **GET** /api/v1/server/blocklist/servers | List server blocks
[**api_v1_server_blocklist_servers_host_delete**](ServerBlocksApi.md#api_v1_server_blocklist_servers_host_delete) | **DELETE** /api/v1/server/blocklist/servers/{host} | Unblock a server by its domain
[**api_v1_server_blocklist_servers_post**](ServerBlocksApi.md#api_v1_server_blocklist_servers_post) | **POST** /api/v1/server/blocklist/servers | Block a server


# **api_v1_blocklist_status_get**
> BlockStatus api_v1_blocklist_status_get(accounts=accounts, hosts=hosts)

Get block status of accounts/hosts

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.block_status import BlockStatus
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
    api_instance = peertube_api_client.ServerBlocksApi(api_client)
    accounts = ['[\"goofy@example.com\",\"donald@example.com\"]'] # List[str] | Check if these accounts are blocked (optional)
    hosts = ['[\"example.com\"]'] # List[str] | Check if these hosts are blocked (optional)

    try:
        # Get block status of accounts/hosts
        api_response = api_instance.api_v1_blocklist_status_get(accounts=accounts, hosts=hosts)
        print("The response of ServerBlocksApi->api_v1_blocklist_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerBlocksApi->api_v1_blocklist_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | [**List[str]**](str.md)| Check if these accounts are blocked | [optional] 
 **hosts** | [**List[str]**](str.md)| Check if these hosts are blocked | [optional] 

### Return type

[**BlockStatus**](BlockStatus.md)

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

# **api_v1_server_blocklist_servers_get**
> api_v1_server_blocklist_servers_get(start=start, count=count, sort=sort)

List server blocks

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
    api_instance = peertube_api_client.ServerBlocksApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List server blocks
        api_instance.api_v1_server_blocklist_servers_get(start=start, count=count, sort=sort)
    except Exception as e:
        print("Exception when calling ServerBlocksApi->api_v1_server_blocklist_servers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

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

# **api_v1_server_blocklist_servers_host_delete**
> api_v1_server_blocklist_servers_host_delete(host)

Unblock a server by its domain

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
    api_instance = peertube_api_client.ServerBlocksApi(api_client)
    host = 'host_example' # str | server domain to unblock

    try:
        # Unblock a server by its domain
        api_instance.api_v1_server_blocklist_servers_host_delete(host)
    except Exception as e:
        print("Exception when calling ServerBlocksApi->api_v1_server_blocklist_servers_host_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| server domain to unblock | 

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
**404** | account block does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_blocklist_servers_post**
> api_v1_server_blocklist_servers_post(api_v1_server_blocklist_servers_post_request=api_v1_server_blocklist_servers_post_request)

Block a server

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_server_blocklist_servers_post_request import ApiV1ServerBlocklistServersPostRequest
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
    api_instance = peertube_api_client.ServerBlocksApi(api_client)
    api_v1_server_blocklist_servers_post_request = peertube_api_client.ApiV1ServerBlocklistServersPostRequest() # ApiV1ServerBlocklistServersPostRequest |  (optional)

    try:
        # Block a server
        api_instance.api_v1_server_blocklist_servers_post(api_v1_server_blocklist_servers_post_request=api_v1_server_blocklist_servers_post_request)
    except Exception as e:
        print("Exception when calling ServerBlocksApi->api_v1_server_blocklist_servers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_server_blocklist_servers_post_request** | [**ApiV1ServerBlocklistServersPostRequest**](ApiV1ServerBlocklistServersPostRequest.md)|  | [optional] 

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
**409** | self-blocking forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

