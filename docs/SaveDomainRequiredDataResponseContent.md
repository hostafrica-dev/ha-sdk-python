# SaveDomainRequiredDataResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SaveDomainRequiredDataData**](SaveDomainRequiredDataData.md) |  | 

## Example

```python
from ha_sdk_python.models.save_domain_required_data_response_content import SaveDomainRequiredDataResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of SaveDomainRequiredDataResponseContent from a JSON string
save_domain_required_data_response_content_instance = SaveDomainRequiredDataResponseContent.from_json(json)
# print the JSON string representation of the object
print(SaveDomainRequiredDataResponseContent.to_json())

# convert the object into a dict
save_domain_required_data_response_content_dict = save_domain_required_data_response_content_instance.to_dict()
# create an instance of SaveDomainRequiredDataResponseContent from a dict
save_domain_required_data_response_content_from_dict = SaveDomainRequiredDataResponseContent.from_dict(save_domain_required_data_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


