# ha_sdk_python.DomainsApi

All URIs are relative to *https://api.hostafrica.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_domain_availability**](DomainsApi.md#check_domain_availability) | **POST** /domain/check-availability | 
[**get_domain**](DomainsApi.md#get_domain) | **POST** /domain/get-domain | 
[**get_domain_contacts**](DomainsApi.md#get_domain_contacts) | **POST** /domain/get-domain-contacts | 
[**list_domains**](DomainsApi.md#list_domains) | **POST** /domain/list-domains | 
[**list_domains_requiring_data**](DomainsApi.md#list_domains_requiring_data) | **POST** /domain/list-domains-requiring-data | 
[**save_domain_required_data**](DomainsApi.md#save_domain_required_data) | **POST** /domain/save-domain-required-data | 
[**suggest_domains**](DomainsApi.md#suggest_domains) | **POST** /domain/suggest | 
[**update_domain_settings**](DomainsApi.md#update_domain_settings) | **POST** /domain/update-domain-settings | 


# **check_domain_availability**
> CheckDomainAvailabilityResponseContent check_domain_availability(check_domain_availability_request_content=check_domain_availability_request_content)

Checks domain name availability for a single domain or a comma-separated batch. Exactly one of domain or domains must be provided. Returns pricing, suggestions, and register_url scoped to the requested currency.

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

Generates AI-powered domain name suggestions from a natural-language description. Returns suggested domains with availability status and pricing.

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

