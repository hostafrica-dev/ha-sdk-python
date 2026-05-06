# ValidatePricingProductResult

Per-product pricing detail in the validate pricing response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **int** |  | 
**name** | **str** |  | 
**billing_cycle** | **str** |  | 
**plan_id** | **int** |  | [optional] 
**prorata** | [**ValidatePricingProrata**](ValidatePricingProrata.md) |  | [optional] 
**recurring_price** | [**ValidatePricingPriceRange**](ValidatePricingPriceRange.md) |  | [optional] 
**discount** | [**ValidatePricingDiscount**](ValidatePricingDiscount.md) |  | [optional] 
**line_total_before_discount** | **str** |  | 
**line_total** | **str** |  | 
**breakdown** | [**ValidatePricingBreakdown**](ValidatePricingBreakdown.md) |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_product_result import ValidatePricingProductResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingProductResult from a JSON string
validate_pricing_product_result_instance = ValidatePricingProductResult.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingProductResult.to_json())

# convert the object into a dict
validate_pricing_product_result_dict = validate_pricing_product_result_instance.to_dict()
# create an instance of ValidatePricingProductResult from a dict
validate_pricing_product_result_from_dict = ValidatePricingProductResult.from_dict(validate_pricing_product_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


