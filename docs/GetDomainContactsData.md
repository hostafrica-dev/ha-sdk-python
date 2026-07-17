# GetDomainContactsData

Domain contact information returned by get-domain-contacts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain_id** | **str** | Domain service id | 
**domain** | **str** | Fully qualified domain name | 
**contacts** | **object** | Contact roles keyed by Registrant, Admin, Tech, and Billing, or an array of contact records. Inner field names and values vary by TLD/registrar. | 

## Example

```python
from ha_sdk_python.models.get_domain_contacts_data import GetDomainContactsData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainContactsData from a JSON string
get_domain_contacts_data_instance = GetDomainContactsData.from_json(json)
# print the JSON string representation of the object
print(GetDomainContactsData.to_json())

# convert the object into a dict
get_domain_contacts_data_dict = get_domain_contacts_data_instance.to_dict()
# create an instance of GetDomainContactsData from a dict
get_domain_contacts_data_from_dict = GetDomainContactsData.from_dict(get_domain_contacts_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


