---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hdr__ddr_8h.html
original_path: doxygen/html/hdr__ddr_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hdr\_ddr.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/i3c.h](i3c_8h_source.md)>`

[Go to the source code of this file.](hdr__ddr_8h_source.md)

| Functions | |
| --- | --- |
| static int | [i3c\_hdr\_ddr\_write](group__i3c__hdr__ddr.md#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I3C target device with HDR DDR. |
| static int | [i3c\_hdr\_ddr\_read](group__i3c__hdr__ddr.md#ga11e788383aeb52184fdd6483cf702d40) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I3C target device with HDR DDR. |
| static int | [i3c\_hdr\_ddr\_write\_read](group__i3c__hdr__ddr.md#gaa752f1095c84ad1b94fb09cc0aeee4fa) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) read\_cmd, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_cmd) |
|  | Write then read data from an I3C target device with HDR DDR. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [hdr\_ddr.h](hdr__ddr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
