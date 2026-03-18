---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/bbram.html
original_path: hardware/peripherals/bbram.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Battery Backed RAM (BBRAM)

The BBRAM APIs allow interfacing with the unique properties of this memory region. The following
common types of BBRAM properties are easily accessed via this API:

- IBBR (invalid) state - check that the BBRAM is not corrupt.
- VSBY (voltage standby) state - check if the BBRAM is using standby voltage.
- VCC (active power) state - check if the BBRAM is on normal power.
- Size - get the size (in bytes) of the BBRAM region.

Along with these, the API provides a means for reading and writing to the memory region via
[`bbram_read()`](#c.bbram_read) and [`bbram_write()`](#c.bbram_write) respectively. Both functions are expected to only
succeed if the BBRAM is in a valid state and the operation is bounded to the memory region.

## API Reference

*group* bbram\_interface
:   BBRAM Interface.

    Typedefs

    typedef int (\*bbram\_api\_check\_invalid\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   API template to check if the BBRAM is invalid.

        See also

        [bbram\_check\_invalid](#group__bbram__interface_1ga7164969f308616696a9ab71a4d19b70b)

    typedef int (\*bbram\_api\_check\_standby\_power\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   API template to check for standby power failure.

        See also

        [bbram\_check\_standby\_power](#group__bbram__interface_1ga948ed0a7d3824f950ad46b99ba3d86f4)

    typedef int (\*bbram\_api\_check\_power\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   API template to check for V CC1 power failure.

        See also

        [bbram\_check\_power](#group__bbram__interface_1ga8fc2a647bda90e96f866514300180a96)

    typedef int (\*bbram\_api\_get\_size\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t \*size)
    :   API template to check the size of the BBRAM.

        See also

        [bbram\_get\_size](#group__bbram__interface_1gab6bdb4a1cba88ca645c256366a696bdd)

    typedef int (\*bbram\_api\_read\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t offset, size\_t size, uint8\_t \*data)
    :   API template to read from BBRAM.

        See also

        [bbram\_read](#group__bbram__interface_1ga9ef786b0fbac3f8523be2bb87b7cff7b)

    typedef int (\*bbram\_api\_write\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t offset, size\_t size, const uint8\_t \*data)
    :   API template to write to BBRAM.

        See also

        [bbram\_write](#group__bbram__interface_1ga51007eed4820aed341d20e4562607564)

    Functions

    int bbram\_check\_invalid(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if BBRAM is invalid.

        Check if “Invalid Battery-Backed RAM” status is set then reset the status bit. This may occur as a result to low voltage at the VBAT pin.

        Parameters:
        :   - **dev** – **[in]** BBRAM device pointer.

        Returns:
        :   0 if the Battery-Backed RAM data is valid, -EFAULT otherwise.

    int bbram\_check\_standby\_power(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check for standby (Volt SBY) power failure.

        Check if the V standby power domain is turned on after it was off then reset the status bit.

        Parameters:
        :   - **dev** – **[in]** BBRAM device pointer.

        Returns:
        :   0 if V SBY power domain is in normal operation.

    int bbram\_check\_power(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check for V CC1 power failure.

        This will return an error if the V CC1 power domain is turned on after it was off and reset the status bit.

        Parameters:
        :   - **dev** – **[in]** BBRAM device pointer.

        Returns:
        :   0 if the V CC1 power domain is in normal operation, -EFAULT otherwise.

    int bbram\_get\_size(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t \*size)
    :   Get the size of the BBRAM (in bytes).

        Parameters:
        :   - **dev** – **[in]** BBRAM device pointer.
            - **size** – **[out]** Pointer to write the size to.

        Returns:
        :   0 for success, -EFAULT otherwise.

    int bbram\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t offset, size\_t size, uint8\_t \*data)
    :   Read bytes from BBRAM.

        Parameters:
        :   - **dev** – **[in]** The BBRAM device pointer to read from.
            - **offset** – **[in]** The offset into the RAM address to start reading from.
            - **size** – **[in]** The number of bytes to read.
            - **data** – **[out]** The buffer to load the data into.

        Returns:
        :   0 on success, -EFAULT if the address range is out of bounds.

    int bbram\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, size\_t offset, size\_t size, const uint8\_t \*data)
    :   Write bytes to BBRAM.

        Parameters:
        :   - **dev** – **[in]** The BBRAM device pointer to write to.
            - **offset** – **[in]** The offset into the RAM address to start writing to.
            - **size** – **[in]** The number of bytes to write.
            - **data** – **[out]** Pointer to the start of data to write.

        Returns:
        :   0 on success, -EFAULT if the address range is out of bounds.

    int bbram\_emul\_set\_invalid(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool is\_invalid)
    :   Set the emulated BBRAM driver’s invalid state.

        Calling this will affect the emulated behavior of [bbram\_check\_invalid()](#group__bbram__interface_1ga7164969f308616696a9ab71a4d19b70b).

        Parameters:
        :   - **dev** – **[in]** The emulated device to modify
            - **is\_invalid** – **[in]** The new invalid state

        Returns:
        :   0 on success, negative values on error.

    int bbram\_emul\_set\_standby\_power\_state(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool failure)
    :   Set the emulated BBRAM driver’s standby power state.

        Calling this will affect the emulated behavior of [bbram\_check\_standby\_power()](#group__bbram__interface_1ga948ed0a7d3824f950ad46b99ba3d86f4).

        Parameters:
        :   - **dev** – **[in]** The emulated device to modify
            - **failure** – **[in]** Whether or not standby power failure should be emulated

        Returns:
        :   0 on success, negative values on error.

    int bbram\_emul\_set\_power\_state(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool failure)
    :   Set the emulated BBRAM driver’s power state.

        Calling this will affect the emulated behavior of [bbram\_check\_power()](#group__bbram__interface_1ga8fc2a647bda90e96f866514300180a96).

        Parameters:
        :   - **dev** – **[in]** The emulated device to modify
            - **failure** – **[in]** Whether or not a power failure should be emulated

        Returns:
        :   0 on success, negative values on error.

    struct bbram\_driver\_api
    :   *#include <bbram.h>*
