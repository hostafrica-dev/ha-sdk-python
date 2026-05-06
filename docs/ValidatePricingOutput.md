# ValidatePricingOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ValidatePricingResponseData**](ValidatePricingResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_output import ValidatePricingOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingOutput from a JSON string
validate_pricing_output_instance = ValidatePricingOutput.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingOutput.to_json())

# convert the object into a dict
validate_pricing_output_dict = validate_pricing_output_instance.to_dict()
# create an instance of ValidatePricingOutput from a dict
validate_pricing_output_from_dict = ValidatePricingOutput.from_dict(validate_pricing_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


