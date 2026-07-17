# SaveDomainRequiredDataData

Response data for save-domain-required-data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain_id** | **str** | Domain service id | 

## Example

```python
from ha_sdk_python.models.save_domain_required_data_data import SaveDomainRequiredDataData

# TODO update the JSON string below
json = "{}"
# create an instance of SaveDomainRequiredDataData from a JSON string
save_domain_required_data_data_instance = SaveDomainRequiredDataData.from_json(json)
# print the JSON string representation of the object
print(SaveDomainRequiredDataData.to_json())

# convert the object into a dict
save_domain_required_data_data_dict = save_domain_required_data_data_instance.to_dict()
# create an instance of SaveDomainRequiredDataData from a dict
save_domain_required_data_data_from_dict = SaveDomainRequiredDataData.from_dict(save_domain_required_data_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


