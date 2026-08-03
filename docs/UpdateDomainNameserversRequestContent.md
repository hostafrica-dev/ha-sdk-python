# UpdateDomainNameserversRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**ns1** | **str** | Primary nameserver hostname | 
**ns2** | **str** | Secondary nameserver hostname | 
**ns3** | **str** | Optional tertiary nameserver hostname | [optional] 
**ns4** | **str** | Optional quaternary nameserver hostname | [optional] 
**ns5** | **str** | Optional fifth nameserver hostname | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_nameservers_request_content import UpdateDomainNameserversRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainNameserversRequestContent from a JSON string
update_domain_nameservers_request_content_instance = UpdateDomainNameserversRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainNameserversRequestContent.to_json())

# convert the object into a dict
update_domain_nameservers_request_content_dict = update_domain_nameservers_request_content_instance.to_dict()
# create an instance of UpdateDomainNameserversRequestContent from a dict
update_domain_nameservers_request_content_from_dict = UpdateDomainNameserversRequestContent.from_dict(update_domain_nameservers_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


