---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/emulator/bus_emulators.html
original_path: hardware/emulator/bus_emulators.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# External Bus and Bus Connected Peripherals Emulators

## Overview

Zephyr supports a simple emulator framework to support testing of external peripheral drivers
without requiring real hardware.

Emulators are used to emulate external hardware devices, to support testing of
various subsystems. For example, it is possible to write an emulator
for an I2C compass such that it appears on the I2C bus and can be used
just like a real hardware device.

Emulators often implement special features for testing. For example a
compass may support returning bogus data if the I2C bus speed is too
high, or may return invalid measurements if calibration has not yet
been completed. This allows for testing that high-level code can
handle these situations correctly. Test coverage can therefore
approach 100% if all failure conditions are emulated.

## Concept

The diagram below shows application code / high-level tests at the top.
This is the ultimate application we want to run.

![Emulator architecture showing tests, emulators and drivers](../../_images/arch.svg)

Below that are peripheral drivers, such as the AT24 EEPROM driver. We can test
peripheral drivers using an emulation driver connected via a emulated I2C
controller/emulator which passes I2C traffic from the AT24 driver to the AT24
simulator.

Separately we can test the STM32 and NXP I2C drivers on real hardware using API
tests. These require some sort of device attached to the bus, but with this, we
can validate much of the driver functionality.

Putting the two together, we can test the application and peripheral code
entirely on native\_sim. Since we know that the I2C driver on the real hardware
works, we should expect the application and peripheral drivers to work on the
real hardware also.

Using the above framework we can test an entire application (e.g. Embedded
Controller) on native\_sim using emulators for all non-chip drivers.

With this approach we can:

- Write individual tests for each driver (green), covering all failure modes,
  error conditions, etc.
- Ensure 100% test coverage for drivers (green)
- Write tests for combinations of drivers, such as GPIOs provided by an I2C GPIO
  expander driver talking over an I2C bus, with the GPIOs controlling a charger.
  All of this can work in the emulated environment or on real hardware.
- Write a complex application that ties together all of these pieces and runs on
  native\_sim. We can develop on a host, use source-level debugging, etc.
- Transfer the application to any board which provides the required features
  (e.g. I2C, enough GPIOs), by adding Kconfig and devicetree fragments.

## Creating a Device Driver Emulator

The emulator subsystem is modeled on the [Device Driver Model](../../kernel/drivers/index.md#device-model-api). You create
an emulator instance using one of the [`EMUL_DT_DEFINE()`](#c.EMUL_DT_DEFINE) or
[`EMUL_DT_INST_DEFINE()`](#c.EMUL_DT_INST_DEFINE) APIs.

Emulators for peripheral devices reuse the same devicetree node as the real
device driver. This means that your emulator defines DT\_DRV\_COMPAT using the
same `compat` value from the real driver.

```c
/* From drivers/sensor/bm160/bm160.c */
#define DT_DRV_COMPAT bosch_bmi160

/* From drivers/sensor/bmi160/emul_bmi160.c */
#define DT_DRV_COMPAT bosch_bmi160
```

The `EMUL_DT_DEFINE()` function accepts two API types:

> 1. `bus_api` - This points to the API for the upstream bus that the emulator
>    connects to. The `bus_api` parameter is required. The supported
>    emulated bus types include I2C, SPI, eSPI, and MSPI.
> 2. `_backend_api` - This points to the device-class specific backend API for
>    the emulator. The `_backend_api` parameter is optional.

The diagram below demonstrates the logical organization of the `bus_api` and
`_backend_api` using the BC1.2 charging detector driver as the model
device-class.

![Device class example, demonstrating BC1.2 charging detectors.](../../_images/device_class_emulator.svg)

The real code is shown in green, while the emulator code is shown in yellow.

The `bus_api` connects the BC1.2 emulators to the `native_sim` I2C
controller. The real BC1.2 drivers are unchanged and operate exactly as if there
was a physical I2C controller present in the system. The `native_sim` I2C
controller uses the `bus_api` to initiate register reads and writes to the
emulator.

The `_backend_api` provides a mechanism for tests to manipulate the emulator
out of band. Each device class defines it’s own API functions. The backend API
functions focus on high-level behavior and do not provide hooks for specific
emulators.

In the case of the BC1.2 charging detector the backend API provides functions
to simulate connecting and disconnecting a charger to the emulated BC1.2 device.
Each emulator is responsible for updating the correct vendor specific registers
and potentially signalling an interrupt.

Example test flow:

> 1. Test registers BC1.2 detection callback using the Zephyr BC1.2 driver API.
> 2. Test connects a charger using the BC1.2 emulator backend.
> 3. Test verifies B1.2 detection callback invoked with correct charger type.
> 4. Test disconnects a charger using the BC1.2 emulator backend.

With this architecture, the same test can be used will all supported drivers in
the same driver class.

## Available Emulators

Zephyr includes the following emulators:

- I2C emulator driver, allowing drivers to be connected to an emulator so that
  tests can be performed without access to the real hardware
- SPI emulator driver, which does the same for SPI
- eSPI emulator driver, which does the same for eSPI. The emulator is being
  developed to support more functionalities.
- MSPI emulator driver, allowing drivers to be connected to an emulator so that
  tests can be performed without access to the real hardware.

## Samples

Here are some examples present in Zephyr:

1. Bosch BMI160 sensor driver connected via both I2C and SPI to an emulator:

   ```shell
   west build -b native_sim tests/drivers/sensor/accel/
   ```
2. The same test can be built with a second EEPROM which is an Atmel AT24 EEPROM driver
   connected via I2C an emulator:

   ```shell
   west build -b native_sim tests/drivers/eeprom/api -- -DDTC_OVERLAY_FILE=at2x_emul.overlay -DOVERLAY_CONFIG=at2x_emul.conf
   ```

### API Reference

*group* Emulator interface
:   Emulators used to test drivers and higher-level code that uses them.

    Defines

    EMUL\_DT\_NAME\_GET(node\_id)
    :   Use the devicetree node identifier as a unique name.

        Parameters:
        :   - **node\_id** – A devicetree node identifier

    EMUL\_DT\_DEFINE(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api)
    :   Define a new emulator.

        This adds a new struct emul to the linker list of emulations. This is typically used in your emulator’s [DT\_INST\_FOREACH\_STATUS\_OKAY()](../../build/dts/api/api.md#group__devicetree-inst_1gaeac7ed0f4a6820a6e5d7dadb6d62d6e7) clause.

        Parameters:
        :   - **node\_id** – Node ID of the driver to emulate (e.g. [DT\_DRV\_INST(n)](../../build/dts/api/api.md#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1)); the node\_id *MUST* have a corresponding [DEVICE\_DT\_DEFINE()](../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1).
            - **init\_fn** – function to call to initialise the emulator (see emul\_init typedef)
            - **data\_ptr** – emulator-specific data
            - **cfg\_ptr** – emulator-specific configuration data
            - **bus\_api** – emulator-specific bus api
            - **\_backend\_api** – emulator-specific backend api

    EMUL\_DT\_INST\_DEFINE(inst, ...)
    :   Like [EMUL\_DT\_DEFINE()](#group__io__emulators_1gad6292e3cd7f17a3600be396777f304c8), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier.

        Parameters:
        :   - **inst** – instance number. The `node_id` argument to EMUL\_DT\_DEFINE is set to `[DT_DRV_INST(inst)](../../build/dts/api/api.md#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1)`.
            - **...** – other parameters as expected by EMUL\_DT\_DEFINE.

    EMUL\_DT\_GET(node\_id)
    :   Get a `const struct emul*` from a devicetree node identifier.

        Returns a pointer to an emulator object created from a devicetree node, if any device was allocated by an emulator implementation.

        If no such device was allocated, this will fail at linker time. If you get an error that looks like `undefined reference to __device_dts_ord_<N>`, that is what happened. Check to make sure your emulator implementation is being compiled, usually by enabling the Kconfig options it requires.

        Parameters:
        :   - **node\_id** – A devicetree node identifier

        Returns:
        :   A pointer to the emul object created for that node

    EMUL\_DT\_GET\_OR\_NULL(node\_id)
    :   Utility macro to obtain an optional reference to an emulator.

        If the node identifier refers to a node with status `okay`, this returns `[EMUL_DT_GET(node_id)](#group__io__emulators_1ga300d997df388118ae380e79b972f85cf)`. Otherwise, it returns `NULL`.

        Parameters:
        :   - **node\_id** – A devicetree node identifier

        Returns:
        :   a [emul](#structemul) reference for the node identifier, which may be `NULL`.

    Typedefs

    typedef int (\*emul\_init\_t)(const struct [emul](#c.emul) \*emul, const struct [device](../../kernel/drivers/index.md#c.device "device") \*parent)
    :   Standard callback for emulator initialisation providing the initialiser record and the device that calls the emulator functions.

        Param emul:
        :   Emulator to init

        Param parent:
        :   Parent device that is using the emulator

    Enums

    enum emul\_bus\_type
    :   The types of supported buses.

        *Values:*

        enumerator EMUL\_BUS\_TYPE\_I2C

        enumerator EMUL\_BUS\_TYPE\_ESPI

        enumerator EMUL\_BUS\_TYPE\_SPI

        enumerator EMUL\_BUS\_TYPE\_MSPI

        enumerator EMUL\_BUS\_TYPE\_NONE

    Functions

    int emul\_init\_for\_bus(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Set up a list of emulators.

        Parameters:
        :   - **dev** – Device the emulators are attached to (e.g. an I2C controller)

        Returns:
        :   0 if OK

        Returns:
        :   negative value on error

    const struct [emul](#c.emul) \*emul\_get\_binding(const char \*name)
    :   Retrieve the emul structure for an emulator by name.

        Emulator objects are created via the [EMUL\_DT\_DEFINE()](#group__io__emulators_1gad6292e3cd7f17a3600be396777f304c8) macro and placed in memory by the linker. If the emulator structure is needed for custom API calls, it can be retrieved by the name that the emulator exposes to the system (this is the devicetree node’s label by default).

        Parameters:
        :   - **name** – Emulator name to search for. A null pointer, or a pointer to an empty string, will cause NULL to be returned.

        Returns:
        :   pointer to emulator structure; NULL if not found or cannot be used.

    struct emul\_link\_for\_bus
    :   *#include <emul.h>*

        Structure uniquely identifying a device to be emulated.

    struct emul\_list\_for\_bus
    :   *#include <emul.h>*

        List of emulators attached to a bus.

        Public Members

        const struct [emul\_link\_for\_bus](#c.emul_link_for_bus) \*children
        :   Identifiers for children of the node.

        unsigned int num\_children
        :   Number of children of the node.

    struct no\_bus\_emul
    :   *#include <emul.h>*

        Emulator API stub when an emulator is not actually placed on a bus.

    struct emul
    :   *#include <emul.h>*

        An emulator instance - represents the *target* emulated device/peripheral that is interacted with through an emulated bus.

        Instances of emulated bus nodes (e.g. i2c\_emul) and emulators (i.e. struct emul) are exactly 1..1

        Public Members

        [emul\_init\_t](#c.emul_init_t) init
        :   function used to initialise the emulator state

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   handle to the device for which this provides low-level emulation

        const void \*cfg
        :   Emulator-specific configuration data.

        void \*data
        :   Emulator-specific data.

        enum [emul\_bus\_type](#c.emul_bus_type) bus\_type
        :   The bus type that the emulator is attached to.

        const void \*backend\_api
        :   Address of the API structure exposed by the emulator instance.

        union bus
        :   *#include <emul.h>*

            Pointer to the emulated bus node.

            Public Members

            struct i2c\_emul \*i2c

            struct espi\_emul \*espi

            struct spi\_emul \*spi

            struct mspi\_emul \*mspi

            struct [no\_bus\_emul](#c.no_bus_emul) \*none
