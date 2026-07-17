# UpdateDomainSettingsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**UpdateDomainSettingsData**](UpdateDomainSettingsData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_domain_settings_response_content import UpdateDomainSettingsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainSettingsResponseContent from a JSON string
update_domain_settings_response_content_instance = UpdateDomainSettingsResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainSettingsResponseContent.to_json())

# convert the object into a dict
update_domain_settings_response_content_dict = update_domain_settings_response_content_instance.to_dict()
# create an instance of UpdateDomainSettingsResponseContent from a dict
update_domain_settings_response_content_from_dict = UpdateDomainSettingsResponseContent.from_dict(update_domain_settings_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


