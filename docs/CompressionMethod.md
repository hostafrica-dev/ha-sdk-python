# CompressionMethod

Compression method option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Compression method value | 
**label** | **str** | Human-readable label for the compression method | 

## Example

```python
from ha_sdk_python.models.compression_method import CompressionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CompressionMethod from a JSON string
compression_method_instance = CompressionMethod.from_json(json)
# print the JSON string representation of the object
print(CompressionMethod.to_json())

# convert the object into a dict
compression_method_dict = compression_method_instance.to_dict()
# create an instance of CompressionMethod from a dict
compression_method_from_dict = CompressionMethod.from_dict(compression_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


