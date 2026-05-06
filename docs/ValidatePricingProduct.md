# ValidatePricingProduct

A single product line item in a validate pricing request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **int** | WHMCS product ID | 
**billing_cycle** | **str** | Billing cycle (e.g. monthly, annually) | 
**plan_id** | **int** | Plan ID for the selected product configuration | 
**hostname** | **str** | Hostname to assign to the service | [optional] 
**config_options** | **object** | Configuration options as a free-form map (option_id -&gt; value) | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_product import ValidatePricingProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingProduct from a JSON string
validate_pricing_product_instance = ValidatePricingProduct.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingProduct.to_json())

# convert the object into a dict
validate_pricing_product_dict = validate_pricing_product_instance.to_dict()
# create an instance of ValidatePricingProduct from a dict
validate_pricing_product_from_dict = ValidatePricingProduct.from_dict(validate_pricing_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


