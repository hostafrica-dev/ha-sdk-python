# DomainContacts

WHOIS contacts keyed by contact role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registrant** | **Dict[str, str]** | WHOIS contact field values for one role; field names vary by TLD/registrar | [optional] 
**admin** | **Dict[str, str]** | WHOIS contact field values for one role; field names vary by TLD/registrar | [optional] 
**tech** | **Dict[str, str]** | WHOIS contact field values for one role; field names vary by TLD/registrar | [optional] 
**billing** | **Dict[str, str]** | WHOIS contact field values for one role; field names vary by TLD/registrar | [optional] 

## Example

```python
from ha_sdk_python.models.domain_contacts import DomainContacts

# TODO update the JSON string below
json = "{}"
# create an instance of DomainContacts from a JSON string
domain_contacts_instance = DomainContacts.from_json(json)
# print the JSON string representation of the object
print(DomainContacts.to_json())

# convert the object into a dict
domain_contacts_dict = domain_contacts_instance.to_dict()
# create an instance of DomainContacts from a dict
domain_contacts_from_dict = DomainContacts.from_dict(domain_contacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


