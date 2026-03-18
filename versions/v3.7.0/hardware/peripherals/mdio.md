---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/mdio.html
original_path: hardware/peripherals/mdio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Management Data Input/Output (MDIO)

## Overview

MDIO is a bus that is commonly used to communicate with ethernet PHY devices.
Many ethernet MAC controllers also provide hardware to communicate over MDIO
bus with a peripheral device.

This API is intended to be used primarily by PHY drivers but can also be
used by user firmware.

## API Reference

*group* MDIO Interface
:   MDIO Interface.

    Functions

    void mdio\_bus\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable MDIO bus.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller

    void mdio\_bus\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable MDIO bus and tri-state drivers.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller

    int mdio\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t \*data)
    :   Read from MDIO Bus.

        This routine provides a generic interface to perform a read on the MDIO bus.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller
            - **prtad** – **[in]** Port address
            - **regad** – **[in]** Register address
            - **data** – Pointer to receive read data

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ETIMEDOUT** – If transaction timedout on the bus
            - **-ENOSYS** – if read is not supported

    int mdio\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t data)
    :   Write to MDIO bus.

        This routine provides a generic interface to perform a write on the MDIO bus.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller
            - **prtad** – **[in]** Port address
            - **regad** – **[in]** Register address
            - **data** – **[in]** Data to write

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ETIMEDOUT** – If transaction timedout on the bus
            - **-ENOSYS** – if write is not supported

    int mdio\_read\_c45(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t \*data)
    :   Read from MDIO Bus using Clause 45 access.

        This routine provides an interface to perform a read on the MDIO bus using IEEE 802.3 Clause 45 access.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller
            - **prtad** – **[in]** Port address
            - **devad** – **[in]** Device address
            - **regad** – **[in]** Register address
            - **data** – Pointer to receive read data

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ETIMEDOUT** – If transaction timedout on the bus
            - **-ENOSYS** – if write using Clause 45 access is not supported

    int mdio\_write\_c45(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t data)
    :   Write to MDIO bus using Clause 45 access.

        This routine provides an interface to perform a write on the MDIO bus using IEEE 802.3 Clause 45 access.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the controller
            - **prtad** – **[in]** Port address
            - **devad** – **[in]** Device address
            - **regad** – **[in]** Register address
            - **data** – **[in]** Data to write

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ETIMEDOUT** – If transaction timedout on the bus
            - **-ENOSYS** – if write using Clause 45 access is not supported
