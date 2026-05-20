# ValidatePricingConfigItem

A single configuration item in the pricing breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_id** | **int** | Option ID (absent for plan-type items) | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**selected** | **object** |  | 
**selected_name** | **str** |  | [optional] 
**plan_config** | [**ValidatePricingPlanConfig**](ValidatePricingPlanConfig.md) |  | [optional] 
**pricing** | [**ValidatePricingPlanPricing**](ValidatePricingPlanPricing.md) |  | [optional] 
**price** | **str** |  | [optional] 
**setup** | **str** |  | [optional] 

## Example

```python
from ha_sdk_python.models.validate_pricing_config_item import ValidatePricingConfigItem

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingConfigItem from a JSON string
validate_pricing_config_item_instance = ValidatePricingConfigItem.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingConfigItem.to_json())

# convert the object into a dict
validate_pricing_config_item_dict = validate_pricing_config_item_instance.to_dict()
# create an instance of ValidatePricingConfigItem from a dict
validate_pricing_config_item_from_dict = ValidatePricingConfigItem.from_dict(validate_pricing_config_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


