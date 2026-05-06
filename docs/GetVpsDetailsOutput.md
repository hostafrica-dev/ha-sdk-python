# GetVpsDetailsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsDetailsResponse**](VpsDetailsResponse.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_vps_details_output import GetVpsDetailsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetVpsDetailsOutput from a JSON string
get_vps_details_output_instance = GetVpsDetailsOutput.from_json(json)
# print the JSON string representation of the object
print(GetVpsDetailsOutput.to_json())

# convert the object into a dict
get_vps_details_output_dict = get_vps_details_output_instance.to_dict()
# create an instance of GetVpsDetailsOutput from a dict
get_vps_details_output_from_dict = GetVpsDetailsOutput.from_dict(get_vps_details_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


