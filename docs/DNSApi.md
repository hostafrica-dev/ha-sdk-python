# ha_sdk_python.DNSApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dns_record**](DNSApi.md#add_dns_record) | **POST** /dns/add-record | 
[**create_rdns_record**](DNSApi.md#create_rdns_record) | **POST** /dns/create-rdns-record | 
[**delete_dns_record**](DNSApi.md#delete_dns_record) | **POST** /dns/delete-record | 
[**delete_rdns_record**](DNSApi.md#delete_rdns_record) | **POST** /dns/delete-rdns-record | 
[**edit_dns_record**](DNSApi.md#edit_dns_record) | **POST** /dns/edit-record | 
[**get_dns_zone_details**](DNSApi.md#get_dns_zone_details) | **POST** /dns/get-zone | 
[**list_dns_create_candidates**](DNSApi.md#list_dns_create_candidates) | **POST** /dns/list-create-candidates | 
[**list_dns_zones**](DNSApi.md#list_dns_zones) | **POST** /dns/list-zones | 
[**list_rdns_records**](DNSApi.md#list_rdns_records) | **POST** /dns/list-rdns-records | 


# **add_dns_record**
> AddDnsRecordResponseContent add_dns_record(add_dns_record_request_content)

Adds a DNS record to a zone via DNSManager.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.add_dns_record_request_content import AddDnsRecordRequestContent
from ha_sdk_python.models.add_dns_record_response_content import AddDnsRecordResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    add_dns_record_request_content = ha_sdk_python.AddDnsRecordRequestContent() # AddDnsRecordRequestContent | 

    try:
        api_response = api_instance.add_dns_record(add_dns_record_request_content)
        print("The response of DNSApi->add_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->add_dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_dns_record_request_content** | [**AddDnsRecordRequestContent**](AddDnsRecordRequestContent.md)|  | 

### Return type

[**AddDnsRecordResponseContent**](AddDnsRecordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddDnsRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rdns_record**
> CreateRdnsRecordResponseContent create_rdns_record(create_rdns_record_request_content)

Creates (or upserts) a PTR record for the authenticated client. If the client already owns a PTR for the same (serverid, ip) it is updated in place; if another client owns it a 409 is returned.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.create_rdns_record_request_content import CreateRdnsRecordRequestContent
from ha_sdk_python.models.create_rdns_record_response_content import CreateRdnsRecordResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    create_rdns_record_request_content = ha_sdk_python.CreateRdnsRecordRequestContent() # CreateRdnsRecordRequestContent | 

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

[BearerAuth](../README.md#BearerAuth)

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
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_record**
> DeleteDnsRecordResponseContent delete_dns_record(delete_dns_record_request_content)

Deletes a DNS record from a zone via DNSManager.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_dns_record_request_content import DeleteDnsRecordRequestContent
from ha_sdk_python.models.delete_dns_record_response_content import DeleteDnsRecordResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    delete_dns_record_request_content = ha_sdk_python.DeleteDnsRecordRequestContent() # DeleteDnsRecordRequestContent | 

    try:
        api_response = api_instance.delete_dns_record(delete_dns_record_request_content)
        print("The response of DNSApi->delete_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->delete_dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_dns_record_request_content** | [**DeleteDnsRecordRequestContent**](DeleteDnsRecordRequestContent.md)|  | 

### Return type

[**DeleteDnsRecordResponseContent**](DeleteDnsRecordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteDnsRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rdns_record**
> DeleteRdnsRecordResponseContent delete_rdns_record(delete_rdns_record_request_content)

Deletes a PTR (rDNS) record owned by the authenticated client

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_rdns_record_request_content import DeleteRdnsRecordRequestContent
from ha_sdk_python.models.delete_rdns_record_response_content import DeleteRdnsRecordResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    delete_rdns_record_request_content = ha_sdk_python.DeleteRdnsRecordRequestContent() # DeleteRdnsRecordRequestContent | 

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

[BearerAuth](../README.md#BearerAuth)

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

# **edit_dns_record**
> EditDnsRecordResponseContent edit_dns_record(edit_dns_record_request_content)

Edits a DNS record in a zone via DNSManager.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.edit_dns_record_request_content import EditDnsRecordRequestContent
from ha_sdk_python.models.edit_dns_record_response_content import EditDnsRecordResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    edit_dns_record_request_content = ha_sdk_python.EditDnsRecordRequestContent() # EditDnsRecordRequestContent | 

    try:
        api_response = api_instance.edit_dns_record(edit_dns_record_request_content)
        print("The response of DNSApi->edit_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->edit_dns_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_dns_record_request_content** | [**EditDnsRecordRequestContent**](EditDnsRecordRequestContent.md)|  | 

### Return type

[**EditDnsRecordResponseContent**](EditDnsRecordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EditDnsRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_zone_details**
> GetDnsZoneDetailsResponseContent get_dns_zone_details(get_dns_zone_details_request_content)

Retrieves DNS zone details and records for an owned domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_dns_zone_details_request_content import GetDnsZoneDetailsRequestContent
from ha_sdk_python.models.get_dns_zone_details_response_content import GetDnsZoneDetailsResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)
    get_dns_zone_details_request_content = ha_sdk_python.GetDnsZoneDetailsRequestContent() # GetDnsZoneDetailsRequestContent | 

    try:
        api_response = api_instance.get_dns_zone_details(get_dns_zone_details_request_content)
        print("The response of DNSApi->get_dns_zone_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_dns_zone_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_dns_zone_details_request_content** | [**GetDnsZoneDetailsRequestContent**](GetDnsZoneDetailsRequestContent.md)|  | 

### Return type

[**GetDnsZoneDetailsResponseContent**](GetDnsZoneDetailsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetDnsZoneDetails 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_create_candidates**
> ListDnsCreateCandidatesResponseContent list_dns_create_candidates()

Lists domains and services eligible for new DNS zone creation.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_dns_create_candidates_response_content import ListDnsCreateCandidatesResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)

    try:
        api_response = api_instance.list_dns_create_candidates()
        print("The response of DNSApi->list_dns_create_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->list_dns_create_candidates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDnsCreateCandidatesResponseContent**](ListDnsCreateCandidatesResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDnsCreateCandidates 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_zones**
> ListDnsZonesResponseContent list_dns_zones()

Lists DNS zones belonging to the authenticated client.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_dns_zones_response_content import ListDnsZonesResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)

    try:
        api_response = api_instance.list_dns_zones()
        print("The response of DNSApi->list_dns_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->list_dns_zones: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDnsZonesResponseContent**](ListDnsZonesResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDnsZones 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rdns_records**
> ListRdnsRecordsResponseContent list_rdns_records()

Lists all rDNS (PTR) records and available services for the authenticated client

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_rdns_records_response_content import ListRdnsRecordsResponseContent
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
    api_instance = ha_sdk_python.DNSApi(api_client)

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

[BearerAuth](../README.md#BearerAuth)

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
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

