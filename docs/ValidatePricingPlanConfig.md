# ValidatePricingPlanConfig

Plan configuration included in pricing breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | [optional] 
**ram** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**bandwidth** | **int** |  | [optional] 
**backups** | **int** |  | [optional] 
**snapshots** | **int** |  | [optional] 

## Example

```python
from ha_sdk_python.models.validate_pricing_plan_config import ValidatePricingPlanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingPlanConfig from a JSON string
validate_pricing_plan_config_instance = ValidatePricingPlanConfig.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingPlanConfig.to_json())

# convert the object into a dict
validate_pricing_plan_config_dict = validate_pricing_plan_config_instance.to_dict()
# create an instance of ValidatePricingPlanConfig from a dict
validate_pricing_plan_config_from_dict = ValidatePricingPlanConfig.from_dict(validate_pricing_plan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


