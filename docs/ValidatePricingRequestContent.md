# ValidatePricingRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo** | **str** | Optional promotional code to apply | [optional] 
**products** | [**List[ValidatePricingProduct]**](ValidatePricingProduct.md) | List of products to validate pricing for | 

## Example

```python
from hostafrica_sdk_python.models.validate_pricing_request_content import ValidatePricingRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePricingRequestContent from a JSON string
validate_pricing_request_content_instance = ValidatePricingRequestContent.from_json(json)
# print the JSON string representation of the object
print(ValidatePricingRequestContent.to_json())

# convert the object into a dict
validate_pricing_request_content_dict = validate_pricing_request_content_instance.to_dict()
# create an instance of ValidatePricingRequestContent from a dict
validate_pricing_request_content_from_dict = ValidatePricingRequestContent.from_dict(validate_pricing_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


