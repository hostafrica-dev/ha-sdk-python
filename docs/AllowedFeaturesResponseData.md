# AllowedFeaturesResponseData

Response data for allowed features operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**features** | [**VpsAvailableFeatures**](VpsAvailableFeatures.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.allowed_features_response_data import AllowedFeaturesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedFeaturesResponseData from a JSON string
allowed_features_response_data_instance = AllowedFeaturesResponseData.from_json(json)
# print the JSON string representation of the object
print(AllowedFeaturesResponseData.to_json())

# convert the object into a dict
allowed_features_response_data_dict = allowed_features_response_data_instance.to_dict()
# create an instance of AllowedFeaturesResponseData from a dict
allowed_features_response_data_from_dict = AllowedFeaturesResponseData.from_dict(allowed_features_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


