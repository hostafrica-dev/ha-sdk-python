# ShutdownVpsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.shutdown_vps_response_content import ShutdownVpsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownVpsResponseContent from a JSON string
shutdown_vps_response_content_instance = ShutdownVpsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ShutdownVpsResponseContent.to_json())

# convert the object into a dict
shutdown_vps_response_content_dict = shutdown_vps_response_content_instance.to_dict()
# create an instance of ShutdownVpsResponseContent from a dict
shutdown_vps_response_content_from_dict = ShutdownVpsResponseContent.from_dict(shutdown_vps_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


