# ValidatePricingResponseData

Top-level data payload for the ValidatePricing response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**ValidatePricingCurrency**](ValidatePricingCurrency.md) |  | 
**products** | [**List[ValidatePricingProductResult]**](ValidatePricingProductResult.md) |  | 
**summary** | [**ValidatePricingSummary**](ValidatePricingSummary.md) |  | 
**errors** | **List[str]** | List of strings | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_response_data import ValidatePricingResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingResponseData from a JSON string
validate_pricing_response_data_instance = ValidatePricingResponseData.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingResponseData.to_json())

# convert the object into a dict
validate_pricing_response_data_dict = validate_pricing_response_data_instance.to_dict()
# create an instance of ValidatePricingResponseData from a dict
validate_pricing_response_data_from_dict = ValidatePricingResponseData.from_dict(validate_pricing_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


