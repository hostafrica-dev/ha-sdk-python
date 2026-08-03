# DomainNameservers

Nameserver hostnames applied to a domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns1** | **str** | Primary nameserver hostname | [optional] 
**ns2** | **str** | Secondary nameserver hostname | [optional] 
**ns3** | **str** | Optional tertiary nameserver hostname | [optional] 
**ns4** | **str** | Optional quaternary nameserver hostname | [optional] 
**ns5** | **str** | Optional fifth nameserver hostname | [optional] 

## Example

```python
from ha_sdk_python.models.domain_nameservers import DomainNameservers

# TODO update the JSON string below
json = "{}"
# create an instance of DomainNameservers from a JSON string
domain_nameservers_instance = DomainNameservers.from_json(json)
# print the JSON string representation of the object
print(DomainNameservers.to_json())

# convert the object into a dict
domain_nameservers_dict = domain_nameservers_instance.to_dict()
# create an instance of DomainNameservers from a dict
domain_nameservers_from_dict = DomainNameservers.from_dict(domain_nameservers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


