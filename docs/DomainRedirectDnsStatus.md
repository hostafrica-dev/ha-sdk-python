# DomainRedirectDnsStatus

DNS readiness flags for domain redirect setup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_missing** | **bool** | True when the domain has no DNS zone yet | [optional] 
**has_a_record** | **bool** | True when @ and www A records point at the redirector | [optional] 
**override_required** | **bool** | True when conflicting @/www A records require override&#x3D;true on add-redirect | [optional] 
**conflicting_records** | [**List[DomainRedirectConflictingRecord]**](DomainRedirectConflictingRecord.md) | Conflicting A records that would be replaced when override&#x3D;true | [optional] 

## Example

```python
from ha_sdk_python.models.domain_redirect_dns_status import DomainRedirectDnsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRedirectDnsStatus from a JSON string
domain_redirect_dns_status_instance = DomainRedirectDnsStatus.from_json(json)
# print the JSON string representation of the object
print(DomainRedirectDnsStatus.to_json())

# convert the object into a dict
domain_redirect_dns_status_dict = domain_redirect_dns_status_instance.to_dict()
# create an instance of DomainRedirectDnsStatus from a dict
domain_redirect_dns_status_from_dict = DomainRedirectDnsStatus.from_dict(domain_redirect_dns_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


