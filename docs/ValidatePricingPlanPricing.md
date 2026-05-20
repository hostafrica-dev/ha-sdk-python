# ValidatePricingPlanPricing

Pricing detail within a plan configuration item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** |  | 
**setup** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_plan_pricing import ValidatePricingPlanPricing

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingPlanPricing from a JSON string
validate_pricing_plan_pricing_instance = ValidatePricingPlanPricing.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingPlanPricing.to_json())

# convert the object into a dict
validate_pricing_plan_pricing_dict = validate_pricing_plan_pricing_instance.to_dict()
# create an instance of ValidatePricingPlanPricing from a dict
validate_pricing_plan_pricing_from_dict = ValidatePricingPlanPricing.from_dict(validate_pricing_plan_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


