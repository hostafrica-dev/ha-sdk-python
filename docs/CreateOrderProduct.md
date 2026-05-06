# CreateOrderProduct

A single product line item in a create order request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **int** | WHMCS product ID | 
**billing_cycle** | **str** | Billing cycle (e.g. monthly, annually) | 
**plan_id** | **int** | Plan ID for the selected product configuration | 
**hostname** | **str** | Hostname to assign to the service | 
**config_options** | **object** | Configuration options as a free-form map | 
**additional_data** | **object** | Additional data as a free-form map | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_order_product import CreateOrderProduct

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderProduct from a JSON string
create_order_product_instance = CreateOrderProduct.from_json(json)
# print the JSON string representation of the object
print(CreateOrderProduct.to_json())

# convert the object into a dict
create_order_product_dict = create_order_product_instance.to_dict()
# create an instance of CreateOrderProduct from a dict
create_order_product_from_dict = CreateOrderProduct.from_dict(create_order_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


