# peertube_api_client.AccountBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_blocklist_status_get**](AccountBlocksApi.md#api_v1_blocklist_status_get) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
[**api_v1_server_blocklist_accounts_account_name_delete**](AccountBlocksApi.md#api_v1_server_blocklist_accounts_account_name_delete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle
[**api_v1_server_blocklist_accounts_get**](AccountBlocksApi.md#api_v1_server_blocklist_accounts_get) | **GET** /api/v1/server/blocklist/accounts | List account blocks
[**api_v1_server_blocklist_accounts_post**](AccountBlocksApi.md#api_v1_server_blocklist_accounts_post) | **POST** /api/v1/server/blocklist/accounts | Block an account


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
    api_instance = peertube_api_client.AccountBlocksApi(api_client)
    accounts = ['[\"goofy@example.com\",\"donald@example.com\"]'] # List[str] | Check if these accounts are blocked (optional)
    hosts = ['[\"example.com\"]'] # List[str] | Check if these hosts are blocked (optional)

    try:
        # Get block status of accounts/hosts
        api_response = api_instance.api_v1_blocklist_status_get(accounts=accounts, hosts=hosts)
        print("The response of AccountBlocksApi->api_v1_blocklist_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountBlocksApi->api_v1_blocklist_status_get: %s\n" % e)
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

# **api_v1_server_blocklist_accounts_account_name_delete**
> api_v1_server_blocklist_accounts_account_name_delete(account_name)

Unblock an account by its handle

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
    api_instance = peertube_api_client.AccountBlocksApi(api_client)
    account_name = 'account_name_example' # str | account to unblock, in the form `username@domain`

    try:
        # Unblock an account by its handle
        api_instance.api_v1_server_blocklist_accounts_account_name_delete(account_name)
    except Exception as e:
        print("Exception when calling AccountBlocksApi->api_v1_server_blocklist_accounts_account_name_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| account to unblock, in the form &#x60;username@domain&#x60; | 

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
**201** | successful operation |  -  |
**404** | account or account block does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_blocklist_accounts_get**
> api_v1_server_blocklist_accounts_get(start=start, count=count, sort=sort)

List account blocks

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
    api_instance = peertube_api_client.AccountBlocksApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List account blocks
        api_instance.api_v1_server_blocklist_accounts_get(start=start, count=count, sort=sort)
    except Exception as e:
        print("Exception when calling AccountBlocksApi->api_v1_server_blocklist_accounts_get: %s\n" % e)
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

# **api_v1_server_blocklist_accounts_post**
> api_v1_server_blocklist_accounts_post(api_v1_server_blocklist_accounts_post_request=api_v1_server_blocklist_accounts_post_request)

Block an account

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_server_blocklist_accounts_post_request import ApiV1ServerBlocklistAccountsPostRequest
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
    api_instance = peertube_api_client.AccountBlocksApi(api_client)
    api_v1_server_blocklist_accounts_post_request = peertube_api_client.ApiV1ServerBlocklistAccountsPostRequest() # ApiV1ServerBlocklistAccountsPostRequest |  (optional)

    try:
        # Block an account
        api_instance.api_v1_server_blocklist_accounts_post(api_v1_server_blocklist_accounts_post_request=api_v1_server_blocklist_accounts_post_request)
    except Exception as e:
        print("Exception when calling AccountBlocksApi->api_v1_server_blocklist_accounts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_server_blocklist_accounts_post_request** | [**ApiV1ServerBlocklistAccountsPostRequest**](ApiV1ServerBlocklistAccountsPostRequest.md)|  | [optional] 

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
**409** | self-blocking forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

