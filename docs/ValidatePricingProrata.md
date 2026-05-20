# ValidatePricingProrata

Prorata charge details for a product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** |  | 
**amount** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**days** | **int** |  | [optional] 

## Example

```python
from ha_sdk_python.models.validate_pricing_prorata import ValidatePricingProrata

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingProrata from a JSON string
validate_pricing_prorata_instance = ValidatePricingProrata.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingProrata.to_json())

# convert the object into a dict
validate_pricing_prorata_dict = validate_pricing_prorata_instance.to_dict()
# create an instance of ValidatePricingProrata from a dict
validate_pricing_prorata_from_dict = ValidatePricingProrata.from_dict(validate_pricing_prorata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


