# ValidatePricingBreakdown

Full breakdown of a product's pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**ValidatePricingBase**](ValidatePricingBase.md) |  | 
**configuration** | [**List[ValidatePricingConfigItem]**](ValidatePricingConfigItem.md) |  | 
**setup_total** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_breakdown import ValidatePricingBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingBreakdown from a JSON string
validate_pricing_breakdown_instance = ValidatePricingBreakdown.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingBreakdown.to_json())

# convert the object into a dict
validate_pricing_breakdown_dict = validate_pricing_breakdown_instance.to_dict()
# create an instance of ValidatePricingBreakdown from a dict
validate_pricing_breakdown_from_dict = ValidatePricingBreakdown.from_dict(validate_pricing_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


