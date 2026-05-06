# CreateOrderInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo** | **str** | Promotional code to apply to the order | [optional] 
**products** | [**List[CreateOrderProduct]**](CreateOrderProduct.md) | List of products to order | 

## Example

```python
from hostafrica_sdk_python.models.create_order_input import CreateOrderInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderInput from a JSON string
create_order_input_instance = CreateOrderInput.from_json(json)
# print the JSON string representation of the object
print(CreateOrderInput.to_json())

# convert the object into a dict
create_order_input_dict = create_order_input_instance.to_dict()
# create an instance of CreateOrderInput from a dict
create_order_input_from_dict = CreateOrderInput.from_dict(create_order_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


