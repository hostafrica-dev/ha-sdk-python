# ValidatePricingInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo** | **str** | Optional promotional code to apply | [optional] 
**products** | [**List[ValidatePricingProduct]**](ValidatePricingProduct.md) | List of products to validate pricing for | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_input import ValidatePricingInput

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingInput from a JSON string
validate_pricing_input_instance = ValidatePricingInput.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingInput.to_json())

# convert the object into a dict
validate_pricing_input_dict = validate_pricing_input_instance.to_dict()
# create an instance of ValidatePricingInput from a dict
validate_pricing_input_from_dict = ValidatePricingInput.from_dict(validate_pricing_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


