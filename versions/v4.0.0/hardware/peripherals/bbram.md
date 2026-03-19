---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/bbram.html
original_path: hardware/peripherals/bbram.html
---

# Battery Backed RAM (BBRAM)

The BBRAM APIs allow interfacing with the unique properties of this memory region. The following
common types of BBRAM properties are easily accessed via this API:

- IBBR (invalid) state - check that the BBRAM is not corrupt.
- VSBY (voltage standby) state - check if the BBRAM is using standby voltage.
- VCC (active power) state - check if the BBRAM is on normal power.
- Size - get the size (in bytes) of the BBRAM region.

Along with these, the API provides a means for reading and writing to the memory region via
[`bbram_read()`](../../doxygen/html/group__bbram__interface.md#ga9ef786b0fbac3f8523be2bb87b7cff7b) and [`bbram_write()`](../../doxygen/html/group__bbram__interface.md#ga51007eed4820aed341d20e4562607564) respectively. Both functions are expected to only
succeed if the BBRAM is in a valid state and the operation is bounded to the memory region.

## API Reference

[BBRAM Interface](../../doxygen/html/group__bbram__interface.md)
