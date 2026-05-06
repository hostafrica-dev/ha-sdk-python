# UpdateVpsConfigResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_vps_config_response_content import UpdateVpsConfigResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVpsConfigResponseContent from a JSON string
update_vps_config_response_content_instance = UpdateVpsConfigResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateVpsConfigResponseContent.to_json())

# convert the object into a dict
update_vps_config_response_content_dict = update_vps_config_response_content_instance.to_dict()
# create an instance of UpdateVpsConfigResponseContent from a dict
update_vps_config_response_content_from_dict = UpdateVpsConfigResponseContent.from_dict(update_vps_config_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


