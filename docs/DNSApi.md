# hostafrica_sdk_python.DNSApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rdns_record**](DNSApi.md#create_rdns_record) | **POST** /dns/create-rdns-record | 
[**delete_rdns_record**](DNSApi.md#delete_rdns_record) | **POST** /dns/delete-rdns-record | 
[**list_rdns_records**](DNSApi.md#list_rdns_records) | **POST** /dns/list-rdns-records | 


# **create_rdns_record**
> CreateRdnsRecordResponseContent create_rdns_record(create_rdns_record_request_content)

Creates (or upserts) a PTR record for the authenticated client. If the client already owns a PTR for the same (serverid, ip) it is updated in place; if another client owns it a 409 is returned.

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.create_rdns_record_request_content import CreateRdnsRecordRequestContent
from hostafrica_sdk_python.models.create_rdns_record_response_content import CreateRdnsRecordResponseContent
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
    api_instance = hostafrica_sdk_python.DNSApi(api_client)
    create_rdns_record_request_content = hostafrica_sdk_python.CreateRdnsRecordRequestContent() # CreateRdnsRecordRequestContent | 

    try:
        api_response = api_instance.create_rdns_record(create_rdns_record_request_content)
        print("The response of DNSApi->create_rdns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->create_rdns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rdns_record_request_content** | [**CreateRdnsRecordRequestContent**](CreateRdnsRecordRequestContent.md)|  | 

### Return type

[**CreateRdnsRecordResponseContent**](CreateRdnsRecordResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CreateRdnsRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**409** | InvalidStateError 409 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rdns_record**
> DeleteRdnsRecordResponseContent delete_rdns_record(delete_rdns_record_request_content)

Deletes a PTR (rDNS) record owned by the authenticated client

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.delete_rdns_record_request_content import DeleteRdnsRecordRequestContent
from hostafrica_sdk_python.models.delete_rdns_record_response_content import DeleteRdnsRecordResponseContent
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
    api_instance = hostafrica_sdk_python.DNSApi(api_client)
    delete_rdns_record_request_content = hostafrica_sdk_python.DeleteRdnsRecordRequestContent() # DeleteRdnsRecordRequestContent | 

    try:
        api_response = api_instance.delete_rdns_record(delete_rdns_record_request_content)
        print("The response of DNSApi->delete_rdns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->delete_rdns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_rdns_record_request_content** | [**DeleteRdnsRecordRequestContent**](DeleteRdnsRecordRequestContent.md)|  | 

### Return type

[**DeleteRdnsRecordResponseContent**](DeleteRdnsRecordResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteRdnsRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rdns_records**
> ListRdnsRecordsResponseContent list_rdns_records()

Lists all rDNS (PTR) records and available services for the authenticated client

### Example

* Bearer Authentication (smithy.api.httpBearerAuth):

```python
import hostafrica_sdk_python
from hostafrica_sdk_python.models.list_rdns_records_response_content import ListRdnsRecordsResponseContent
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
    api_instance = hostafrica_sdk_python.DNSApi(api_client)

    try:
        api_response = api_instance.list_rdns_records()
        print("The response of DNSApi->list_rdns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->list_rdns_records: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListRdnsRecordsResponseContent**](ListRdnsRecordsResponseContent.md)

### Authorization

[smithy.api.httpBearerAuth](../README.md#smithy.api.httpBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListRdnsRecords 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

