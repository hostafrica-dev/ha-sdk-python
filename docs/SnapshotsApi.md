# hostafrica_sdk_python.SnapshotsApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /vps/create-snapshot | 
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **POST** /vps/delete-snapshot | 
[**list_snapshots**](SnapshotsApi.md#list_snapshots) | **POST** /vps/list-snapshots | 
[**rollback_snapshot**](SnapshotsApi.md#rollback_snapshot) | **POST** /vps/rollback-snapshot | 
[**update_snapshot**](SnapshotsApi.md#update_snapshot) | **POST** /vps/update-snapshot | 


# **create_snapshot**
> CreateSnapshotResponseContent create_snapshot(create_snapshot_request_content)

Creates a new snapshot for a VPS service

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.create_snapshot_request_content import CreateSnapshotRequestContent
from hostafrica_sdk_python.models.create_snapshot_response_content import CreateSnapshotResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.SnapshotsApi(api_client)
    create_snapshot_request_content = hostafrica_sdk_python.CreateSnapshotRequestContent() # CreateSnapshotRequestContent | 

    try:
        api_response = api_instance.create_snapshot(create_snapshot_request_content)
        print("The response of SnapshotsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_snapshot_request_content** | [**CreateSnapshotRequestContent**](CreateSnapshotRequestContent.md)|  | 

### Return type

[**CreateSnapshotResponseContent**](CreateSnapshotResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateSnapshot 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot**
> DeleteSnapshotResponseContent delete_snapshot(delete_snapshot_request_content)

Deletes a specific snapshot from a VPS service

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.delete_snapshot_request_content import DeleteSnapshotRequestContent
from hostafrica_sdk_python.models.delete_snapshot_response_content import DeleteSnapshotResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.SnapshotsApi(api_client)
    delete_snapshot_request_content = hostafrica_sdk_python.DeleteSnapshotRequestContent() # DeleteSnapshotRequestContent | 

    try:
        api_response = api_instance.delete_snapshot(delete_snapshot_request_content)
        print("The response of SnapshotsApi->delete_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_snapshot_request_content** | [**DeleteSnapshotRequestContent**](DeleteSnapshotRequestContent.md)|  | 

### Return type

[**DeleteSnapshotResponseContent**](DeleteSnapshotResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteSnapshot 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots**
> ListSnapshotsResponseContent list_snapshots(list_snapshots_request_content)

Retrieves the list of snapshots for a VPS service

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.list_snapshots_request_content import ListSnapshotsRequestContent
from hostafrica_sdk_python.models.list_snapshots_response_content import ListSnapshotsResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.SnapshotsApi(api_client)
    list_snapshots_request_content = hostafrica_sdk_python.ListSnapshotsRequestContent() # ListSnapshotsRequestContent | 

    try:
        api_response = api_instance.list_snapshots(list_snapshots_request_content)
        print("The response of SnapshotsApi->list_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_snapshots_request_content** | [**ListSnapshotsRequestContent**](ListSnapshotsRequestContent.md)|  | 

### Return type

[**ListSnapshotsResponseContent**](ListSnapshotsResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListSnapshots 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_snapshot**
> RollbackSnapshotResponseContent rollback_snapshot(rollback_snapshot_request_content)

[Under development] Rolls back a VPS to a previous snapshot state

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.rollback_snapshot_request_content import RollbackSnapshotRequestContent
from hostafrica_sdk_python.models.rollback_snapshot_response_content import RollbackSnapshotResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.SnapshotsApi(api_client)
    rollback_snapshot_request_content = hostafrica_sdk_python.RollbackSnapshotRequestContent() # RollbackSnapshotRequestContent | 

    try:
        api_response = api_instance.rollback_snapshot(rollback_snapshot_request_content)
        print("The response of SnapshotsApi->rollback_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->rollback_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollback_snapshot_request_content** | [**RollbackSnapshotRequestContent**](RollbackSnapshotRequestContent.md)|  | 

### Return type

[**RollbackSnapshotResponseContent**](RollbackSnapshotResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RollbackSnapshot 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot**
> UpdateSnapshotResponseContent update_snapshot(update_snapshot_request_content)

Updates a snapshot's metadata

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.update_snapshot_request_content import UpdateSnapshotRequestContent
from hostafrica_sdk_python.models.update_snapshot_response_content import UpdateSnapshotResponseContent
from hostafrica_sdk_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hostafrica.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostafrica_sdk_python.Configuration(
    host = "https://api.hostafrica.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: smithy.api.httpBearerAuth
configuration = hostafrica_sdk_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostafrica_sdk_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostafrica_sdk_python.SnapshotsApi(api_client)
    update_snapshot_request_content = hostafrica_sdk_python.UpdateSnapshotRequestContent() # UpdateSnapshotRequestContent | 

    try:
        api_response = api_instance.update_snapshot(update_snapshot_request_content)
        print("The response of SnapshotsApi->update_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->update_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_snapshot_request_content** | [**UpdateSnapshotRequestContent**](UpdateSnapshotRequestContent.md)|  | 

### Return type

[**UpdateSnapshotResponseContent**](UpdateSnapshotResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateSnapshot 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

