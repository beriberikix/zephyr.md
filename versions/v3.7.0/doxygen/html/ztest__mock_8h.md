---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ztest__mock_8h.html
original_path: doxygen/html/ztest__mock_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_mock.h File Reference

Ztest mocking support.
[More...](#details)

[Go to the source code of this file.](ztest__mock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ztest\_expect\_value](group__ztest__mock.md#ga58c2f0c0e628e73a2268a3d18b0440d6)(func, param, value) |
|  | Tell function *func* to expect the value *value* for *param*. |
| #define | [ztest\_check\_expected\_value](group__ztest__mock.md#gae9af6ba8e51738e938763c896f17ea8f)(param) |
|  | If *param* doesn't match the value set by [ztest\_expect\_value()](group__ztest__mock.md#ga58c2f0c0e628e73a2268a3d18b0440d6 "Tell function func to expect the value value for param."), fail the test. |
| #define | [ztest\_expect\_data](group__ztest__mock.md#gac1a64d8bf9c877e8666e0c6d93b0dbab)(func, param, data) |
|  | Tell function *func* to expect the data *data* for *param*. |
| #define | [ztest\_check\_expected\_data](group__ztest__mock.md#ga805cf99272f147beeeee5ad6ca2553f5)(param, length) |
|  | If data pointed by *param* don't match the data set by [ztest\_expect\_data()](group__ztest__mock.md#gac1a64d8bf9c877e8666e0c6d93b0dbab "Tell function func to expect the data data for param."), fail the test. |
| #define | [ztest\_return\_data](group__ztest__mock.md#gac79d097a6b274b25286f2b0e80fbd6e9)(func, param, data) |
|  | Tell function *func* to return the data *data* for *param*. |
| #define | [ztest\_copy\_return\_data](group__ztest__mock.md#ga12872a3d783d53d564ed94583bc490b0)(param, length) |
|  | Copy the data set by ztest\_return\_data to the memory pointed by *param*. |
| #define | [ztest\_returns\_value](group__ztest__mock.md#ga2ec539b4c0f3e4efb695213b4fd08c2c)(func, value) |
|  | Tell *func* that it should return *value*. |
| #define | [ztest\_get\_return\_value](group__ztest__mock.md#ga31dcd5b5a3596a7404a771a2d32f3a39)() |
|  | Get the return value for current function. |
| #define | [ztest\_get\_return\_value\_ptr](group__ztest__mock.md#gaa2df2eaeba49019b7a83ac769ea95968)() |
|  | Get the return value as a pointer for current function. |

## Detailed Description

Ztest mocking support.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_mock.h](ztest__mock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
