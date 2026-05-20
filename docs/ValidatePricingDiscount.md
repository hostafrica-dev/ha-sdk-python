# ValidatePricingDiscount

Discount detail applied to a product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** |  | 
**code** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**amount** | **str** |  | 
**recurring_amount** | **str** |  | 
**apply_once** | **bool** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_discount import ValidatePricingDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingDiscount from a JSON string
validate_pricing_discount_instance = ValidatePricingDiscount.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingDiscount.to_json())

# convert the object into a dict
validate_pricing_discount_dict = validate_pricing_discount_instance.to_dict()
# create an instance of ValidatePricingDiscount from a dict
validate_pricing_discount_from_dict = ValidatePricingDiscount.from_dict(validate_pricing_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


