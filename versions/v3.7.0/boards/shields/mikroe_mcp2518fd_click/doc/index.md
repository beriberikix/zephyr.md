---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/mikroe_mcp2518fd_click/doc/index.html
original_path: boards/shields/mikroe_mcp2518fd_click/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MikroElektronika MCP2518FD Click shield

## Overview

MCP2518FD Click shield has a MCP2518FD CAN FD controller via a SPI
interface and a high-speed ATA6563 CAN transceiver.

More information about the shield can be found at
[Mikroe MCP2518FD click](https://www.mikroe.com/mcp2518fd-click) [[1]](#id1).

### Requirements

The shield uses a mikroBUS interface. The target board must define
a mikrobus\_spi and mikrobus\_header node labels
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details). The target board must also
support level triggered interrupts.

### Programming

Set `--shield mikroe_mcp2518fd_click` when you invoke `west build`,
for example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s28 --shield mikroe_mcp2518fd_click samples/drivers/can/counter
west flash
```

### References

[[1](#id2)]

[https://www.mikroe.com/mcp2518fd-click](https://www.mikroe.com/mcp2518fd-click)
