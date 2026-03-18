---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/drivers/index.html
original_path: kernel/drivers/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Device Driver Model

## Introduction

The Zephyr kernel supports a variety of device drivers. Whether a
driver is available depends on the board and the driver.

The Zephyr device model provides a consistent device model for configuring the
drivers that are part of a system. The device model is responsible
for initializing all the drivers configured into the system.

Each type of driver (e.g. UART, SPI, I2C) is supported by a generic type API.

In this model the driver fills in the pointer to the structure containing the
function pointers to its API functions during driver initialization. These
structures are placed into the RAM section in initialization level order.

[![Device Driver Model](../../_images/device_driver_model.svg)](../../_images/device_driver_model.svg)

## Standard Drivers

Device drivers which are present on all supported board configurations
are listed below.

- **Interrupt controller**: This device driver is used by the kernel’s
  interrupt management subsystem.
- **Timer**: This device driver is used by the kernel’s system clock and
  hardware clock subsystem.
- **Serial communication**: This device driver is used by the kernel’s
  system console subsystem.
- **Entropy**: This device driver provides a source of entropy numbers
  for the random number generator subsystem.

  Important

  Use the [random API functions](../../services/crypto/random/index.md#random-api) for random
  values. [Entropy functions](../../hardware/peripherals/entropy.md#entropy-api) should not be
  directly used as a random number generator source as some hardware
  implementations are designed to be an entropy seed source for random
  number generators and will not provide cryptographically secure
  random number streams.

## Synchronous Calls

Zephyr provides a set of device drivers for multiple boards. Each driver
should support an interrupt-based implementation, rather than polling, unless
the specific hardware does not provide any interrupt.

High-level calls accessed through device-specific APIs, such as
`i2c.h` or `spi.h`, are usually intended as synchronous. Thus,
these calls should be blocking.

## Driver APIs

The following APIs for device drivers are provided by `device.h`. The APIs
are intended for use in device drivers only and should not be used in
applications.

[`DEVICE_DEFINE()`](#c.DEVICE_DEFINE)
:   Create device object and related data structures including setting it
    up for boot-time initialization.

[`DEVICE_NAME_GET()`](#c.DEVICE_NAME_GET)
:   Converts a device identifier to the global identifier for a device
    object.

[`DEVICE_GET()`](#c.DEVICE_GET)
:   Obtain a pointer to a device object by name.

[`DEVICE_DECLARE()`](#c.DEVICE_DECLARE)
:   Declare a device object. Use this when you need a forward reference
    to a device that has not yet been defined.

## Driver Data Structures

The device initialization macros populate some data structures at build time
which are
split into read-only and runtime-mutable parts. At a high level we have:

```c
struct device {
      const char *name;
      const void *config;
      const void *api;
      void * const data;
};
```

The `config` member is for read-only configuration data set at build time. For
example, base memory mapped IO addresses, IRQ line numbers, or other fixed
physical characteristics of the device. This is the `config` pointer
passed to `DEVICE_DEFINE()` and related macros.

The `data` struct is kept in RAM, and is used by the driver for
per-instance runtime housekeeping. For example, it may contain reference counts,
semaphores, scratch buffers, etc.

The `api` struct maps generic subsystem APIs to the device-specific
implementations in the driver. It is typically read-only and populated at
build time. The next section describes this in more detail.

## Subsystems and API Structures

Most drivers will be implementing a device-independent subsystem API.
Applications can simply program to that generic API, and application
code is not specific to any particular driver implementation.

A subsystem API definition typically looks like this:

```c
typedef int (*subsystem_do_this_t)(const struct device *dev, int foo, int bar);
typedef void (*subsystem_do_that_t)(const struct device *dev, void *baz);

struct subsystem_api {
      subsystem_do_this_t do_this;
      subsystem_do_that_t do_that;
};

static inline int subsystem_do_this(const struct device *dev, int foo, int bar)
{
      struct subsystem_api *api;

      api = (struct subsystem_api *)dev->api;
      return api->do_this(dev, foo, bar);
}

static inline void subsystem_do_that(const struct device *dev, void *baz)
{
      struct subsystem_api *api;

      api = (struct subsystem_api *)dev->api;
      api->do_that(dev, baz);
}
```

A driver implementing a particular subsystem will define the real implementation
of these APIs, and populate an instance of subsystem\_api structure:

```c
static int my_driver_do_this(const struct device *dev, int foo, int bar)
{
      ...
}

static void my_driver_do_that(const struct device *dev, void *baz)
{
      ...
}

static struct subsystem_api my_driver_api_funcs = {
      .do_this = my_driver_do_this,
      .do_that = my_driver_do_that
};
```

The driver would then pass `my_driver_api_funcs` as the `api` argument to
`DEVICE_DEFINE()`.

Note

Since pointers to the API functions are referenced in the `api`
struct, they will always be included in the binary even if unused;
`gc-sections` linker option will always see at least one reference to
them. Providing for link-time size optimizations with driver APIs in
most cases requires that the optional feature be controlled by a
Kconfig option.

## Device-Specific API Extensions

Some devices can be cast as an instance of a driver subsystem such as GPIO,
but provide additional functionality that cannot be exposed through the
standard API. These devices combine subsystem operations with
device-specific APIs, described in a device-specific header.

A device-specific API definition typically looks like this:

```c
#include <zephyr/drivers/subsystem.h>

/* When extensions need not be invoked from user mode threads */
int specific_do_that(const struct device *dev, int foo);

/* When extensions must be invokable from user mode threads */
__syscall int specific_from_user(const struct device *dev, int bar);

/* Only needed when extensions include syscalls */
#include <syscalls/specific.h>
```

A driver implementing extensions to the subsystem will define the real
implementation of both the subsystem API and the specific APIs:

```c
static int generic_do_this(const struct device *dev, void *arg)
{
   ...
}

static struct generic_api api {
   ...
   .do_this = generic_do_this,
   ...
};

/* supervisor-only API is globally visible */
int specific_do_that(const struct device *dev, int foo)
{
   ...
}

/* syscall API passes through a translation */
int z_impl_specific_from_user(const struct device *dev, int bar)
{
   ...
}

#ifdef CONFIG_USERSPACE

#include <zephyr/internal/syscall_handler.h>

int z_vrfy_specific_from_user(const struct device *dev, int bar)
{
    K_OOPS(K_SYSCALL_SPECIFIC_DRIVER(dev, K_OBJ_DRIVER_GENERIC, &api));
    return z_impl_specific_do_that(dev, bar)
}

#include <syscalls/specific_from_user_mrsh.c>

#endif /* CONFIG_USERSPACE */
```

Applications use the device through both the subsystem and specific
APIs.

Note

Public API for device-specific extensions should be prefixed with the
compatible for the device to which it applies. For example, if
adding special functions to support the Maxim DS3231 the identifier
fragment `specific` in the examples above would be `maxim_ds3231`.

## Single Driver, Multiple Instances

Some drivers may be instantiated multiple times in a given system. For example
there can be multiple GPIO banks, or multiple UARTS. Each instance of the driver
will have a different `config` struct and `data` struct.

Configuring interrupts for multiple drivers instances is a special case. If each
instance needs to configure a different interrupt line, this can be accomplished
through the use of per-instance configuration functions, since the parameters
to `IRQ_CONNECT()` need to be resolvable at build time.

For example, let’s say we need to configure two instances of `my_driver`, each
with a different interrupt line. In `drivers/subsystem/subsystem_my_driver.h`:

```c
typedef void (*my_driver_config_irq_t)(const struct device *dev);

struct my_driver_config {
      DEVICE_MMIO_ROM;
      my_driver_config_irq_t config_func;
};
```

In the implementation of the common init function:

```c
void my_driver_isr(const struct device *dev)
{
      /* Handle interrupt */
      ...
}

int my_driver_init(const struct device *dev)
{
      const struct my_driver_config *config = dev->config;

      DEVICE_MMIO_MAP(dev, K_MEM_CACHE_NONE);

      /* Do other initialization stuff */
      ...

      config->config_func(dev);

      return 0;
}
```

Then when the particular instance is declared:

```c
#if CONFIG_MY_DRIVER_0

DEVICE_DECLARE(my_driver_0);

static void my_driver_config_irq_0(const struct device *dev)
{
      IRQ_CONNECT(MY_DRIVER_0_IRQ, MY_DRIVER_0_PRI, my_driver_isr,
                  DEVICE_GET(my_driver_0), MY_DRIVER_0_FLAGS);
}

const static struct my_driver_config my_driver_config_0 = {
      DEVICE_MMIO_ROM_INIT(DT_DRV_INST(0)),
      .config_func = my_driver_config_irq_0
}

static struct my_data_0;

DEVICE_DEFINE(my_driver_0, MY_DRIVER_0_NAME, my_driver_init,
              NULL, &my_data_0, &my_driver_config_0,
              POST_KERNEL, MY_DRIVER_0_PRIORITY, &my_api_funcs);

#endif /* CONFIG_MY_DRIVER_0 */
```

Note the use of `DEVICE_DECLARE()` to avoid a circular dependency on providing
the IRQ handler argument and the definition of the device itself.

## Initialization Levels

Drivers may depend on other drivers being initialized first, or require
the use of kernel services. [`DEVICE_DEFINE()`](#c.DEVICE_DEFINE) and related APIs
allow the user to specify at what time during the boot sequence the init
function will be executed. Any driver will specify one of four
initialization levels:

`PRE_KERNEL_1`
:   Used for devices that have no dependencies, such as those that rely
    solely on hardware present in the processor/SOC. These devices cannot
    use any kernel services during configuration, since the kernel services are
    not yet available. The interrupt subsystem will be configured however
    so it’s OK to set up interrupts. Init functions at this level run on the
    interrupt stack.

`PRE_KERNEL_2`
:   Used for devices that rely on the initialization of devices initialized
    as part of the `PRE_KERNEL_1` level. These devices cannot use any kernel
    services during configuration, since the kernel services are not yet
    available. Init functions at this level run on the interrupt stack.

`POST_KERNEL`
:   Used for devices that require kernel services during configuration.
    Init functions at this level run in context of the kernel main task.

Within each initialization level you may specify a priority level, relative to
other devices in the same initialization level. The priority level is specified
as an integer value in the range 0 to 99; lower values indicate earlier
initialization. The priority level must be a decimal integer literal without
leading zeroes or sign (e.g. 32), or an equivalent symbolic name (e.g.
`\#define MY_INIT_PRIO 32`); symbolic expressions are *not* permitted (e.g.
`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT + 5`).

Drivers and other system utilities can determine whether startup is
still in pre-kernel states by using the [`k_is_pre_kernel()`](../services/interrupts.md#c.k_is_pre_kernel "k_is_pre_kernel")
function.

## System Drivers

In some cases you may just need to run a function at boot. For such cases, the
`SYS_INIT` can be used. This macro does not take any config or runtime
data structures and there isn’t a way to later get a device pointer by name. The
same device policies for initialization level and priority apply.

## Inspecting the initialization sequence

Device drivers declared with [`DEVICE_DEFINE`](#c.DEVICE_DEFINE) (or any variations of it)
and `SYS_INIT` are processed at boot time and the corresponding
initialization functions are called sequentially according to their specified
level and priority.

Sometimes it’s useful to inspect the final sequence of initialization function
call as produced by the linker. To do that, use the `initlevels` CMake
target, for example `west build -t initlevels`.

## Error handling

In general, it’s best to use `__ASSERT()` macros instead of
propagating return values unless the failure is expected to occur
during the normal course of operation (such as a storage device
full). Bad parameters, programming errors, consistency checks,
pathological/unrecoverable failures, etc., should be handled by
assertions.

When it is appropriate to return error conditions for the caller to
check, 0 should be returned on success and a POSIX `errno.h` code
returned on failure. See
[https://github.com/zephyrproject-rtos/zephyr/wiki/Naming-Conventions#return-codes](https://github.com/zephyrproject-rtos/zephyr/wiki/Naming-Conventions#return-codes)
for details about this.

## Memory Mapping

On some systems, the linear address of peripheral memory-mapped I/O (MMIO)
regions cannot be known at build time:

- The I/O ranges must be probed at runtime from the bus, such as with
  PCI express
- A memory management unit (MMU) is active, and the physical address of
  the MMIO range must be mapped into the page tables at some virtual
  memory location determined by the kernel.

These systems must maintain storage for the MMIO range within RAM and
establish the mapping within the driver’s init function. Other systems
do not care about this and can use MMIO physical addresses directly from
DTS and do not need any RAM-based storage for it.

For drivers that may need to deal with this situation, a set of
APIs under the DEVICE\_MMIO scope are defined, along with a mapping function
`device_map()`.

### Device Model Drivers with one MMIO region

The simplest case is for drivers which need to maintain one MMIO region.
These drivers will need to use the `DEVICE_MMIO_ROM` and
`DEVICE_MMIO_RAM` macros in the definitions for their `config_info`
and `driver_data` structures, with initialization of the `config_info`
from DTS using `DEVICE_MMIO_ROM_INIT`. A call to `DEVICE_MMIO_MAP()`
is made within the init function:

```c
struct my_driver_config {
   DEVICE_MMIO_ROM; /* Must be first */
   ...
}

struct my_driver_dev_data {
   DEVICE_MMIO_RAM; /* Must be first */
   ...
}

const static struct my_driver_config my_driver_config_0 = {
   DEVICE_MMIO_ROM_INIT(DT_DRV_INST(...)),
   ...
}

int my_driver_init(const struct device *dev)
{
   ...
   DEVICE_MMIO_MAP(dev, K_MEM_CACHE_NONE);
   ...
}

int my_driver_some_function(const struct device *dev)
{
   ...
   /* Write some data to the MMIO region */
   sys_write32(0xDEADBEEF, DEVICE_MMIO_GET(dev));
   ...
}
```

The particular expansion of these macros depends on configuration. On
a device with no MMU or PCI-e, `DEVICE_MMIO_MAP` and
`DEVICE_MMIO_RAM` expand to nothing.

### Device Model Drivers with multiple MMIO regions

Some drivers may have multiple MMIO regions. In addition, some drivers
may already be implementing a form of inheritance which requires some other
data to be placed first in the `config_info` and `driver_data`
structures.

This can be managed with the `DEVICE_MMIO_NAMED` variant macros. These
require that `DEV_CFG()` and `DEV_DATA()` macros be defined to obtain
a properly typed pointer to the driver’s config\_info or dev\_data structs.
For example:

```c
struct my_driver_config {
   ...
     DEVICE_MMIO_NAMED_ROM(corge);
     DEVICE_MMIO_NAMED_ROM(grault);
   ...
}

struct my_driver_dev_data {
        ...
     DEVICE_MMIO_NAMED_RAM(corge);
     DEVICE_MMIO_NAMED_RAM(grault);
     ...
}

#define DEV_CFG(_dev) \
   ((const struct my_driver_config *)((_dev)->config))

#define DEV_DATA(_dev) \
   ((struct my_driver_dev_data *)((_dev)->data))

const static struct my_driver_config my_driver_config_0 = {
   ...
   DEVICE_MMIO_NAMED_ROM_INIT(corge, DT_DRV_INST(...)),
   DEVICE_MMIO_NAMED_ROM_INIT(grault, DT_DRV_INST(...)),
   ...
}

int my_driver_init(const struct device *dev)
{
   ...
   DEVICE_MMIO_NAMED_MAP(dev, corge, K_MEM_CACHE_NONE);
   DEVICE_MMIO_NAMED_MAP(dev, grault, K_MEM_CACHE_NONE);
   ...
}

int my_driver_some_function(const struct device *dev)
{
   ...
   /* Write some data to the MMIO regions */
   sys_write32(0xDEADBEEF, DEVICE_MMIO_GET(dev, grault));
   sys_write32(0xF0CCAC1A, DEVICE_MMIO_GET(dev, corge));
   ...
}
```

### Device Model Drivers with multiple MMIO regions in the same DT node

Some drivers may have multiple MMIO regions defined into the same DT device
node using the `reg-names` property to differentiate them, for example:

```devicetree
/dts-v1/;

/ {
        a-driver@40000000 {
                reg = <0x40000000 0x1000>,
                      <0x40001000 0x1000>;
                reg-names = "corge", "grault";
        };
};
```

This can be managed as seen in the previous section but this time using the
`DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME` macro instead. So the only difference
would be in the driver config struct:

```c
const static struct my_driver_config my_driver_config_0 = {
   ...
   DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(corge, DT_DRV_INST(...)),
   DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(grault, DT_DRV_INST(...)),
   ...
}
```

### Drivers that do not use Zephyr Device Model

Some drivers or driver-like code may not user Zephyr’s device model,
and alternative storage must be arranged for the MMIO data. An
example of this are timer drivers, or interrupt controller code.

This can be managed with the `DEVICE_MMIO_TOPLEVEL` set of macros,
for example:

```c
DEVICE_MMIO_TOPLEVEL_STATIC(my_regs, DT_DRV_INST(..));

void some_init_code(...)
{
   ...
   DEVICE_MMIO_TOPLEVEL_MAP(my_regs, K_MEM_CACHE_NONE);
   ...
}

void some_function(...)
   ...
   sys_write32(DEVICE_MMIO_TOPLEVEL_GET(my_regs), 0xDEADBEEF);
   ...
}
```

### Drivers that do not use DTS

Some drivers may not obtain the MMIO physical address from DTS, such as
is the case with PCI-E. In this case the `device_map()` function
may be used directly:

```c
void some_init_code(...)
{
   ...
   struct pcie_bar mbar;
   bool bar_found = pcie_get_mbar(bdf, index, &mbar);

   device_map(DEVICE_MMIO_RAM_PTR(dev), mbar.phys_addr, mbar.size, K_MEM_CACHE_NONE);
   ...
}
```

For these cases, DEVICE\_MMIO\_ROM directives may be omitted.

## API Reference

*group* device\_model
:   Device Model.

    Defines

    DEVICE\_HANDLE\_NULL
    :   Flag value used to identify an unknown device.

    DEVICE\_NAME\_GET(dev\_id)
    :   Expands to the name of a global device object.

        Return the full name of a device object symbol created by [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d), using the `dev_id` provided to [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d). This is the name of the global variable storing the device structure, not a pointer to the string in the [device::name](#structdevice_1a1e74e8d3b0b1a981c67e1d0284ccac3d) field.

        It is meant to be used for declaring extern symbols pointing to device objects before using the DEVICE\_GET macro to get the device object.

        This macro is normally only useful within device driver source code. In other situations, you are probably looking for [device\_get\_binding()](#group__device__model_1ga15386ca9ab38f3e30183c18f604fa835).

        Parameters:
        :   - **dev\_id** – Device identifier.

        Returns:
        :   The full name of the device object defined by device definition macros.

    DEVICE\_DEFINE(dev\_id, name, init\_fn, pm, data, config, level, prio, api)
    :   Create a device object and set it up for boot time initialization.

        This macro defines a [device](#structdevice) that is automatically configured by the kernel during system initialization. This macro should only be used when the device is not being allocated from a devicetree node. If you are allocating a device from a devicetree node, use [DEVICE\_DT\_DEFINE()](#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) or [DEVICE\_DT\_INST\_DEFINE()](#group__device__model_1gada5ba4aca9e0662ccebb2232c7256419) instead.

        Parameters:
        :   - **dev\_id** – A unique token which is used in the name of the global device structure as a C identifier.
            - **name** – A string name for the device, which will be stored in [device::name](#structdevice_1a1e74e8d3b0b1a981c67e1d0284ccac3d). This name can be used to look up the device with [device\_get\_binding()](#group__device__model_1ga15386ca9ab38f3e30183c18f604fa835). This must be less than Z\_DEVICE\_MAX\_NAME\_LEN characters (including terminating `NULL`) in order to be looked up from user mode.
            - **init\_fn** – Pointer to the device’s initialization function, which will be run by the kernel during system initialization. Can be `NULL`.
            - **pm** – Pointer to the device’s power management resources, a [pm\_device](../../services/pm/api/index.md#structpm__device), which will be stored in device::pm field. Use `NULL` if the device does not use PM.
            - **data** – Pointer to the device’s private mutable data, which will be stored in [device::data](#structdevice_1a27573cbd10ee145f8bb1396242b27a3e).
            - **config** – Pointer to the device’s private constant data, which will be stored in [device::config](#structdevice_1aca2d801eb15996cf1c74dc65cfa651fc).
            - **level** – The device’s initialization level (PRE\_KERNEL\_1, PRE\_KERNEL\_2 or POST\_KERNEL).
            - **prio** – The device’s priority within its initialization level. See SYS\_INIT() for details.
            - **api** – Pointer to the device’s API structure. Can be `NULL`.

    DEVICE\_DT\_NAME(node\_id)
    :   Return a string name for a devicetree node.

        This macro returns a string literal usable as a device’s name from a devicetree node identifier.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.

        Returns:
        :   The value of the node’s `label` property, if it has one. Otherwise, the node’s full name in `node-name@unit-address` form.

    DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, ...)
    :   Create a device object from a devicetree node identifier and set it up for boot time initialization.

        This macro defines a [device](#structdevice) that is automatically configured by the kernel during system initialization. The global device object’s name as a C identifier is derived from the node’s dependency ordinal. [device::name](#structdevice_1a1e74e8d3b0b1a981c67e1d0284ccac3d) is set to `[DEVICE_DT_NAME(node_id)](#group__device__model_1gad864d7a50ee45285dacd68be1e5a49ce)`.

        The device is declared with extern visibility, so a pointer to a global device object can be obtained with `[DEVICE_DT_GET(node_id)](#group__device__model_1ga9a65996ce21f43acb7db061e23b48ec7)` from any source file that includes `<zephyr/device.h>`. Before using the pointer, the referenced object should be checked using [device\_is\_ready()](#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb).

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Pointer to the device’s initialization function, which will be run by the kernel during system initialization. Can be `NULL`.
            - **pm** – Pointer to the device’s power management resources, a [pm\_device](../../services/pm/api/index.md#structpm__device), which will be stored in device::pm. Use `NULL` if the device does not use PM.
            - **data** – Pointer to the device’s private mutable data, which will be stored in [device::data](#structdevice_1a27573cbd10ee145f8bb1396242b27a3e).
            - **config** – Pointer to the device’s private constant data, which will be stored in [device::config](#structdevice_1aca2d801eb15996cf1c74dc65cfa651fc) field.
            - **level** – The device’s initialization level (PRE\_KERNEL\_1, PRE\_KERNEL\_2 or POST\_KERNEL).
            - **prio** – The device’s priority within its initialization level. See SYS\_INIT() for details.
            - **api** – Pointer to the device’s API structure. Can be `NULL`.

    DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like [DEVICE\_DT\_DEFINE()](#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1), but uses an instance of a `DT_DRV_COMPAT` compatible instead of a node identifier.

        Parameters:
        :   - **inst** – Instance number. The `node_id` argument to [DEVICE\_DT\_DEFINE()](#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) is set to `[DT_DRV_INST(inst)](../../build/dts/api/api.md#group__devicetree-inst_1ga219f413efba2f4c0151468b9a25a8dc1)`.
            - **...** – Other parameters as expected by [DEVICE\_DT\_DEFINE()](#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1).

    DEVICE\_DT\_NAME\_GET(node\_id)
    :   The name of the global device object for `node_id`.

        Returns the name of the global device structure as a C identifier. The device must be allocated using [DEVICE\_DT\_DEFINE()](#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) or [DEVICE\_DT\_INST\_DEFINE()](#group__device__model_1gada5ba4aca9e0662ccebb2232c7256419) for this to work.

        This macro is normally only useful within device driver source code. In other situations, you are probably looking for [DEVICE\_DT\_GET()](#group__device__model_1ga9a65996ce21f43acb7db061e23b48ec7).

        Parameters:
        :   - **node\_id** – Devicetree node identifier

        Returns:
        :   The name of the device object as a C identifier

    DEVICE\_DT\_GET(node\_id)
    :   Get a [device](#structdevice) reference from a devicetree node identifier.

        Returns a pointer to a device object created from a devicetree node, if any device was allocated by a driver.

        If no such device was allocated, this will fail at linker time. If you get an error that looks like `undefined reference to __device_dts_ord_<N>`, that is what happened. Check to make sure your device driver is being compiled, usually by enabling the Kconfig options it requires.

        Parameters:
        :   - **node\_id** – A devicetree node identifier

        Returns:
        :   A pointer to the device object created for that node

    DEVICE\_DT\_INST\_GET(inst)
    :   Get a [device](#structdevice) reference for an instance of a `DT_DRV_COMPAT` compatible.

        This is equivalent to `[DEVICE_DT_GET(DT_DRV_INST(inst))](#group__device__model_1ga9a65996ce21f43acb7db061e23b48ec7)`.

        Parameters:
        :   - **inst** – `DT_DRV_COMPAT` instance number

        Returns:
        :   A pointer to the device object created for that instance

    DEVICE\_DT\_GET\_ANY(compat)
    :   Get a [device](#structdevice) reference from a devicetree compatible.

        If an enabled devicetree node has the given compatible and a device object was created from it, this returns a pointer to that device.

        If there no such devices, this returns NULL.

        If there are multiple, this returns an arbitrary one.

        If this returns non-NULL, the device must be checked for readiness before use, e.g. with [device\_is\_ready()](#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb).

        Parameters:
        :   - **compat** – lowercase-and-underscores devicetree compatible

        Returns:
        :   a pointer to a device, or NULL

    DEVICE\_DT\_GET\_ONE(compat)
    :   Get a [device](#structdevice) reference from a devicetree compatible.

        If an enabled devicetree node has the given compatible and a device object was created from it, this returns a pointer to that device.

        If there are no such devices, this will fail at compile time.

        If there are multiple, this returns an arbitrary one.

        If this returns non-NULL, the device must be checked for readiness before use, e.g. with [device\_is\_ready()](#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb).

        Parameters:
        :   - **compat** – lowercase-and-underscores devicetree compatible

        Returns:
        :   a pointer to a device

    DEVICE\_DT\_GET\_OR\_NULL(node\_id)
    :   Utility macro to obtain an optional reference to a device.

        If the node identifier refers to a node with status `okay`, this returns `[DEVICE_DT_GET(node_id)](#group__device__model_1ga9a65996ce21f43acb7db061e23b48ec7)`. Otherwise, it returns `NULL`.

        Parameters:
        :   - **node\_id** – devicetree node identifier

        Returns:
        :   a [device](#structdevice) reference for the node identifier, which may be `NULL`.

    DEVICE\_GET(dev\_id)
    :   Obtain a pointer to a device object by name.

        Return the address of a device object created by [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d), using the dev\_id provided to [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d).

        Parameters:
        :   - **dev\_id** – Device identifier.

        Returns:
        :   A pointer to the device object created by [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d)

    DEVICE\_DECLARE(dev\_id)
    :   Declare a static device object.

        This macro can be used at the top-level to declare a device, such that [DEVICE\_GET()](#group__device__model_1gaf9403e7eb573a30d2dfaed357f4ef3f4) may be used before the full declaration in [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d).

        This is often useful when configuring interrupts statically in a device’s init or per-instance config function, as the init function itself is required by [DEVICE\_DEFINE()](#group__device__model_1gac12521f4d900e8947aac45c1b228366d) and use of [DEVICE\_GET()](#group__device__model_1gaf9403e7eb573a30d2dfaed357f4ef3f4) inside it creates a circular dependency.

        Parameters:
        :   - **dev\_id** – Device identifier.

    DEVICE\_INIT\_DT\_GET(node\_id)
    :   Get a init\_entry reference from a devicetree node.

        Parameters:
        :   - **node\_id** – A devicetree node identifier

        Returns:
        :   A pointer to the init\_entry object created for that node

    DEVICE\_INIT\_GET(dev\_id)
    :   Get a init\_entry reference from a device identifier.

        Parameters:
        :   - **dev\_id** – Device identifier.

        Returns:
        :   A pointer to the init\_entry object created for that device

    Typedefs

    typedef int16\_t device\_handle\_t
    :   Type used to represent a “handle” for a device.

        Every [device](#structdevice) has an associated handle. You can get a pointer to a [device](#structdevice) from its handle and vice versa, but the handle uses less space than a pointer. The device.h API mainly uses handles to store lists of multiple devices in a compact way.

        The extreme values and zero have special significance. Negative values identify functionality that does not correspond to a Zephyr device, such as the system clock or a SYS\_INIT() function.

        See also

        [device\_handle\_get()](#group__device__model_1ga456366a9ca0a8e97484c97c279745203)

        See also

        [device\_from\_handle()](#group__device__model_1ga73680daef9f8d7dc2541d83d09737f4a)

    typedef int (\*device\_visitor\_callback\_t)(const struct [device](#c.device) \*dev, void \*context)
    :   Prototype for functions used when iterating over a set of devices.

        Such a function may be used in API that identifies a set of devices and provides a visitor API supporting caller-specific interaction with each device in the set.

        The visit is said to succeed if the visitor returns a non-negative value.

        See also

        [device\_required\_foreach()](#group__device__model_1ga6e3b6dbb15ca28d6c94ee07702663245)

        See also

        [device\_supported\_foreach()](#group__device__model_1gaf5fce5e93fd6d5e13aa8b20251b82b2a)

        Param dev:
        :   a device in the set being iterated

        Param context:
        :   state used to support the visitor function

        Return:
        :   A non-negative number to allow walking to continue, and a negative error code to case the iteration to stop.

    Functions

    static inline [device\_handle\_t](#c.device_handle_t) device\_handle\_get(const struct [device](#c.device) \*dev)
    :   Get the handle for a given device.

        Parameters:
        :   - **dev** – the device for which a handle is desired.

        Returns:
        :   the handle for the device, or DEVICE\_HANDLE\_NULL if the device does not have an associated handle.

    static inline const struct [device](#c.device) \*device\_from\_handle([device\_handle\_t](#c.device_handle_t) dev\_handle)
    :   Get the device corresponding to a handle.

        Parameters:
        :   - **dev\_handle** – the device handle

        Returns:
        :   the device that has that handle, or a null pointer if `dev_handle` does not identify a device.

    static inline const [device\_handle\_t](#c.device_handle_t) \*device\_required\_handles\_get(const struct [device](#c.device) \*dev, size\_t \*count)
    :   Get the device handles for devicetree dependencies of this device.

        This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

        The array contains a handle for each device that `dev` requires directly, as determined from the devicetree. This does not include transitive dependencies; you must recursively determine those.

        Parameters:
        :   - **dev** – the device for which dependencies are desired.
            - **count** – pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if the device has no devicetree dependencies.

        Returns:
        :   a pointer to a sequence of `count` device handles, or a null pointer if `dev` does not have any dependency data.

    static inline const [device\_handle\_t](#c.device_handle_t) \*device\_injected\_handles\_get(const struct [device](#c.device) \*dev, size\_t \*count)
    :   Get the device handles for injected dependencies of this device.

        This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

        The array contains a handle for each device that `dev` manually injected as a dependency, via providing extra arguments to Z\_DEVICE\_DEFINE. This does not include transitive dependencies; you must recursively determine those.

        Parameters:
        :   - **dev** – the device for which injected dependencies are desired.
            - **count** – pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if the device has no devicetree dependencies.

        Returns:
        :   a pointer to a sequence of `*count` device handles, or a null pointer if `dev` does not have any dependency data.

    static inline const [device\_handle\_t](#c.device_handle_t) \*device\_supported\_handles\_get(const struct [device](#c.device) \*dev, size\_t \*count)
    :   Get the set of handles that this device supports.

        This function returns a pointer to an array of device handles. The length of the array is stored in the `count` parameter.

        The array contains a handle for each device that `dev` “supports” &#8212; that is, devices that require `dev` directly &#8212; as determined from the devicetree. This does not include transitive dependencies; you must recursively determine those.

        Parameters:
        :   - **dev** – the device for which supports are desired.
            - **count** – pointer to where this function should store the length of the returned array. No value is stored if the call returns a null pointer. The value may be set to zero if nothing in the devicetree depends on `dev`.

        Returns:
        :   a pointer to a sequence of `*count` device handles, or a null pointer if `dev` does not have any dependency data.

    int device\_required\_foreach(const struct [device](#c.device) \*dev, [device\_visitor\_callback\_t](#c.device_visitor_callback_t) visitor\_cb, void \*context)
    :   Visit every device that `dev` directly requires.

        Zephyr maintains information about which devices are directly required by another device; for example an I2C-based sensor driver will require an I2C controller for communication. Required devices can derive from statically-defined devicetree relationships or dependencies registered at runtime.

        This API supports operating on the set of required devices. Example uses include making sure required devices are ready before the requiring device is used, and releasing them when the requiring device is no longer needed.

        There is no guarantee on the order in which required devices are visited.

        If the `visitor_cb` function returns a negative value iteration is halted, and the returned value from the visitor is returned from this function.

        Note

        This API is not available to unprivileged threads.

        Parameters:
        :   - **dev** – a device of interest. The devices that this device depends on will be used as the set of devices to visit. This parameter must not be null.
            - **visitor\_cb** – the function that should be invoked on each device in the dependency set. This parameter must not be null.
            - **context** – state that is passed through to the visitor function. This parameter may be null if `visitor_cb` tolerates a null `context`.

        Returns:
        :   The number of devices that were visited if all visits succeed, or the negative value returned from the first visit that did not succeed.

    int device\_supported\_foreach(const struct [device](#c.device) \*dev, [device\_visitor\_callback\_t](#c.device_visitor_callback_t) visitor\_cb, void \*context)
    :   Visit every device that `dev` directly supports.

        Zephyr maintains information about which devices are directly supported by another device; for example an I2C controller will support an I2C-based sensor driver. Supported devices can derive from statically-defined devicetree relationships.

        This API supports operating on the set of supported devices. Example uses include iterating over the devices connected to a regulator when it is powered on.

        There is no guarantee on the order in which required devices are visited.

        If the `visitor_cb` function returns a negative value iteration is halted, and the returned value from the visitor is returned from this function.

        Note

        This API is not available to unprivileged threads.

        Parameters:
        :   - **dev** – a device of interest. The devices that this device supports will be used as the set of devices to visit. This parameter must not be null.
            - **visitor\_cb** – the function that should be invoked on each device in the support set. This parameter must not be null.
            - **context** – state that is passed through to the visitor function. This parameter may be null if `visitor_cb` tolerates a null `context`.

        Returns:
        :   The number of devices that were visited if all visits succeed, or the negative value returned from the first visit that did not succeed.

    const struct [device](#c.device) \*device\_get\_binding(const char \*name)
    :   Get a [device](#structdevice) reference from its [device::name](#structdevice_1a1e74e8d3b0b1a981c67e1d0284ccac3d) field.

        This function iterates through the devices on the system. If a device with the given `name` field is found, and that device initialized successfully at boot time, this function returns a pointer to the device.

        If no device has the given `name`, this function returns `NULL`.

        This function also returns NULL when a device is found, but it failed to initialize successfully at boot time. (To troubleshoot this case, set a breakpoint on your device driver’s initialization function.)

        Parameters:
        :   - **name** – device name to search for. A null pointer, or a pointer to an empty string, will cause NULL to be returned.

        Returns:
        :   pointer to device structure with the given name; `NULL` if the device is not found or if the device with that name’s initialization function failed.

    bool device\_is\_ready(const struct [device](#c.device) \*dev)
    :   Verify that a device is ready for use.

        Indicates whether the provided device pointer is for a device known to be in a state where it can be used with its standard API.

        This can be used with device pointers captured from [DEVICE\_DT\_GET()](#group__device__model_1ga9a65996ce21f43acb7db061e23b48ec7), which does not include the readiness checks of [device\_get\_binding()](#group__device__model_1ga15386ca9ab38f3e30183c18f604fa835). At minimum this means that the device has been successfully initialized.

        Parameters:
        :   - **dev** – pointer to the device in question.

        Return values:
        :   - **true** – If the device is ready for use.
            - **false** – If the device is not ready for use or if a NULL device pointer is passed as argument.

    struct device\_state
    :   *#include <device.h>*

        Runtime device dynamic structure (in RAM) per driver instance.

        Fields in this are expected to be default-initialized to zero. The kernel driver infrastructure and driver access functions are responsible for ensuring that any non-zero initialization is done before they are accessed.

        Public Members

        uint8\_t init\_res
        :   Device initialization return code (positive errno value).

            Device initialization functions return a negative errno code if they fail. In Zephyr, errno values do not exceed 255, so we can store the positive result value in a uint8\_t type.

        bool initialized
        :   Indicates the device initialization function has been invoked.

    struct device
    :   *#include <device.h>*

        Runtime device structure (in ROM) per driver instance.

        Public Members

        const char \*name
        :   Name of the device instance.

        const void \*config
        :   Address of device instance config information.

        const void \*api
        :   Address of the API structure exposed by the device instance.

        struct [device\_state](#c.device_state) \*state
        :   Address of the common device state.

        void \*data
        :   Address of the device instance private data.

        const [device\_handle\_t](#c.device_handle_t) \*deps
        :   Optional pointer to dependencies associated with the device.

            This encodes a sequence of sets of device handles that have some relationship to this node. The individual sets are extracted with dedicated API, such as [device\_required\_handles\_get()](#group__device__model_1ga2157bbfc2deecfae6514f58221663618). Only available if  [`CONFIG_DEVICE_DEPS`](../../kconfig.md#CONFIG_DEVICE_DEPS "CONFIG_DEVICE_DEPS") is enabled.

        union [device](#c.device).[anonymous] [anonymous]
        :   Reference to the device PM resources (only available if  [`CONFIG_PM_DEVICE`](../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is enabled).
