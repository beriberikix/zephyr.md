---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/flash.html
original_path: hardware/peripherals/flash.html
---

# Flash

## Overview

**Flash offset concept**

Offsets used by the user API are expressed in relation to
the flash memory beginning address. This rule shall be applied to
all flash controller regular memory that layout is accessible via
API for retrieving the layout of pages (see [`CONFIG_FLASH_PAGE_LAYOUT`](../../kconfig.md#CONFIG_FLASH_PAGE_LAYOUT "CONFIG_FLASH_PAGE_LAYOUT")).

An exception from the rule may be applied to a vendor-specific flash
dedicated-purpose region (such a region obviously can’t be covered under
API for retrieving the layout of pages).

## User API Reference

[FLASH Interface](../../doxygen/html/group__flash__interface.md)

Related code samples

- [AT45 DataFlash driver](../../samples/drivers/spi_flash_at45/README.md#spi-flash-at45 "Use the AT45 family DataFlash driver to interact with the flash memory over SPI.")Use the AT45 family DataFlash driver to interact with the flash memory over SPI.
- [Flash shell](../../samples/drivers/flash_shell/README.md#flash-shell "Explore a flash device using shell commands.")Explore a flash device using shell commands.
- [JEDEC MSPI-NOR flash](../../samples/drivers/mspi/mspi_flash/README.md#mspi-flash "Use the flash API to interact with a MSPI NOR serial flash memory device.")Use the flash API to interact with a MSPI NOR serial flash memory device.
- [JEDEC SPI-NOR flash](../../samples/drivers/spi_flash/README.md#spi-nor "Use the flash API to interact with an SPI NOR serial flash memory device.")Use the flash API to interact with an SPI NOR serial flash memory device.
- [JESD216 flash](../../samples/drivers/jesd216/README.md#jesd216 "Use the JESD216 flash API to extract information from a compatible serial memory device.")Use the JESD216 flash API to extract information from a compatible serial memory device.
- [Memory-Mapped Flash](../../samples/boards/espressif/flash_memory_mapped/README.md#esp32-flash-memory-mapped "Write data into scratch area and read it using flash API and memory-mapped pointer.")Write data into scratch area and read it using flash API and memory-mapped pointer.
- [nRF SoC Internal Storage](../../samples/drivers/soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")Use the flash API to interact with the SoC flash.

## Implementation interface API Reference

[FLASH internal Interface](../../doxygen/html/group__flash__internal__interface.md)
