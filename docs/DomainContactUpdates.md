# DomainContactUpdates

WHOIS contact updates keyed by Registrant, Admin, Tech, and Billing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registrant** | [**DomainContactUpdate**](DomainContactUpdate.md) |  | [optional] 
**admin** | [**DomainContactUpdate**](DomainContactUpdate.md) |  | [optional] 
**tech** | [**DomainContactUpdate**](DomainContactUpdate.md) |  | [optional] 
**billing** | [**DomainContactUpdate**](DomainContactUpdate.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.domain_contact_updates import DomainContactUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of DomainContactUpdates from a JSON string
domain_contact_updates_instance = DomainContactUpdates.from_json(json)
# print the JSON string representation of the object
print(DomainContactUpdates.to_json())

# convert the object into a dict
domain_contact_updates_dict = domain_contact_updates_instance.to_dict()
# create an instance of DomainContactUpdates from a dict
domain_contact_updates_from_dict = DomainContactUpdates.from_dict(domain_contact_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


