# DomainHostingLink

Linked hosting service for a domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosting_id** | **int** | Linked hosting service id | 
**module** | **str** | Hosting module name (e.g. cpanel) | 

## Example

```python
from ha_sdk_python.models.domain_hosting_link import DomainHostingLink

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHostingLink from a JSON string
domain_hosting_link_instance = DomainHostingLink.from_json(json)
# print the JSON string representation of the object
print(DomainHostingLink.to_json())

# convert the object into a dict
domain_hosting_link_dict = domain_hosting_link_instance.to_dict()
# create an instance of DomainHostingLink from a dict
domain_hosting_link_from_dict = DomainHostingLink.from_dict(domain_hosting_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


