# ValidatePricingResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ValidatePricingResponseData**](ValidatePricingResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_response_content import ValidatePricingResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingResponseContent from a JSON string
validate_pricing_response_content_instance = ValidatePricingResponseContent.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingResponseContent.to_json())

# convert the object into a dict
validate_pricing_response_content_dict = validate_pricing_response_content_instance.to_dict()
# create an instance of ValidatePricingResponseContent from a dict
validate_pricing_response_content_from_dict = ValidatePricingResponseContent.from_dict(validate_pricing_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


