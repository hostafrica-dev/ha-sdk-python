# ha_sdk_python.PowerManagementApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_power_task**](PowerManagementApi.md#create_power_task) | **POST** /vps/create-power-task | 
[**delete_power_task**](PowerManagementApi.md#delete_power_task) | **POST** /vps/delete-power-task | 
[**list_power_tasks**](PowerManagementApi.md#list_power_tasks) | **POST** /vps/list-power-tasks | 
[**reboot_vps**](PowerManagementApi.md#reboot_vps) | **POST** /vps/reboot | 
[**shutdown_vps**](PowerManagementApi.md#shutdown_vps) | **POST** /vps/shutdown | 
[**start_vps**](PowerManagementApi.md#start_vps) | **POST** /vps/start | 
[**stop_vps**](PowerManagementApi.md#stop_vps) | **POST** /vps/stop | 
[**update_power_task**](PowerManagementApi.md#update_power_task) | **POST** /vps/update-power-task | 


# **create_power_task**
> CreatePowerTaskResponseContent create_power_task(create_power_task_request_content)

Creates a new power task (scheduled start/stop/restart operation) for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_power_task_request_content import CreatePowerTaskRequestContent
from ha_sdk_python.models.create_power_task_response_content import CreatePowerTaskResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    create_power_task_request_content = ha_sdk_python.CreatePowerTaskRequestContent() # CreatePowerTaskRequestContent | 

    try:
        api_response = api_instance.create_power_task(create_power_task_request_content)
        print("The response of PowerManagementApi->create_power_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->create_power_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_power_task_request_content** | [**CreatePowerTaskRequestContent**](CreatePowerTaskRequestContent.md)|  | 

### Return type

[**CreatePowerTaskResponseContent**](CreatePowerTaskResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreatePowerTask 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_power_task**
> DeletePowerTaskResponseContent delete_power_task(delete_power_task_request_content)

Deletes a power task from a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_power_task_request_content import DeletePowerTaskRequestContent
from ha_sdk_python.models.delete_power_task_response_content import DeletePowerTaskResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    delete_power_task_request_content = ha_sdk_python.DeletePowerTaskRequestContent() # DeletePowerTaskRequestContent | 

    try:
        api_response = api_instance.delete_power_task(delete_power_task_request_content)
        print("The response of PowerManagementApi->delete_power_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->delete_power_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_power_task_request_content** | [**DeletePowerTaskRequestContent**](DeletePowerTaskRequestContent.md)|  | 

### Return type

[**DeletePowerTaskResponseContent**](DeletePowerTaskResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeletePowerTask 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_power_tasks**
> ListPowerTasksResponseContent list_power_tasks(list_power_tasks_request_content)

Retrieves the list of power tasks (scheduled start/stop/restart operations) for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_power_tasks_request_content import ListPowerTasksRequestContent
from ha_sdk_python.models.list_power_tasks_response_content import ListPowerTasksResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    list_power_tasks_request_content = ha_sdk_python.ListPowerTasksRequestContent() # ListPowerTasksRequestContent | 

    try:
        api_response = api_instance.list_power_tasks(list_power_tasks_request_content)
        print("The response of PowerManagementApi->list_power_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->list_power_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_power_tasks_request_content** | [**ListPowerTasksRequestContent**](ListPowerTasksRequestContent.md)|  | 

### Return type

[**ListPowerTasksResponseContent**](ListPowerTasksResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListPowerTasks 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_vps**
> RebootVpsResponseContent reboot_vps(reboot_vps_request_content)

Gracefully reboot a VPS service. Sends ACPI reboot signal to guest OS

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.reboot_vps_request_content import RebootVpsRequestContent
from ha_sdk_python.models.reboot_vps_response_content import RebootVpsResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    reboot_vps_request_content = ha_sdk_python.RebootVpsRequestContent() # RebootVpsRequestContent | 

    try:
        api_response = api_instance.reboot_vps(reboot_vps_request_content)
        print("The response of PowerManagementApi->reboot_vps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->reboot_vps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_vps_request_content** | [**RebootVpsRequestContent**](RebootVpsRequestContent.md)|  | 

### Return type

[**RebootVpsResponseContent**](RebootVpsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RebootVps 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_vps**
> ShutdownVpsResponseContent shutdown_vps(shutdown_vps_request_content)

Gracefully shutdown a VPS service. Sends ACPI shutdown signal to guest OS

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.shutdown_vps_request_content import ShutdownVpsRequestContent
from ha_sdk_python.models.shutdown_vps_response_content import ShutdownVpsResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    shutdown_vps_request_content = ha_sdk_python.ShutdownVpsRequestContent() # ShutdownVpsRequestContent | 

    try:
        api_response = api_instance.shutdown_vps(shutdown_vps_request_content)
        print("The response of PowerManagementApi->shutdown_vps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->shutdown_vps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shutdown_vps_request_content** | [**ShutdownVpsRequestContent**](ShutdownVpsRequestContent.md)|  | 

### Return type

[**ShutdownVpsResponseContent**](ShutdownVpsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ShutdownVps 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_vps**
> StartVpsResponseContent start_vps(start_vps_request_content)

Starts a stopped VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.start_vps_request_content import StartVpsRequestContent
from ha_sdk_python.models.start_vps_response_content import StartVpsResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    start_vps_request_content = ha_sdk_python.StartVpsRequestContent() # StartVpsRequestContent | 

    try:
        api_response = api_instance.start_vps(start_vps_request_content)
        print("The response of PowerManagementApi->start_vps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->start_vps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_vps_request_content** | [**StartVpsRequestContent**](StartVpsRequestContent.md)|  | 

### Return type

[**StartVpsResponseContent**](StartVpsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | StartVps 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_vps**
> StopVpsResponseContent stop_vps(stop_vps_request_content)

Hard stops a running VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.stop_vps_request_content import StopVpsRequestContent
from ha_sdk_python.models.stop_vps_response_content import StopVpsResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    stop_vps_request_content = ha_sdk_python.StopVpsRequestContent() # StopVpsRequestContent | 

    try:
        api_response = api_instance.stop_vps(stop_vps_request_content)
        print("The response of PowerManagementApi->stop_vps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->stop_vps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_vps_request_content** | [**StopVpsRequestContent**](StopVpsRequestContent.md)|  | 

### Return type

[**StopVpsResponseContent**](StopVpsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | StopVps 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_task**
> UpdatePowerTaskResponseContent update_power_task(update_power_task_request_content)

Updates an existing power task (scheduled start/stop/restart operation) for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_power_task_request_content import UpdatePowerTaskRequestContent
from ha_sdk_python.models.update_power_task_response_content import UpdatePowerTaskResponseContent
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
    api_instance = ha_sdk_python.PowerManagementApi(api_client)
    update_power_task_request_content = ha_sdk_python.UpdatePowerTaskRequestContent() # UpdatePowerTaskRequestContent | 

    try:
        api_response = api_instance.update_power_task(update_power_task_request_content)
        print("The response of PowerManagementApi->update_power_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PowerManagementApi->update_power_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_power_task_request_content** | [**UpdatePowerTaskRequestContent**](UpdatePowerTaskRequestContent.md)|  | 

### Return type

[**UpdatePowerTaskResponseContent**](UpdatePowerTaskResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdatePowerTask 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

