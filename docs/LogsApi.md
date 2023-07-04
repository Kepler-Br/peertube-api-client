# peertube_api_client.LogsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instance_audit_logs**](LogsApi.md#get_instance_audit_logs) | **GET** /api/v1/server/audit-logs | Get instance audit logs
[**get_instance_logs**](LogsApi.md#get_instance_logs) | **GET** /api/v1/server/logs | Get instance logs
[**send_client_log**](LogsApi.md#send_client_log) | **POST** /api/v1/server/logs/client | Send client log


# **get_instance_audit_logs**
> List[str] get_instance_audit_logs()

Get instance audit logs

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
    api_instance = peertube_api_client.LogsApi(api_client)

    try:
        # Get instance audit logs
        api_response = api_instance.get_instance_audit_logs()
        print("The response of LogsApi->get_instance_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_instance_audit_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_instance_logs**
> List[str] get_instance_logs()

Get instance logs

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
    api_instance = peertube_api_client.LogsApi(api_client)

    try:
        # Get instance logs
        api_response = api_instance.get_instance_logs()
        print("The response of LogsApi->get_instance_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->get_instance_logs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **send_client_log**
> send_client_log(send_client_log=send_client_log)

Send client log

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.send_client_log import SendClientLog
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
    api_instance = peertube_api_client.LogsApi(api_client)
    send_client_log = peertube_api_client.SendClientLog() # SendClientLog |  (optional)

    try:
        # Send client log
        api_instance.send_client_log(send_client_log=send_client_log)
    except Exception as e:
        print("Exception when calling LogsApi->send_client_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_client_log** | [**SendClientLog**](SendClientLog.md)|  | [optional] 

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

