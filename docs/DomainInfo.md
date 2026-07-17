# DomainInfo

Summary of an owned domain returned by list operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id | 
**type** | **str** | Domain operation type (e.g. Register, Transfer) | 
**domain** | **str** | Fully qualified domain name | 
**status** | **str** | Domain status (e.g. Active, Expired, Cancelled) | 
**period** | **int** | Registration or billing period in years | 
**donotrenew** | **int** | Renewal flag: 0 &#x3D; renew, 1 &#x3D; do not renew | 
**id_protection** | **int** | WHOIS privacy enabled: 0 &#x3D; off, 1 &#x3D; on | 
**id_protection_supported** | **bool** | Whether the TLD supports ID protection | 
**recurringamount** | **str** | Recurring amount as a decimal string (e.g. \&quot;149.99\&quot;) | 
**expirydate** | **str** | Domain expiry date (YYYY-MM-DD) | [optional] 
**nextinvoicedate** | **str** | Next invoice date (YYYY-MM-DD) | [optional] 
**nextduedate** | **str** | Next due date (YYYY-MM-DD) | [optional] 
**has_hosting** | [**DomainHostingLink**](DomainHostingLink.md) |  | [optional] 
**has_dns_manager_zone** | **bool** | Whether a DNS Manager zone exists for this domain name | 
**evaluation** | **object** | Domain evaluator result when enabled; null when unavailable | [optional] 

## Example

```python
from ha_sdk_python.models.domain_info import DomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainInfo from a JSON string
domain_info_instance = DomainInfo.from_json(json)
# print the JSON string representation of the object
print(DomainInfo.to_json())

# convert the object into a dict
domain_info_dict = domain_info_instance.to_dict()
# create an instance of DomainInfo from a dict
domain_info_from_dict = DomainInfo.from_dict(domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


