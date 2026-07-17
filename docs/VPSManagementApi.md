# ha_sdk_python.VPSManagementApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vps_config**](VPSManagementApi.md#get_vps_config) | **POST** /vps/get-config | 
[**get_vps_details**](VPSManagementApi.md#get_vps_details) | **POST** /vps/get-details | 
[**list_isos**](VPSManagementApi.md#list_isos) | **POST** /vps/list-isos | 
[**list_reinstall_os**](VPSManagementApi.md#list_reinstall_os) | **POST** /vps/list-reinstall-images | 
[**list_vps_services**](VPSManagementApi.md#list_vps_services) | **POST** /vps/list-vps-services | 
[**mount_iso**](VPSManagementApi.md#mount_iso) | **POST** /vps/mount-iso | 
[**trigger_reinstall**](VPSManagementApi.md#trigger_reinstall) | **POST** /vps/trigger-reinstall | 
[**update_vps_config**](VPSManagementApi.md#update_vps_config) | **POST** /vps/update-config | 


# **get_vps_config**
> GetVpsConfigResponseContent get_vps_config(get_vps_config_request_content)

Retrieves VPS configuration settings including name, hostname, auto-start, boot order, and CD-ROM

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_vps_config_request_content import GetVpsConfigRequestContent
from ha_sdk_python.models.get_vps_config_response_content import GetVpsConfigResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    get_vps_config_request_content = ha_sdk_python.GetVpsConfigRequestContent() # GetVpsConfigRequestContent | 

    try:
        api_response = api_instance.get_vps_config(get_vps_config_request_content)
        print("The response of VPSManagementApi->get_vps_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->get_vps_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vps_config_request_content** | [**GetVpsConfigRequestContent**](GetVpsConfigRequestContent.md)|  | 

### Return type

[**GetVpsConfigResponseContent**](GetVpsConfigResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetVpsConfig 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vps_details**
> GetVpsDetailsResponseContent get_vps_details(get_vps_details_request_content)

Gets detailed information about a VPS service including configuration, network settings, and statistics

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_vps_details_request_content import GetVpsDetailsRequestContent
from ha_sdk_python.models.get_vps_details_response_content import GetVpsDetailsResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    get_vps_details_request_content = ha_sdk_python.GetVpsDetailsRequestContent() # GetVpsDetailsRequestContent | 

    try:
        api_response = api_instance.get_vps_details(get_vps_details_request_content)
        print("The response of VPSManagementApi->get_vps_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->get_vps_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vps_details_request_content** | [**GetVpsDetailsRequestContent**](GetVpsDetailsRequestContent.md)|  | 

### Return type

[**GetVpsDetailsResponseContent**](GetVpsDetailsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetVpsDetails 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_isos**
> ListIsosResponseContent list_isos(list_isos_request_content)

Retrieves the list of available ISO images for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_isos_request_content import ListIsosRequestContent
from ha_sdk_python.models.list_isos_response_content import ListIsosResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    list_isos_request_content = ha_sdk_python.ListIsosRequestContent() # ListIsosRequestContent | 

    try:
        api_response = api_instance.list_isos(list_isos_request_content)
        print("The response of VPSManagementApi->list_isos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->list_isos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_isos_request_content** | [**ListIsosRequestContent**](ListIsosRequestContent.md)|  | 

### Return type

[**ListIsosResponseContent**](ListIsosResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListIsos 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reinstall_os**
> ListReinstallOsResponseContent list_reinstall_os(list_reinstall_os_request_content)

Retrieves the list of available OS images for VPS reinstallation

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_reinstall_os_request_content import ListReinstallOsRequestContent
from ha_sdk_python.models.list_reinstall_os_response_content import ListReinstallOsResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    list_reinstall_os_request_content = ha_sdk_python.ListReinstallOsRequestContent() # ListReinstallOsRequestContent | 

    try:
        api_response = api_instance.list_reinstall_os(list_reinstall_os_request_content)
        print("The response of VPSManagementApi->list_reinstall_os:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->list_reinstall_os: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_reinstall_os_request_content** | [**ListReinstallOsRequestContent**](ListReinstallOsRequestContent.md)|  | 

### Return type

[**ListReinstallOsResponseContent**](ListReinstallOsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListReinstallOs 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vps_services**
> ListVpsServicesResponseContent list_vps_services()

Lists all VPS services accessible by the authenticated user

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_vps_services_response_content import ListVpsServicesResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)

    try:
        api_response = api_instance.list_vps_services()
        print("The response of VPSManagementApi->list_vps_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->list_vps_services: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListVpsServicesResponseContent**](ListVpsServicesResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListVpsServices 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_iso**
> MountIsoResponseContent mount_iso(mount_iso_request_content)

Mounts an ISO image on a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.mount_iso_request_content import MountIsoRequestContent
from ha_sdk_python.models.mount_iso_response_content import MountIsoResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    mount_iso_request_content = ha_sdk_python.MountIsoRequestContent() # MountIsoRequestContent | 

    try:
        api_response = api_instance.mount_iso(mount_iso_request_content)
        print("The response of VPSManagementApi->mount_iso:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->mount_iso: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_iso_request_content** | [**MountIsoRequestContent**](MountIsoRequestContent.md)|  | 

### Return type

[**MountIsoResponseContent**](MountIsoResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MountIso 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_reinstall**
> TriggerReinstallResponseContent trigger_reinstall(trigger_reinstall_request_content)

Triggers a VPS reinstallation with the specified OS template

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.trigger_reinstall_request_content import TriggerReinstallRequestContent
from ha_sdk_python.models.trigger_reinstall_response_content import TriggerReinstallResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    trigger_reinstall_request_content = ha_sdk_python.TriggerReinstallRequestContent() # TriggerReinstallRequestContent | 

    try:
        api_response = api_instance.trigger_reinstall(trigger_reinstall_request_content)
        print("The response of VPSManagementApi->trigger_reinstall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->trigger_reinstall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_reinstall_request_content** | [**TriggerReinstallRequestContent**](TriggerReinstallRequestContent.md)|  | 

### Return type

[**TriggerReinstallResponseContent**](TriggerReinstallResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TriggerReinstall 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vps_config**
> UpdateVpsConfigResponseContent update_vps_config(update_vps_config_request_content)

Updates VPS configuration settings such as name, hostname, auto-start, boot order, and CD-ROM

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_vps_config_request_content import UpdateVpsConfigRequestContent
from ha_sdk_python.models.update_vps_config_response_content import UpdateVpsConfigResponseContent
from ha_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ha_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = ha_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ha_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ha_sdk_python.VPSManagementApi(api_client)
    update_vps_config_request_content = ha_sdk_python.UpdateVpsConfigRequestContent() # UpdateVpsConfigRequestContent | 

    try:
        api_response = api_instance.update_vps_config(update_vps_config_request_content)
        print("The response of VPSManagementApi->update_vps_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSManagementApi->update_vps_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vps_config_request_content** | [**UpdateVpsConfigRequestContent**](UpdateVpsConfigRequestContent.md)|  | 

### Return type

[**UpdateVpsConfigResponseContent**](UpdateVpsConfigResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateVpsConfig 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

