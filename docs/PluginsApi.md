# peertube_api_client.PluginsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_plugin**](PluginsApi.md#add_plugin) | **POST** /api/v1/plugins/install | Install a plugin
[**api_v1_plugins_npm_name_public_settings_get**](PluginsApi.md#api_v1_plugins_npm_name_public_settings_get) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings
[**api_v1_plugins_npm_name_registered_settings_get**](PluginsApi.md#api_v1_plugins_npm_name_registered_settings_get) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings
[**api_v1_plugins_npm_name_settings_put**](PluginsApi.md#api_v1_plugins_npm_name_settings_put) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings
[**get_available_plugins**](PluginsApi.md#get_available_plugins) | **GET** /api/v1/plugins/available | List available plugins
[**get_plugin**](PluginsApi.md#get_plugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin
[**get_plugins**](PluginsApi.md#get_plugins) | **GET** /api/v1/plugins | List plugins
[**uninstall_plugin**](PluginsApi.md#uninstall_plugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin
[**update_plugin**](PluginsApi.md#update_plugin) | **POST** /api/v1/plugins/update | Update a plugin


# **add_plugin**
> add_plugin(add_plugin_request=add_plugin_request)

Install a plugin

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_plugin_request import AddPluginRequest
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    add_plugin_request = peertube_api_client.AddPluginRequest() # AddPluginRequest |  (optional)

    try:
        # Install a plugin
        api_instance.add_plugin(add_plugin_request=add_plugin_request)
    except Exception as e:
        print("Exception when calling PluginsApi->add_plugin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_plugin_request** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] 

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
**400** | should have either &#x60;npmName&#x60; or &#x60;path&#x60; set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_plugins_npm_name_public_settings_get**
> Dict[str, object] api_v1_plugins_npm_name_public_settings_get(npm_name)

Get a plugin's public settings

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
    api_instance = peertube_api_client.PluginsApi(api_client)
    npm_name = 'peertube-plugin-auth-ldap' # str | name of the plugin/theme on npmjs.com or in its package.json

    try:
        # Get a plugin's public settings
        api_response = api_instance.api_v1_plugins_npm_name_public_settings_get(npm_name)
        print("The response of PluginsApi->api_v1_plugins_npm_name_public_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->api_v1_plugins_npm_name_public_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_name** | **str**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_plugins_npm_name_registered_settings_get**
> Dict[str, object] api_v1_plugins_npm_name_registered_settings_get(npm_name)

Get a plugin's registered settings

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
    api_instance = peertube_api_client.PluginsApi(api_client)
    npm_name = 'peertube-plugin-auth-ldap' # str | name of the plugin/theme on npmjs.com or in its package.json

    try:
        # Get a plugin's registered settings
        api_response = api_instance.api_v1_plugins_npm_name_registered_settings_get(npm_name)
        print("The response of PluginsApi->api_v1_plugins_npm_name_registered_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->api_v1_plugins_npm_name_registered_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_name** | **str**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

**Dict[str, object]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_plugins_npm_name_settings_put**
> api_v1_plugins_npm_name_settings_put(npm_name, api_v1_plugins_npm_name_settings_put_request=api_v1_plugins_npm_name_settings_put_request)

Set a plugin's settings

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_plugins_npm_name_settings_put_request import ApiV1PluginsNpmNameSettingsPutRequest
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    npm_name = 'peertube-plugin-auth-ldap' # str | name of the plugin/theme on npmjs.com or in its package.json
    api_v1_plugins_npm_name_settings_put_request = peertube_api_client.ApiV1PluginsNpmNameSettingsPutRequest() # ApiV1PluginsNpmNameSettingsPutRequest |  (optional)

    try:
        # Set a plugin's settings
        api_instance.api_v1_plugins_npm_name_settings_put(npm_name, api_v1_plugins_npm_name_settings_put_request=api_v1_plugins_npm_name_settings_put_request)
    except Exception as e:
        print("Exception when calling PluginsApi->api_v1_plugins_npm_name_settings_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_name** | **str**| name of the plugin/theme on npmjs.com or in its package.json | 
 **api_v1_plugins_npm_name_settings_put_request** | [**ApiV1PluginsNpmNameSettingsPutRequest**](ApiV1PluginsNpmNameSettingsPutRequest.md)|  | [optional] 

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
**404** | plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_plugins**
> PluginResponse get_available_plugins(search=search, plugin_type=plugin_type, current_peer_tube_engine=current_peer_tube_engine, start=start, count=count, sort=sort)

List available plugins

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.plugin_response import PluginResponse
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    search = 'search_example' # str |  (optional)
    plugin_type = 56 # int |  (optional)
    current_peer_tube_engine = 'current_peer_tube_engine_example' # str |  (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List available plugins
        api_response = api_instance.get_available_plugins(search=search, plugin_type=plugin_type, current_peer_tube_engine=current_peer_tube_engine, start=start, count=count, sort=sort)
        print("The response of PluginsApi->get_available_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_available_plugins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 
 **plugin_type** | **int**|  | [optional] 
 **current_peer_tube_engine** | **str**|  | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**503** | plugin index unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin**
> Plugin get_plugin(npm_name)

Get a plugin

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.plugin import Plugin
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    npm_name = 'peertube-plugin-auth-ldap' # str | name of the plugin/theme on npmjs.com or in its package.json

    try:
        # Get a plugin
        api_response = api_instance.get_plugin(npm_name)
        print("The response of PluginsApi->get_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_name** | **str**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins**
> PluginResponse get_plugins(plugin_type=plugin_type, uninstalled=uninstalled, start=start, count=count, sort=sort)

List plugins

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.plugin_response import PluginResponse
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    plugin_type = 56 # int |  (optional)
    uninstalled = True # bool |  (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List plugins
        api_response = api_instance.get_plugins(plugin_type=plugin_type, uninstalled=uninstalled, start=start, count=count, sort=sort)
        print("The response of PluginsApi->get_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_type** | **int**|  | [optional] 
 **uninstalled** | **bool**|  | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**PluginResponse**](PluginResponse.md)

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

# **uninstall_plugin**
> uninstall_plugin(uninstall_plugin_request=uninstall_plugin_request)

Uninstall a plugin

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.uninstall_plugin_request import UninstallPluginRequest
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    uninstall_plugin_request = peertube_api_client.UninstallPluginRequest() # UninstallPluginRequest |  (optional)

    try:
        # Uninstall a plugin
        api_instance.uninstall_plugin(uninstall_plugin_request=uninstall_plugin_request)
    except Exception as e:
        print("Exception when calling PluginsApi->uninstall_plugin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uninstall_plugin_request** | [**UninstallPluginRequest**](UninstallPluginRequest.md)|  | [optional] 

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
**404** | existing plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin**
> update_plugin(add_plugin_request=add_plugin_request)

Update a plugin

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_plugin_request import AddPluginRequest
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
    api_instance = peertube_api_client.PluginsApi(api_client)
    add_plugin_request = peertube_api_client.AddPluginRequest() # AddPluginRequest |  (optional)

    try:
        # Update a plugin
        api_instance.update_plugin(add_plugin_request=add_plugin_request)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_plugin_request** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] 

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
**400** | should have either &#x60;npmName&#x60; or &#x60;path&#x60; set |  -  |
**404** | existing plugin not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

