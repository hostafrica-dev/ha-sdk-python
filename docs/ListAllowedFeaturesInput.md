# ListAllowedFeaturesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_allowed_features_input import ListAllowedFeaturesInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllowedFeaturesInput from a JSON string
list_allowed_features_input_instance = ListAllowedFeaturesInput.from_json(json)
# print the JSON string representation of the object
print(ListAllowedFeaturesInput.to_json())

# convert the object into a dict
list_allowed_features_input_dict = list_allowed_features_input_instance.to_dict()
# create an instance of ListAllowedFeaturesInput from a dict
list_allowed_features_input_from_dict = ListAllowedFeaturesInput.from_dict(list_allowed_features_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


