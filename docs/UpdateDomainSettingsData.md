# UpdateDomainSettingsData

Response data for update-domain-settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain_id** | **str** | Domain service id as returned by upstream | 
**setting** | [**DomainSettingKey**](DomainSettingKey.md) |  | 
**value** | **bool** | Boolean value requested | 
**requires_payment** | **bool** | True when payment must be completed before a paid addon is enabled | 
**invoice_id** | **int** | Invoice id when requires_payment is true | [optional] 
**amount** | **float** | Invoice amount in client currency when requires_payment is true | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_settings_data import UpdateDomainSettingsData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainSettingsData from a JSON string
update_domain_settings_data_instance = UpdateDomainSettingsData.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainSettingsData.to_json())

# convert the object into a dict
update_domain_settings_data_dict = update_domain_settings_data_instance.to_dict()
# create an instance of UpdateDomainSettingsData from a dict
update_domain_settings_data_from_dict = UpdateDomainSettingsData.from_dict(update_domain_settings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


