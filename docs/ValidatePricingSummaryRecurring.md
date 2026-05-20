# ValidatePricingSummaryRecurring

Recurring totals in the order summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before_discount** | **str** |  | 
**discount** | **str** |  | 
**after_discount** | **str** |  | 

## Example

```python
from ha_sdk_python.models.validate_pricing_summary_recurring import ValidatePricingSummaryRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingSummaryRecurring from a JSON string
validate_pricing_summary_recurring_instance = ValidatePricingSummaryRecurring.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingSummaryRecurring.to_json())

# convert the object into a dict
validate_pricing_summary_recurring_dict = validate_pricing_summary_recurring_instance.to_dict()
# create an instance of ValidatePricingSummaryRecurring from a dict
validate_pricing_summary_recurring_from_dict = ValidatePricingSummaryRecurring.from_dict(validate_pricing_summary_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


