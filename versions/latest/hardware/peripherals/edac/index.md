---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/edac/index.html
original_path: hardware/peripherals/edac/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Error Detection And Correction (EDAC)

Error Detection And Correction is a mechanism used to detect and correct errors
while storing or reading data.

## Configuration option

Related configuration option:

- [`CONFIG_EDAC`](../../../kconfig.md#CONFIG_EDAC "CONFIG_EDAC")

## API Reference

Related code samples

[EDAC shell](../../../samples/subsys/edac/README.md#edac "Test error detection and correction (EDAC) using shell commands.")
:   Test error detection and correction (EDAC) using shell commands.

*group* edac
:   Optional interfaces

    EDAC Optional Interfaces

    static inline int edac\_inject\_set\_param1(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t value)
    :   Set injection parameter param1.

        Set first error injection parameter value.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – First injection parameter

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, other error code otherwise

    static inline int edac\_inject\_get\_param1(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*value)
    :   Get injection parameter param1.

        Get first error injection parameter value.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – Pointer to the first injection parameter

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    static inline int edac\_inject\_set\_param2(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t value)
    :   Set injection parameter param2.

        Set second error injection parameter value.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – Second injection parameter

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    static inline int edac\_inject\_get\_param2(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*value)
    :   Get injection parameter param2.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – Pointer to the second injection parameter

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    static inline int edac\_inject\_set\_error\_type(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t error\_type)
    :   Set error type value.

        Set the value of error type to be injected

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **error\_type** – Error type value

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    static inline int edac\_inject\_get\_error\_type(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*error\_type)
    :   Get error type value.

        Get the value of error type to be injected

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **error\_type** – Pointer to error type value

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    static inline int edac\_inject\_error\_trigger(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Set injection control.

        Trigger error injection.

        Parameters:
        :   - **dev** – Pointer to the device structure

        Return values:
        :   - **-ENOSYS** – if the optional interface is not implemented
            - **0** – on success, error code otherwise

    Mandatory interfaces

    EDAC Mandatory Interfaces

    static inline int edac\_ecc\_error\_log\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*value)
    :   Get ECC Error Log.

        Read value of ECC Error Log.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – Pointer to the ECC Error Log value

        Return values:
        :   - **0** – on success, error code otherwise
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_ecc\_error\_log\_clear(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear ECC Error Log.

        Clear value of ECC Error Log.

        Parameters:
        :   - **dev** – Pointer to the device structure

        Return values:
        :   - **0** – on success, error code otherwise
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_parity\_error\_log\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*value)
    :   Get Parity Error Log.

        Read value of Parity Error Log.

        Parameters:
        :   - **dev** – Pointer to the device structure
            - **value** – Pointer to the parity Error Log value

        Return values:
        :   - **0** – on success, error code otherwise
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_parity\_error\_log\_clear(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear Parity Error Log.

        Clear value of Parity Error Log.

        Parameters:
        :   - **dev** – Pointer to the device structure

        Return values:
        :   - **0** – on success, error code otherwise
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_errors\_cor\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get number of correctable errors.

        Parameters:
        :   - **dev** – Pointer to the device structure

        Return values:
        :   - **num** – Number of correctable errors
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_errors\_uc\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get number of uncorrectable errors.

        Parameters:
        :   - **dev** – Pointer to the device structure

        Return values:
        :   - **num** – Number of uncorrectable errors
            - **-ENOSYS** – if the mandatory interface is not implemented

    static inline int edac\_notify\_callback\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, edac\_notify\_callback\_f cb)
    :   Register callback function for memory error exception.

        This callback runs in interrupt context

        Parameters:
        :   - **dev** – EDAC driver device to install callback
            - **cb** – Callback function pointer

        Return values:
        :   - **0** – on success, error code otherwise
            - **-ENOSYS** – if the mandatory interface is not implemented

    Enums

    enum edac\_error\_type
    :   EDAC error type.

        *Values:*

        enumerator EDAC\_ERROR\_TYPE\_DRAM\_COR = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Correctable error type.

        enumerator EDAC\_ERROR\_TYPE\_DRAM\_UC = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Uncorrectable error type.
