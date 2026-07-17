# DomainSearchResponseData

Response data for domain availability and suggestion operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[DomainAvailabilityResult]**](DomainAvailabilityResult.md) | Domain availability results | 
**suggestions** | **List[str]** | Alternative domain suggestions (single-domain lookup only) | [optional] 
**currency** | **int** | Upstream currency identifier | 
**currency_code** | **str** | ISO currency code for the quoted prices | 
**currency_note** | **str** | Note that prices and register_url are valid only for currency_code | 
**warnings** | **List[str]** | Non-fatal warnings the client should be aware of | [optional] 

## Example

```python
from ha_sdk_python.models.domain_search_response_data import DomainSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainSearchResponseData from a JSON string
domain_search_response_data_instance = DomainSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(DomainSearchResponseData.to_json())

# convert the object into a dict
domain_search_response_data_dict = domain_search_response_data_instance.to_dict()
# create an instance of DomainSearchResponseData from a dict
domain_search_response_data_from_dict = DomainSearchResponseData.from_dict(domain_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


