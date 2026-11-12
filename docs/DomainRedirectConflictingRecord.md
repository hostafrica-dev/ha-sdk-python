# DomainRedirectConflictingRecord

Conflicting A record that blocks redirect setup without override=true

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | Zone line / record id when present | [optional] 
**name** | **str** | Record name (e.g. @, www, or FQDN) | [optional] 
**type** | **str** | Record type (typically A) | [optional] 
**value** | **str** | Record IP value when present | [optional] 

## Example

```python
from ha_sdk_python.models.domain_redirect_conflicting_record import DomainRedirectConflictingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRedirectConflictingRecord from a JSON string
domain_redirect_conflicting_record_instance = DomainRedirectConflictingRecord.from_json(json)
# print the JSON string representation of the object
print(DomainRedirectConflictingRecord.to_json())

# convert the object into a dict
domain_redirect_conflicting_record_dict = domain_redirect_conflicting_record_instance.to_dict()
# create an instance of DomainRedirectConflictingRecord from a dict
domain_redirect_conflicting_record_from_dict = DomainRedirectConflictingRecord.from_dict(domain_redirect_conflicting_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


