# ha_sdk_python.DomainsApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dnssec_record**](DomainsApi.md#add_dnssec_record) | **POST** /domain/add-dnssec-record | 
[**add_domain_redirect**](DomainsApi.md#add_domain_redirect) | **POST** /domain/add-redirect | 
[**check_domain_availability**](DomainsApi.md#check_domain_availability) | **POST** /domain/check-availability | 
[**delete_dnssec_record**](DomainsApi.md#delete_dnssec_record) | **POST** /domain/delete-dnssec-record | 
[**delete_domain_redirect**](DomainsApi.md#delete_domain_redirect) | **POST** /domain/delete-redirect | 
[**delete_private_nameserver**](DomainsApi.md#delete_private_nameserver) | **POST** /domain/delete-private-nameserver | 
[**get_domain**](DomainsApi.md#get_domain) | **POST** /domain/get-domain | 
[**get_domain_contacts**](DomainsApi.md#get_domain_contacts) | **POST** /domain/get-domain-contacts | 
[**get_domain_redirect_details**](DomainsApi.md#get_domain_redirect_details) | **POST** /domain/get-redirect-details | 
[**list_dnssec_records**](DomainsApi.md#list_dnssec_records) | **POST** /domain/list-dnssec-records | 
[**list_domain_redirects**](DomainsApi.md#list_domain_redirects) | **POST** /domain/list-redirects | 
[**list_domains**](DomainsApi.md#list_domains) | **POST** /domain/list-domains | 
[**list_domains_requiring_data**](DomainsApi.md#list_domains_requiring_data) | **POST** /domain/list-domains-requiring-data | 
[**modify_private_nameserver**](DomainsApi.md#modify_private_nameserver) | **POST** /domain/modify-private-nameserver | 
[**register_private_nameserver**](DomainsApi.md#register_private_nameserver) | **POST** /domain/register-private-nameserver | 
[**save_domain_required_data**](DomainsApi.md#save_domain_required_data) | **POST** /domain/save-domain-required-data | 
[**suggest_domains**](DomainsApi.md#suggest_domains) | **POST** /domain/suggest | 
[**update_domain_contacts**](DomainsApi.md#update_domain_contacts) | **POST** /domain/update-domain-contacts | 
[**update_domain_lock_status**](DomainsApi.md#update_domain_lock_status) | **POST** /domain/update-lock-status | 
[**update_domain_nameservers**](DomainsApi.md#update_domain_nameservers) | **POST** /domain/update-nameservers | 
[**update_domain_settings**](DomainsApi.md#update_domain_settings) | **POST** /domain/update-domain-settings | 


# **add_dnssec_record**
> AddDnssecRecordResponseContent add_dnssec_record(add_dnssec_record_request_content)

Adds a DNSSEC DS record for an owned domain on supported registrars.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.add_dnssec_record_request_content import AddDnssecRecordRequestContent
from ha_sdk_python.models.add_dnssec_record_response_content import AddDnssecRecordResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    add_dnssec_record_request_content = ha_sdk_python.AddDnssecRecordRequestContent() # AddDnssecRecordRequestContent | 

    try:
        api_response = api_instance.add_dnssec_record(add_dnssec_record_request_content)
        print("The response of DomainsApi->add_dnssec_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->add_dnssec_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_dnssec_record_request_content** | [**AddDnssecRecordRequestContent**](AddDnssecRecordRequestContent.md)|  | 

### Return type

[**AddDnssecRecordResponseContent**](AddDnssecRecordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddDnssecRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_redirect**
> AddDomainRedirectResponseContent add_domain_redirect(add_domain_redirect_request_content)

Creates or updates HTTP redirect configuration for an owned domain. Upstream may create a DNS zone and point @/www A records at the redirector. If conflicting A records exist, retry with override=true after confirming via get-redirect-details.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.add_domain_redirect_request_content import AddDomainRedirectRequestContent
from ha_sdk_python.models.add_domain_redirect_response_content import AddDomainRedirectResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    add_domain_redirect_request_content = ha_sdk_python.AddDomainRedirectRequestContent() # AddDomainRedirectRequestContent | 

    try:
        api_response = api_instance.add_domain_redirect(add_domain_redirect_request_content)
        print("The response of DomainsApi->add_domain_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->add_domain_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_redirect_request_content** | [**AddDomainRedirectRequestContent**](AddDomainRedirectRequestContent.md)|  | 

### Return type

[**AddDomainRedirectResponseContent**](AddDomainRedirectResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddDomainRedirect 200 response |  -  |
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

# **check_domain_availability**
> CheckDomainAvailabilityResponseContent check_domain_availability(check_domain_availability_request_content=check_domain_availability_request_content)

Use to check availability/pricing for known domain names. Pass exactly one of domain or domains (comma-separated, max 20); API rejects both omitted or both set. Optional currency (default ZAR). Returns availability, prices, and an external register_url. Prefer suggest_domains for name ideas.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.check_domain_availability_request_content import CheckDomainAvailabilityRequestContent
from ha_sdk_python.models.check_domain_availability_response_content import CheckDomainAvailabilityResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    check_domain_availability_request_content = ha_sdk_python.CheckDomainAvailabilityRequestContent() # CheckDomainAvailabilityRequestContent |  (optional)

    try:
        api_response = api_instance.check_domain_availability(check_domain_availability_request_content=check_domain_availability_request_content)
        print("The response of DomainsApi->check_domain_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->check_domain_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_domain_availability_request_content** | [**CheckDomainAvailabilityRequestContent**](CheckDomainAvailabilityRequestContent.md)|  | [optional] 

### Return type

[**CheckDomainAvailabilityResponseContent**](CheckDomainAvailabilityResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CheckDomainAvailability 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dnssec_record**
> DeleteDnssecRecordResponseContent delete_dnssec_record(delete_dnssec_record_request_content)

Removes a DNSSEC DS record from an owned domain on supported registrars.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_dnssec_record_request_content import DeleteDnssecRecordRequestContent
from ha_sdk_python.models.delete_dnssec_record_response_content import DeleteDnssecRecordResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    delete_dnssec_record_request_content = ha_sdk_python.DeleteDnssecRecordRequestContent() # DeleteDnssecRecordRequestContent | 

    try:
        api_response = api_instance.delete_dnssec_record(delete_dnssec_record_request_content)
        print("The response of DomainsApi->delete_dnssec_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_dnssec_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_dnssec_record_request_content** | [**DeleteDnssecRecordRequestContent**](DeleteDnssecRecordRequestContent.md)|  | 

### Return type

[**DeleteDnssecRecordResponseContent**](DeleteDnssecRecordResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteDnssecRecord 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_redirect**
> DeleteDomainRedirectResponseContent delete_domain_redirect(delete_domain_redirect_request_content)

Removes redirect configuration for an owned domain from the redirector service. DNS records and zones are not modified.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_domain_redirect_request_content import DeleteDomainRedirectRequestContent
from ha_sdk_python.models.delete_domain_redirect_response_content import DeleteDomainRedirectResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    delete_domain_redirect_request_content = ha_sdk_python.DeleteDomainRedirectRequestContent() # DeleteDomainRedirectRequestContent | 

    try:
        api_response = api_instance.delete_domain_redirect(delete_domain_redirect_request_content)
        print("The response of DomainsApi->delete_domain_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_domain_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_domain_redirect_request_content** | [**DeleteDomainRedirectRequestContent**](DeleteDomainRedirectRequestContent.md)|  | 

### Return type

[**DeleteDomainRedirectResponseContent**](DeleteDomainRedirectResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeleteDomainRedirect 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_private_nameserver**
> DeletePrivateNameserverResponseContent delete_private_nameserver(delete_private_nameserver_request_content)

Deletes a private/child nameserver glue host for an owned domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.delete_private_nameserver_request_content import DeletePrivateNameserverRequestContent
from ha_sdk_python.models.delete_private_nameserver_response_content import DeletePrivateNameserverResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    delete_private_nameserver_request_content = ha_sdk_python.DeletePrivateNameserverRequestContent() # DeletePrivateNameserverRequestContent | 

    try:
        api_response = api_instance.delete_private_nameserver(delete_private_nameserver_request_content)
        print("The response of DomainsApi->delete_private_nameserver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_private_nameserver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_private_nameserver_request_content** | [**DeletePrivateNameserverRequestContent**](DeletePrivateNameserverRequestContent.md)|  | 

### Return type

[**DeletePrivateNameserverResponseContent**](DeletePrivateNameserverResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeletePrivateNameserver 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> GetDomainResponseContent get_domain(get_domain_request_content)

Gets details for an owned domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_domain_request_content import GetDomainRequestContent
from ha_sdk_python.models.get_domain_response_content import GetDomainResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    get_domain_request_content = ha_sdk_python.GetDomainRequestContent() # GetDomainRequestContent | 

    try:
        api_response = api_instance.get_domain(get_domain_request_content)
        print("The response of DomainsApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_domain_request_content** | [**GetDomainRequestContent**](GetDomainRequestContent.md)|  | 

### Return type

[**GetDomainResponseContent**](GetDomainResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetDomain 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_contacts**
> GetDomainContactsResponseContent get_domain_contacts(get_domain_contacts_request_content)

Retrieves WHOIS contact information for an owned domain. Contact field names vary by TLD and registrar; use the returned structure when building custom contact update payloads.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_domain_contacts_request_content import GetDomainContactsRequestContent
from ha_sdk_python.models.get_domain_contacts_response_content import GetDomainContactsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    get_domain_contacts_request_content = ha_sdk_python.GetDomainContactsRequestContent() # GetDomainContactsRequestContent | 

    try:
        api_response = api_instance.get_domain_contacts(get_domain_contacts_request_content)
        print("The response of DomainsApi->get_domain_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_domain_contacts_request_content** | [**GetDomainContactsRequestContent**](GetDomainContactsRequestContent.md)|  | 

### Return type

[**GetDomainContactsResponseContent**](GetDomainContactsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetDomainContacts 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_redirect_details**
> GetDomainRedirectDetailsResponseContent get_domain_redirect_details(get_domain_redirect_details_request_content)

Retrieves redirect configuration and DNS readiness flags for an owned domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.get_domain_redirect_details_request_content import GetDomainRedirectDetailsRequestContent
from ha_sdk_python.models.get_domain_redirect_details_response_content import GetDomainRedirectDetailsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    get_domain_redirect_details_request_content = ha_sdk_python.GetDomainRedirectDetailsRequestContent() # GetDomainRedirectDetailsRequestContent | 

    try:
        api_response = api_instance.get_domain_redirect_details(get_domain_redirect_details_request_content)
        print("The response of DomainsApi->get_domain_redirect_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_redirect_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_domain_redirect_details_request_content** | [**GetDomainRedirectDetailsRequestContent**](GetDomainRedirectDetailsRequestContent.md)|  | 

### Return type

[**GetDomainRedirectDetailsResponseContent**](GetDomainRedirectDetailsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetDomainRedirectDetails 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dnssec_records**
> ListDnssecRecordsResponseContent list_dnssec_records(list_dnssec_records_request_content)

Lists DNSSEC DS records configured for an owned domain.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_dnssec_records_request_content import ListDnssecRecordsRequestContent
from ha_sdk_python.models.list_dnssec_records_response_content import ListDnssecRecordsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    list_dnssec_records_request_content = ha_sdk_python.ListDnssecRecordsRequestContent() # ListDnssecRecordsRequestContent | 

    try:
        api_response = api_instance.list_dnssec_records(list_dnssec_records_request_content)
        print("The response of DomainsApi->list_dnssec_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_dnssec_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_dnssec_records_request_content** | [**ListDnssecRecordsRequestContent**](ListDnssecRecordsRequestContent.md)|  | 

### Return type

[**ListDnssecRecordsResponseContent**](ListDnssecRecordsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDnssecRecords 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domain_redirects**
> ListDomainRedirectsResponseContent list_domain_redirects()

Lists configured domain redirects for the authenticated client.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_domain_redirects_response_content import ListDomainRedirectsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)

    try:
        api_response = api_instance.list_domain_redirects()
        print("The response of DomainsApi->list_domain_redirects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domain_redirects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDomainRedirectsResponseContent**](ListDomainRedirectsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDomainRedirects 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> ListDomainsResponseContent list_domains()

List all domains belonging to the authenticated client.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_domains_response_content import ListDomainsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)

    try:
        api_response = api_instance.list_domains()
        print("The response of DomainsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDomainsResponseContent**](ListDomainsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDomains 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains_requiring_data**
> ListDomainsRequiringDataResponseContent list_domains_requiring_data()

Lists domains belonging to the authenticated client that require additional registrar or contact data.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.list_domains_requiring_data_response_content import ListDomainsRequiringDataResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)

    try:
        api_response = api_instance.list_domains_requiring_data()
        print("The response of DomainsApi->list_domains_requiring_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains_requiring_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDomainsRequiringDataResponseContent**](ListDomainsRequiringDataResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ListDomainsRequiringData 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_private_nameserver**
> ModifyPrivateNameserverResponseContent modify_private_nameserver(modify_private_nameserver_request_content)

Modifies a private/child nameserver. Provide at least one of new_nameserver or new_ip_address. Some registrars (COZA/COCCA) require new_ip_address and reject hostname changes.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.modify_private_nameserver_request_content import ModifyPrivateNameserverRequestContent
from ha_sdk_python.models.modify_private_nameserver_response_content import ModifyPrivateNameserverResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    modify_private_nameserver_request_content = ha_sdk_python.ModifyPrivateNameserverRequestContent() # ModifyPrivateNameserverRequestContent | 

    try:
        api_response = api_instance.modify_private_nameserver(modify_private_nameserver_request_content)
        print("The response of DomainsApi->modify_private_nameserver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->modify_private_nameserver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_private_nameserver_request_content** | [**ModifyPrivateNameserverRequestContent**](ModifyPrivateNameserverRequestContent.md)|  | 

### Return type

[**ModifyPrivateNameserverResponseContent**](ModifyPrivateNameserverResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ModifyPrivateNameserver 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_private_nameserver**
> RegisterPrivateNameserverResponseContent register_private_nameserver(register_private_nameserver_request_content)

Registers a private/child nameserver (glue host) under an owned domain. Requires available_features.private_nameservers on get-domain. Distinct from update-nameservers.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.register_private_nameserver_request_content import RegisterPrivateNameserverRequestContent
from ha_sdk_python.models.register_private_nameserver_response_content import RegisterPrivateNameserverResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    register_private_nameserver_request_content = ha_sdk_python.RegisterPrivateNameserverRequestContent() # RegisterPrivateNameserverRequestContent | 

    try:
        api_response = api_instance.register_private_nameserver(register_private_nameserver_request_content)
        print("The response of DomainsApi->register_private_nameserver:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->register_private_nameserver: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_private_nameserver_request_content** | [**RegisterPrivateNameserverRequestContent**](RegisterPrivateNameserverRequestContent.md)|  | 

### Return type

[**RegisterPrivateNameserverResponseContent**](RegisterPrivateNameserverResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RegisterPrivateNameserver 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_domain_required_data**
> SaveDomainRequiredDataResponseContent save_domain_required_data(save_domain_required_data_request_content)

Saves additional registrar field values for a pending domain. Keys must match additionalFields[].name from list-domains-requiring-data.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.save_domain_required_data_request_content import SaveDomainRequiredDataRequestContent
from ha_sdk_python.models.save_domain_required_data_response_content import SaveDomainRequiredDataResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    save_domain_required_data_request_content = ha_sdk_python.SaveDomainRequiredDataRequestContent() # SaveDomainRequiredDataRequestContent | 

    try:
        api_response = api_instance.save_domain_required_data(save_domain_required_data_request_content)
        print("The response of DomainsApi->save_domain_required_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->save_domain_required_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_domain_required_data_request_content** | [**SaveDomainRequiredDataRequestContent**](SaveDomainRequiredDataRequestContent.md)|  | 

### Return type

[**SaveDomainRequiredDataResponseContent**](SaveDomainRequiredDataResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SaveDomainRequiredData 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest_domains**
> SuggestDomainsResponseContent suggest_domains(suggest_domains_request_content)

Use for domain name ideas from a description. For specific domains, use check_domain_availability.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.suggest_domains_request_content import SuggestDomainsRequestContent
from ha_sdk_python.models.suggest_domains_response_content import SuggestDomainsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    suggest_domains_request_content = ha_sdk_python.SuggestDomainsRequestContent() # SuggestDomainsRequestContent | 

    try:
        api_response = api_instance.suggest_domains(suggest_domains_request_content)
        print("The response of DomainsApi->suggest_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->suggest_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suggest_domains_request_content** | [**SuggestDomainsRequestContent**](SuggestDomainsRequestContent.md)|  | 

### Return type

[**SuggestDomainsResponseContent**](SuggestDomainsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuggestDomains 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_contacts**
> UpdateDomainContactsResponseContent update_domain_contacts(update_domain_contacts_request_content)

Updates WHOIS contact information for an owned domain. Each role (Registrant, Admin, Tech, Billing) uses a source type: owner (client profile), contact (saved WHMCS contact id), or custom (inline WHOIS fields). WHOIS values must be nested under fields; for owner and contact they are flattened upstream when present.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_domain_contacts_request_content import UpdateDomainContactsRequestContent
from ha_sdk_python.models.update_domain_contacts_response_content import UpdateDomainContactsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    update_domain_contacts_request_content = ha_sdk_python.UpdateDomainContactsRequestContent() # UpdateDomainContactsRequestContent | 

    try:
        api_response = api_instance.update_domain_contacts(update_domain_contacts_request_content)
        print("The response of DomainsApi->update_domain_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_domain_contacts_request_content** | [**UpdateDomainContactsRequestContent**](UpdateDomainContactsRequestContent.md)|  | 

### Return type

[**UpdateDomainContactsResponseContent**](UpdateDomainContactsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateDomainContacts 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_lock_status**
> UpdateDomainLockStatusResponseContent update_domain_lock_status(update_domain_lock_status_request_content)

Sets the registrar transfer lock for an owned domain. When the account has 2FA enabled, upstream may return 403 until two_fa_code (or two_fa_backup) is supplied.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_domain_lock_status_request_content import UpdateDomainLockStatusRequestContent
from ha_sdk_python.models.update_domain_lock_status_response_content import UpdateDomainLockStatusResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    update_domain_lock_status_request_content = ha_sdk_python.UpdateDomainLockStatusRequestContent() # UpdateDomainLockStatusRequestContent | 

    try:
        api_response = api_instance.update_domain_lock_status(update_domain_lock_status_request_content)
        print("The response of DomainsApi->update_domain_lock_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_lock_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_domain_lock_status_request_content** | [**UpdateDomainLockStatusRequestContent**](UpdateDomainLockStatusRequestContent.md)|  | 

### Return type

[**UpdateDomainLockStatusResponseContent**](UpdateDomainLockStatusResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateDomainLockStatus 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_nameservers**
> UpdateDomainNameserversResponseContent update_domain_nameservers(update_domain_nameservers_request_content)

Updates nameservers for an owned domain. ns1 and ns2 are required; ns3 through ns5 are optional.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_domain_nameservers_request_content import UpdateDomainNameserversRequestContent
from ha_sdk_python.models.update_domain_nameservers_response_content import UpdateDomainNameserversResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    update_domain_nameservers_request_content = ha_sdk_python.UpdateDomainNameserversRequestContent() # UpdateDomainNameserversRequestContent | 

    try:
        api_response = api_instance.update_domain_nameservers(update_domain_nameservers_request_content)
        print("The response of DomainsApi->update_domain_nameservers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_nameservers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_domain_nameservers_request_content** | [**UpdateDomainNameserversRequestContent**](UpdateDomainNameserversRequestContent.md)|  | 

### Return type

[**UpdateDomainNameserversResponseContent**](UpdateDomainNameserversResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateDomainNameservers 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_settings**
> UpdateDomainSettingsResponseContent update_domain_settings(update_domain_settings_request_content)

Updates a single domain setting (auto-renew, ID protection, or paid addons). One setting per request.

### Example

* Bearer Authentication (BearerAuth):

```python
import ha_sdk_python
from ha_sdk_python.models.update_domain_settings_request_content import UpdateDomainSettingsRequestContent
from ha_sdk_python.models.update_domain_settings_response_content import UpdateDomainSettingsResponseContent
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
    api_instance = ha_sdk_python.DomainsApi(api_client)
    update_domain_settings_request_content = ha_sdk_python.UpdateDomainSettingsRequestContent() # UpdateDomainSettingsRequestContent | 

    try:
        api_response = api_instance.update_domain_settings(update_domain_settings_request_content)
        print("The response of DomainsApi->update_domain_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_domain_settings_request_content** | [**UpdateDomainSettingsRequestContent**](UpdateDomainSettingsRequestContent.md)|  | 

### Return type

[**UpdateDomainSettingsResponseContent**](UpdateDomainSettingsResponseContent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UpdateDomainSettings 200 response |  -  |
**400** | BadRequestError 400 response |  -  |
**401** | UnauthorizedError 401 response |  -  |
**403** | ForbiddenError 403 response |  -  |
**404** | ResourceNotFoundError 404 response |  -  |
**422** | ValidationError 422 response |  -  |
**429** | TooManyRequestsError 429 response |  * Retry-After - Number of seconds to wait before retrying <br>  |
**500** | InternalServiceError 500 response |  -  |
**503** | ServiceUnavailableError 503 response |  * Retry-After - Number of seconds to wait before retrying <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

