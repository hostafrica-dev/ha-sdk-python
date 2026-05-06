# ListAllowedFeaturesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**AllowedFeaturesResponseData**](AllowedFeaturesResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_allowed_features_output import ListAllowedFeaturesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllowedFeaturesOutput from a JSON string
list_allowed_features_output_instance = ListAllowedFeaturesOutput.from_json(json)
# print the JSON string representation of the object
print(ListAllowedFeaturesOutput.to_json())

# convert the object into a dict
list_allowed_features_output_dict = list_allowed_features_output_instance.to_dict()
# create an instance of ListAllowedFeaturesOutput from a dict
list_allowed_features_output_from_dict = ListAllowedFeaturesOutput.from_dict(list_allowed_features_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


