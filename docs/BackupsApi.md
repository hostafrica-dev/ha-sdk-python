# ha_sdk_python.BackupsApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backup**](BackupsApi.md#create_backup) | **POST** /vps/create-backup | 
[**create_backup_schedule**](BackupsApi.md#create_backup_schedule) | **POST** /vps/create-backup-schedule | 
[**delete_backup**](BackupsApi.md#delete_backup) | **POST** /vps/delete-backup | 
[**delete_backup_schedule**](BackupsApi.md#delete_backup_schedule) | **POST** /vps/delete-backup-schedule | 
[**edit_backup_schedule**](BackupsApi.md#edit_backup_schedule) | **POST** /vps/edit-backup-schedule | 
[**list_backup_schedules**](BackupsApi.md#list_backup_schedules) | **POST** /vps/list-backup-schedules | 
[**list_backups**](BackupsApi.md#list_backups) | **POST** /vps/list-backups | 
[**restore_backup**](BackupsApi.md#restore_backup) | **POST** /vps/restore-backup | 


# **create_backup**
> CreateBackupResponseContent create_backup(create_backup_request_content)

Creates a new backup for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_backup_request_content import CreateBackupRequestContent
from ha_sdk_python.models.create_backup_response_content import CreateBackupResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    create_backup_request_content = ha_sdk_python.CreateBackupRequestContent() # CreateBackupRequestContent | 

    try:
        api_response = api_instance.create_backup(create_backup_request_content)
        print("The response of BackupsApi->create_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->create_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_backup_request_content** | [**CreateBackupRequestContent**](CreateBackupRequestContent.md)|  | 

### Return type

[**CreateBackupResponseContent**](CreateBackupResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateBackup 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_backup_schedule**
> CreateBackupScheduleResponseContent create_backup_schedule(create_backup_schedule_request_content)

Creates a new backup schedule for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_backup_schedule_request_content import CreateBackupScheduleRequestContent
from ha_sdk_python.models.create_backup_schedule_response_content import CreateBackupScheduleResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    create_backup_schedule_request_content = ha_sdk_python.CreateBackupScheduleRequestContent() # CreateBackupScheduleRequestContent | 

    try:
        api_response = api_instance.create_backup_schedule(create_backup_schedule_request_content)
        print("The response of BackupsApi->create_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->create_backup_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_backup_schedule_request_content** | [**CreateBackupScheduleRequestContent**](CreateBackupScheduleRequestContent.md)|  | 

### Return type

[**CreateBackupScheduleResponseContent**](CreateBackupScheduleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateBackupSchedule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup**
> DeleteBackupResponseContent delete_backup(delete_backup_request_content)

Deletes a specific backup from a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_backup_request_content import DeleteBackupRequestContent
from ha_sdk_python.models.delete_backup_response_content import DeleteBackupResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    delete_backup_request_content = ha_sdk_python.DeleteBackupRequestContent() # DeleteBackupRequestContent | 

    try:
        api_response = api_instance.delete_backup(delete_backup_request_content)
        print("The response of BackupsApi->delete_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->delete_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_backup_request_content** | [**DeleteBackupRequestContent**](DeleteBackupRequestContent.md)|  | 

### Return type

[**DeleteBackupResponseContent**](DeleteBackupResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteBackup 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup_schedule**
> DeleteBackupScheduleResponseContent delete_backup_schedule(delete_backup_schedule_request_content)

Deletes a backup schedule from a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_backup_schedule_request_content import DeleteBackupScheduleRequestContent
from ha_sdk_python.models.delete_backup_schedule_response_content import DeleteBackupScheduleResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    delete_backup_schedule_request_content = ha_sdk_python.DeleteBackupScheduleRequestContent() # DeleteBackupScheduleRequestContent | 

    try:
        api_response = api_instance.delete_backup_schedule(delete_backup_schedule_request_content)
        print("The response of BackupsApi->delete_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->delete_backup_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_backup_schedule_request_content** | [**DeleteBackupScheduleRequestContent**](DeleteBackupScheduleRequestContent.md)|  | 

### Return type

[**DeleteBackupScheduleResponseContent**](DeleteBackupScheduleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteBackupSchedule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_backup_schedule**
> EditBackupScheduleResponseContent edit_backup_schedule(edit_backup_schedule_request_content)

Edits an existing backup schedule for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.edit_backup_schedule_request_content import EditBackupScheduleRequestContent
from ha_sdk_python.models.edit_backup_schedule_response_content import EditBackupScheduleResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    edit_backup_schedule_request_content = ha_sdk_python.EditBackupScheduleRequestContent() # EditBackupScheduleRequestContent | 

    try:
        api_response = api_instance.edit_backup_schedule(edit_backup_schedule_request_content)
        print("The response of BackupsApi->edit_backup_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->edit_backup_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_backup_schedule_request_content** | [**EditBackupScheduleRequestContent**](EditBackupScheduleRequestContent.md)|  | 

### Return type

[**EditBackupScheduleResponseContent**](EditBackupScheduleResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EditBackupSchedule 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backup_schedules**
> ListBackupSchedulesResponseContent list_backup_schedules(list_backup_schedules_request_content)

Retrieves the list of backup schedules for a VPS service

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_backup_schedules_request_content import ListBackupSchedulesRequestContent
from ha_sdk_python.models.list_backup_schedules_response_content import ListBackupSchedulesResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    list_backup_schedules_request_content = ha_sdk_python.ListBackupSchedulesRequestContent() # ListBackupSchedulesRequestContent | 

    try:
        api_response = api_instance.list_backup_schedules(list_backup_schedules_request_content)
        print("The response of BackupsApi->list_backup_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->list_backup_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_backup_schedules_request_content** | [**ListBackupSchedulesRequestContent**](ListBackupSchedulesRequestContent.md)|  | 

### Return type

[**ListBackupSchedulesResponseContent**](ListBackupSchedulesResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListBackupSchedules 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_backups**
> ListBackupsResponseContent list_backups(list_backups_request_content)

Retrieves the list of backups for a VPS service including quota information and backup configuration options

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_backups_request_content import ListBackupsRequestContent
from ha_sdk_python.models.list_backups_response_content import ListBackupsResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    list_backups_request_content = ha_sdk_python.ListBackupsRequestContent() # ListBackupsRequestContent | 

    try:
        api_response = api_instance.list_backups(list_backups_request_content)
        print("The response of BackupsApi->list_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->list_backups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_backups_request_content** | [**ListBackupsRequestContent**](ListBackupsRequestContent.md)|  | 

### Return type

[**ListBackupsResponseContent**](ListBackupsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListBackups 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_backup**
> RestoreBackupResponseContent restore_backup(restore_backup_request_content)

Restores a VPS from a backup with the specified backup identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.restore_backup_request_content import RestoreBackupRequestContent
from ha_sdk_python.models.restore_backup_response_content import RestoreBackupResponseContent
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
    api_instance = ha_sdk_python.BackupsApi(api_client)
    restore_backup_request_content = ha_sdk_python.RestoreBackupRequestContent() # RestoreBackupRequestContent | 

    try:
        api_response = api_instance.restore_backup(restore_backup_request_content)
        print("The response of BackupsApi->restore_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->restore_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_backup_request_content** | [**RestoreBackupRequestContent**](RestoreBackupRequestContent.md)|  | 

### Return type

[**RestoreBackupResponseContent**](RestoreBackupResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RestoreBackup 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

