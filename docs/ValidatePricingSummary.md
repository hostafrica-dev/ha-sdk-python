# ValidatePricingSummary

Order-level summary of totals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtotal** | **str** |  | 
**discount_total** | **str** |  | 
**total_due** | **str** |  | 
**recurring** | [**ValidatePricingSummaryRecurring**](ValidatePricingSummaryRecurring.md) |  | [optional] 
**prorata_total** | **str** |  | [optional] 
**promo_applied** | **str** |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_summary import ValidatePricingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingSummary from a JSON string
validate_pricing_summary_instance = ValidatePricingSummary.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingSummary.to_json())

# convert the object into a dict
validate_pricing_summary_dict = validate_pricing_summary_instance.to_dict()
# create an instance of ValidatePricingSummary from a dict
validate_pricing_summary_from_dict = ValidatePricingSummary.from_dict(validate_pricing_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


