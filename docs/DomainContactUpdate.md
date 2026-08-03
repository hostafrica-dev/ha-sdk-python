# DomainContactUpdate

Update payload for one WHOIS contact role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DomainContactSourceType**](DomainContactSourceType.md) |  | 
**id** | **int** | Saved WHMCS contact id; required when type is contact | [optional] 
**fields** | **Dict[str, str]** | WHOIS contact field values for one role; field names vary by TLD/registrar | [optional] 

## Example

```python
from ha_sdk_python.models.domain_contact_update import DomainContactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DomainContactUpdate from a JSON string
domain_contact_update_instance = DomainContactUpdate.from_json(json)
# print the JSON string representation of the object
print(DomainContactUpdate.to_json())

# convert the object into a dict
domain_contact_update_dict = domain_contact_update_instance.to_dict()
# create an instance of DomainContactUpdate from a dict
domain_contact_update_from_dict = DomainContactUpdate.from_dict(domain_contact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


