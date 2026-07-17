# SaveDomainRequiredDataRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**fields** | **Dict[str, str]** | Registrar field values keyed by additionalFields[].name | 

## Example

```python
from ha_sdk_python.models.save_domain_required_data_request_content import SaveDomainRequiredDataRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of SaveDomainRequiredDataRequestContent from a JSON string
save_domain_required_data_request_content_instance = SaveDomainRequiredDataRequestContent.from_json(json)
# print the JSON string representation of the object
print(SaveDomainRequiredDataRequestContent.to_json())

# convert the object into a dict
save_domain_required_data_request_content_dict = save_domain_required_data_request_content_instance.to_dict()
# create an instance of SaveDomainRequiredDataRequestContent from a dict
save_domain_required_data_request_content_from_dict = SaveDomainRequiredDataRequestContent.from_dict(save_domain_required_data_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


