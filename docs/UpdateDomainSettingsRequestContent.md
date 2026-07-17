# UpdateDomainSettingsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**setting** | [**DomainSettingKey**](DomainSettingKey.md) |  | 
**value** | **bool** | New boolean value | 
**gateway** | **str** | Payment gateway slug when enabling a paid addon (e.g. stripe) | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_settings_request_content import UpdateDomainSettingsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainSettingsRequestContent from a JSON string
update_domain_settings_request_content_instance = UpdateDomainSettingsRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainSettingsRequestContent.to_json())

# convert the object into a dict
update_domain_settings_request_content_dict = update_domain_settings_request_content_instance.to_dict()
# create an instance of UpdateDomainSettingsRequestContent from a dict
update_domain_settings_request_content_from_dict = UpdateDomainSettingsRequestContent.from_dict(update_domain_settings_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


