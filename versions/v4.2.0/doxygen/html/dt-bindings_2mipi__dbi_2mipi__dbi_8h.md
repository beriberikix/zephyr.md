---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html
original_path: doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi.h File Reference

[Go to the source code of this file.](dt-bindings_2mipi__dbi_2mipi__dbi_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MIPI\_DBI\_MODE\_SPI\_3WIRE](group__mipi__dbi__interface.md#ga9aeeeef78898e1d649f96feccae2fcac)   0x1 |
|  | SPI 3 wire (Type C1). |
| #define | [MIPI\_DBI\_MODE\_SPI\_4WIRE](group__mipi__dbi__interface.md#ga5c27ef3aa3256e60495a7c511cbaf7a5)   0x2 |
|  | SPI 4 wire (Type C3). |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_16\_BIT](group__mipi__dbi__interface.md#ga4e59f3d57007cea38ae04aac74c2b5dc)   0x3 |
|  | Parallel Bus protocol for MIPI DBI Type A based on Motorola 6800 bus. |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_9\_BIT](group__mipi__dbi__interface.md#gaa89b584bc5bf5a153926ba808de49131)   0x4 |
| #define | [MIPI\_DBI\_MODE\_6800\_BUS\_8\_BIT](group__mipi__dbi__interface.md#gab9b80bb367e7bd084ae490bbff9034b9)   0x5 |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_16\_BIT](group__mipi__dbi__interface.md#ga3c3d1c379c4bc07847412b3bd5b76cb1)   0x6 |
|  | Parallel Bus protocol for MIPI DBI Type B based on Intel 8080 bus. |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_9\_BIT](group__mipi__dbi__interface.md#gad4c61d48021f38c0759daf9a401f24c7)   0x7 |
| #define | [MIPI\_DBI\_MODE\_8080\_BUS\_8\_BIT](group__mipi__dbi__interface.md#ga3d26bb4556822d12567c62c7ff2c3bb9)   0x8 |
| #define | [MIPI\_DBI\_MODE\_RGB332](group__mipi__dbi__interface.md#ga11d68e3a9a449ec8fce4bbae637af08c)   (0x1 << 4U) |
|  | Color coding for MIPI DBI Type A or Type B interface. |
| #define | [MIPI\_DBI\_MODE\_RGB444](group__mipi__dbi__interface.md#gac18f3926b86551908300f055ebe9212a)   (0x2 << 4U) |
|  | For 8-bit data bus width, 2 pixels are sent in 3 cycles. |
| #define | [MIPI\_DBI\_MODE\_RGB565](group__mipi__dbi__interface.md#ga53bbca5860b8845e892d3605c44877b4)   (0x3 << 4U) |
|  | For 8-bit data bus width, 1 pixel is sent in 2 cycles. |
| #define | [MIPI\_DBI\_MODE\_RGB666\_1](group__mipi__dbi__interface.md#gaa264bb127fbbece867bf444c8168b6f4)   (0x4 << 4U) |
|  | For 8-bit data bus width, MIPI\_DBI\_MODE\_RGB666\_1 and MIPI\_DBI\_MODE\_RGB666\_2 are the same. |
| #define | [MIPI\_DBI\_MODE\_RGB666\_2](group__mipi__dbi__interface.md#gafb1d7ae963a9cfedadaa4c4299ad7f99)   (0x5 << 4U) |
| #define | [MIPI\_DBI\_MODE\_RGB888\_1](group__mipi__dbi__interface.md#gad7195e4b6aad08002b4b61a3052bf8e7)   (0x6 << 4U) |
|  | For 8-bit data bus width, MIPI\_DBI\_MODE\_RGB666\_1 and MIPI\_DBI\_MODE\_RGB666\_2 are the same. |
| #define | [MIPI\_DBI\_MODE\_RGB888\_2](group__mipi__dbi__interface.md#ga0edb36a8b62a252bff686f0463bd83fc)   (0x7 << 4U) |
| #define | [MIPI\_DBI\_TE\_NO\_EDGE](group__mipi__dbi__interface.md#gad73dfe18498d59ed4bc2a9f15306d695)   0x0 |
|  | MIPI DBI tearing enable synchronization is disabled. |
| #define | [MIPI\_DBI\_TE\_RISING\_EDGE](group__mipi__dbi__interface.md#gaa83bb6eb37251b1a5b4cd8b60b076d17)   0x1 |
|  | MIPI DBI tearing enable synchronization on rising edge of TE signal. |
| #define | [MIPI\_DBI\_TE\_FALLING\_EDGE](group__mipi__dbi__interface.md#gad1ebe36d7048bca248d3a03b63e1e9c7)   0x2 |
|  | MIPI DBI tearing enable synchronization on falling edge of TE signal. |
| #define | [MIPI\_DBI\_SPI\_XFR\_8BIT](group__mipi__dbi__interface.md#ga900ba99dbfe81a0856a008809e9f1273)   8 |
|  | SPI transfer of DBI commands as 8-bit blocks, the default behaviour in SPI 4 wire (Type C3) mode. |
| #define | [MIPI\_DBI\_SPI\_XFR\_16BIT](group__mipi__dbi__interface.md#ga55bd42d5252cedb919cc0b0bd1d6cdf7)   16 |
|  | SPI transfer of DBI commands as 16-bit blocks, a rare and seldom behaviour in SPI 4 wire (Type C3) mode. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [mipi\_dbi](dir_e611cdaf3e454b28b4ecdd29a4f655ae.md)
- [mipi\_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
