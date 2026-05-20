# ValidatePricingBase

Base price breakdown (recurring + setup)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring** | **str** |  | 
**setup** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_base import ValidatePricingBase

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingBase from a JSON string
validate_pricing_base_instance = ValidatePricingBase.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingBase.to_json())

# convert the object into a dict
validate_pricing_base_dict = validate_pricing_base_instance.to_dict()
# create an instance of ValidatePricingBase from a dict
validate_pricing_base_from_dict = ValidatePricingBase.from_dict(validate_pricing_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


