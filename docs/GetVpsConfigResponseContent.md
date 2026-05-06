# GetVpsConfigResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsConfigResponseData**](VpsConfigResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_vps_config_response_content import GetVpsConfigResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsConfigResponseContent from a JSON string
get_vps_config_response_content_instance = GetVpsConfigResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetVpsConfigResponseContent.to_json())

# convert the object into a dict
get_vps_config_response_content_dict = get_vps_config_response_content_instance.to_dict()
# create an instance of GetVpsConfigResponseContent from a dict
get_vps_config_response_content_from_dict = GetVpsConfigResponseContent.from_dict(get_vps_config_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


