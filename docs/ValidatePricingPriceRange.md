# ValidatePricingPriceRange

Price before and after discount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before_discount** | **str** |  | 
**discount** | **str** |  | 
**after_discount** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_price_range import ValidatePricingPriceRange

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingPriceRange from a JSON string
validate_pricing_price_range_instance = ValidatePricingPriceRange.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingPriceRange.to_json())

# convert the object into a dict
validate_pricing_price_range_dict = validate_pricing_price_range_instance.to_dict()
# create an instance of ValidatePricingPriceRange from a dict
validate_pricing_price_range_from_dict = ValidatePricingPriceRange.from_dict(validate_pricing_price_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


