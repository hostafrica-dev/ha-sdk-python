# ListAllowedFeaturesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**AllowedFeaturesResponseData**](AllowedFeaturesResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_allowed_features_response_content import ListAllowedFeaturesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllowedFeaturesResponseContent from a JSON string
list_allowed_features_response_content_instance = ListAllowedFeaturesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListAllowedFeaturesResponseContent.to_json())

# convert the object into a dict
list_allowed_features_response_content_dict = list_allowed_features_response_content_instance.to_dict()
# create an instance of ListAllowedFeaturesResponseContent from a dict
list_allowed_features_response_content_from_dict = ListAllowedFeaturesResponseContent.from_dict(list_allowed_features_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


