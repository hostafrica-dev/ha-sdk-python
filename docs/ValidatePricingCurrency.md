# ValidatePricingCurrency

Currency info in the pricing validation response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**prefix** | **str** |  | 
**suffix** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_currency import ValidatePricingCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingCurrency from a JSON string
validate_pricing_currency_instance = ValidatePricingCurrency.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingCurrency.to_json())

# convert the object into a dict
validate_pricing_currency_dict = validate_pricing_currency_instance.to_dict()
# create an instance of ValidatePricingCurrency from a dict
validate_pricing_currency_from_dict = ValidatePricingCurrency.from_dict(validate_pricing_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


