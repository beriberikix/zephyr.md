---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/conn__mgr__monitor_8h.html
original_path: doxygen/html/conn__mgr__monitor_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_monitor.h File Reference

[Go to the source code of this file.](conn__mgr__monitor_8h_source.md)

| Functions | |
| --- | --- |
| void | [conn\_mgr\_mon\_resend\_status](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277) (void) |
|  | Resend either NET\_L4\_CONNECTED or NET\_L4\_DISCONNECTED depending on whether connectivity is currently available. |
| void | [conn\_mgr\_ignore\_iface](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark an iface to be ignored by conn\_mgr. |
| void | [conn\_mgr\_watch\_iface](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979) (struct [net\_if](structnet__if.md) \*iface) |
|  | Watch (stop ignoring) an iface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_is\_iface\_ignored](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check whether the provided iface is currently ignored. |
| void | [conn\_mgr\_ignore\_l2](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Mark an L2 to be ignored by conn\_mgr. |
| void | [conn\_mgr\_watch\_l2](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Watch (stop ignoring) an L2. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_monitor.h](conn__mgr__monitor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
