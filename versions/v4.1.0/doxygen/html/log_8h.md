---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log_8h.html
original_path: doxygen/html/log_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log.h File Reference

`#include <[zephyr/logging/log_instance.h](log__instance_8h_source.md)>`  
`#include <[zephyr/logging/log_core.h](log__core_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](log_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOG\_ERR](group__log__api.md#gad6db28c61c838c1f7316417e1e4847f2)(...) |
|  | Writes an ERROR level message to the log. |
| #define | [LOG\_WRN](group__log__api.md#ga644db4299681d9ebf06f8745ad984c65)(...) |
|  | Writes a WARNING level message to the log. |
| #define | [LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)(...) |
|  | Writes an INFO level message to the log. |
| #define | [LOG\_DBG](group__log__api.md#gafb97e6291db24665313453d192941330)(...) |
|  | Writes a DEBUG level message to the log. |
| #define | [LOG\_WRN\_ONCE](group__log__api.md#gaa9b22a7d4659030d9a3273f1f1e6786c)(...) |
|  | Writes a WARNING level message to the log on the first execution only. |
| #define | [LOG\_PRINTK](group__log__api.md#ga4ab5cae247b853bf9f4f0bf761c1c71e)(...) |
|  | Unconditionally print raw log message. |
| #define | [LOG\_RAW](group__log__api.md#ga7dedf58739648ed9b9aef1abe982f7d6)(...) |
|  | Unconditionally print raw log message. |
| #define | [LOG\_INST\_ERR](group__log__api.md#ga830f32743847c52e01a510ab0716fe90)(\_log\_inst, ...) |
|  | Writes an ERROR level message associated with the instance to the log. |
| #define | [LOG\_INST\_WRN](group__log__api.md#ga76057f789dfc164adbb1dbc9f3aff417)(\_log\_inst, ...) |
|  | Writes a WARNING level message associated with the instance to the log. |
| #define | [LOG\_INST\_INF](group__log__api.md#ga222c5b535fb3ecb36dea97885c794188)(\_log\_inst, ...) |
|  | Writes an INFO level message associated with the instance to the log. |
| #define | [LOG\_INST\_DBG](group__log__api.md#gae10014012020ea5a6b9a86a5224f19b0)(\_log\_inst, ...) |
|  | Writes a DEBUG level message associated with the instance to the log. |
| #define | [LOG\_HEXDUMP\_ERR](group__log__api.md#gabdae4f5b8b16804b53f83a85c3023134)(\_data, \_length, \_str) |
|  | Writes an ERROR level hexdump message to the log. |
| #define | [LOG\_HEXDUMP\_WRN](group__log__api.md#gaf73802661fea926bb2b7e628727cdceb)(\_data, \_length, \_str) |
|  | Writes a WARNING level message to the log. |
| #define | [LOG\_HEXDUMP\_INF](group__log__api.md#ga8e060bbe660c246a38adccd873e58c6c)(\_data, \_length, \_str) |
|  | Writes an INFO level message to the log. |
| #define | [LOG\_HEXDUMP\_DBG](group__log__api.md#ga01dda8273f7d453a855542a52524dca8)(\_data, \_length, \_str) |
|  | Writes a DEBUG level message to the log. |
| #define | [LOG\_INST\_HEXDUMP\_ERR](group__log__api.md#gaf2f504a779917dc0f40767cba9f940b9)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes an ERROR hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_WRN](group__log__api.md#gab6542651f88fbb0991fb2339102b52a5)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes a WARNING level hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_INF](group__log__api.md#ga8e38c461c6058ee604b4dddad662d4ca)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes an INFO level hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_DBG](group__log__api.md#ga4b73e6d51cff26ea5595df8680c00563)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes a DEBUG level hexdump message associated with the instance to the log. |
| #define | [LOG\_MODULE\_REGISTER](group__log__api.md#ga2404243df68fb6e51129d1c7ecc5ca45)(...) |
|  | Create module-specific state and register the module with Logger. |
| #define | [LOG\_MODULE\_DECLARE](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)(...) |
|  | Macro for declaring a log module (not registering it). |
| #define | [LOG\_LEVEL\_SET](group__log__api.md#gac396852328a77360a0c27dbf7b52356e)(level) |
|  | Macro for setting log level in the file or function where instance logging API is used. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log.h](log_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
