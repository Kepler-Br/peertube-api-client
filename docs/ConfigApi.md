# peertube_api_client.ConfigApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_custom_config**](ConfigApi.md#del_custom_config) | **DELETE** /api/v1/config/custom | Delete instance runtime configuration
[**get_about**](ConfigApi.md#get_about) | **GET** /api/v1/config/about | Get instance \&quot;About\&quot; information
[**get_config**](ConfigApi.md#get_config) | **GET** /api/v1/config | Get instance public configuration
[**get_custom_config**](ConfigApi.md#get_custom_config) | **GET** /api/v1/config/custom | Get instance runtime configuration
[**put_custom_config**](ConfigApi.md#put_custom_config) | **PUT** /api/v1/config/custom | Set instance runtime configuration


# **del_custom_config**
> del_custom_config()

Delete instance runtime configuration

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
    api_instance = peertube_api_client.ConfigApi(api_client)

    try:
        # Delete instance runtime configuration
        api_instance.del_custom_config()
    except Exception as e:
        print("Exception when calling ConfigApi->del_custom_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_about**
> ServerConfigAbout get_about()

Get instance \"About\" information

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.server_config_about import ServerConfigAbout
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
    api_instance = peertube_api_client.ConfigApi(api_client)

    try:
        # Get instance \"About\" information
        api_response = api_instance.get_about()
        print("The response of ConfigApi->get_about:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_about: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerConfigAbout**](ServerConfigAbout.md)

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

# **get_config**
> ServerConfig get_config()

Get instance public configuration

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.server_config import ServerConfig
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
    api_instance = peertube_api_client.ConfigApi(api_client)

    try:
        # Get instance public configuration
        api_response = api_instance.get_config()
        print("The response of ConfigApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerConfig**](ServerConfig.md)

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

# **get_custom_config**
> ServerConfigCustom get_custom_config()

Get instance runtime configuration

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.server_config_custom import ServerConfigCustom
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
    api_instance = peertube_api_client.ConfigApi(api_client)

    try:
        # Get instance runtime configuration
        api_response = api_instance.get_custom_config()
        print("The response of ConfigApi->get_custom_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->get_custom_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerConfigCustom**](ServerConfigCustom.md)

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

# **put_custom_config**
> put_custom_config()

Set instance runtime configuration

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
    api_instance = peertube_api_client.ConfigApi(api_client)

    try:
        # Set instance runtime configuration
        api_instance.put_custom_config()
    except Exception as e:
        print("Exception when calling ConfigApi->put_custom_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**400** | Arises when:   - the emailer is disabled and the instance is open to registrations   - webtorrent and hls are disabled with transcoding enabled - you need at least one enabled  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

