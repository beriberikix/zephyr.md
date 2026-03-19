---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/porting/soc_porting.html
original_path: hardware/porting/soc_porting.html
---

# SoC Porting Guide

This page describes how to add support for a new [SoC](../../glossary.md#term-SoC) in Zephyr, be it in
the upstream Zephyr project or locally in your own repository.

## SoC Definitions

It is expected that you are familiar with the board concept in Zephyr.
A high level overview of the hardware support hierarchy and terms used in the
Zephyr documentation can be seen in [Hardware support hierarchy](board_porting.md#hw-support-hierarchy).

For SoC porting, the most important terms are:

- SoC: the exact system on a chip the board’s CPU is part of.
- SoC series: a group of tightly related SoCs.
- SoC family: a wider group of SoCs with similar characteristics.
- CPU Cluster: a cluster of one or more CPU cores.
- CPU core: a particular CPU instance of a given architecture.
- Architecture: an instruction set architecture.

### Architecture

See [Architecture Porting Guide](arch.md#architecture-porting-guide).

## Create your SoC directory

Each SoC must have a unique name. Use the official name given by the SoC vendor
and check that it’s not already in use. In some cases someone else may have
contributed a SoC with identical name. If the SoC name is already in use, then
you should probably improve the existing SoC instead of creating a new one.
The script `list_hardware` can be used to retrieve a list of all SoCs known
in Zephyr, for example `./scripts/list_hardware.py --soc-root=. --socs` from
the Zephyr base directory for a list of names that are already in use.

Start by creating the directory `zephyr/soc/<VENDOR>/soc1`, where
`<VENDOR>` is your vendor subdirectory.

Note

A `<VENDOR>` subdirectory is mandatory if contributing your SoC
to Zephyr, but if your SoC is placed in a local repo, then any folder
structure under `<your-repo>/soc` is permitted.
The `<VENDOR>` subdirectory must match a vendor defined in the list in
[dts/bindings/vendor-prefixes.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/bindings/vendor-prefixes.txt). If the SoC vendor does not
have a prefix in that list, then one must be created.

Note

The SoC directory name does not need to match the name of the SoC.
Multiple SoCs can even be defined in one directory. In Zephyr, SoCs are often
organized in sub-folders in a common SoC Family or SoC Series tree.

Your SoC directory should look like this:

```text
soc/<VENDOR>/<soc-name>
├── soc.yml
├── soc.h
├── CMakeLists.txt
├── Kconfig
├── Kconfig.soc
└── Kconfig.defconfig
```

Replace `<soc-name>` with your SoC’s name.

The mandatory files are:

1. `soc.yml`: a YAML file describing the high-level meta data of the
   SoC such as:

   - SoC name: the name of the SoC
   - CPU clusters: CPU clusters if the SoC contains one or more clusters
   - SoC series: the SoC series to which the SoC belong
   - SoC family: the SoC family to which the series belong
2. `soc.h`: a header file which can be used to describe or provide
   configuration macros for the SoC. The `soc.h` will often be included in
   drivers, sub-systems, boards, and other source code found in Zephyr.
3. `Kconfig.soc`: the base SoC configuration which defines a Kconfig SoC
   symbol in the form of `config SOC_<soc-name>` and provides the SoC name to
   the Kconfig `SOC` setting.
   If the `soc.yml` describes a SoC family and series, then those must also
   be defined in this file. Kconfig settings outside of the SoC tree must not be
   selected. To select general Zephyr Kconfig settings the `Kconfig` file
   must be used.
4. `CMakeLists.txt`: CMake file loaded by the Zephyr build system. This
   CMake file can define additional include paths and/or source files to be used
   when a build targets the SoC. Also the base line linker script to use must be
   defined.

The optional files are:

- `Kconfig`, `Kconfig.defconfig` software configuration in
  [Configuration System (Kconfig)](../../build/kconfig/index.md#kconfig) format. These select the architecture and peripherals
  available.

## Write your SoC YAML

The SoC YAML file describes the SoC family, SoC series, and SoC at a high level.

Detailed configurations, such as hardware description and configuration are done
in devicetree and Kconfig.

The skeleton of a simple SoC YAML file containing just one SoC is:

```yaml
socs:
- name: <soc1>
```

It is possible to have multiple SoC located in the SoC folder.
For example if they belong to a common family or series it is recommended to
locate such SoC in a common tree.
Multiple SoCs and SoC series in a common folder can be described in the
`soc.yml` file as:

```yaml
family:
  name: <family-name>
  series:
    - name: <series-1-name>
      socs:
        - name: <soc1>
          cpucluster:
            - name: <coreA>
            - name: <coreB>
              ...
        - name: <soc2>
    - name: <series-2-name>
      ...
```

## Write your SoC devicetree

SoC devicetree include files are located in the `<zephyr-repo>/dts` folder
under a corresponding `<ARCH>/<VENDOR>`.

The SoC `dts/<ARCH>/<VENDOR>/<soc>.dtsi` describes your SoC hardware in
the Devicetree Source (DTS) format and must be included by any boards which use
the SoC.

If a highlevel `<arch>.dtsi` file exists, then a good starting point is to
include this file in your `<soc>.dtsi`.

In general, `<soc>.dtsi` should look like this:

```devicetree
#include <arch>/<arch>.dtsi

/ {
        chosen {
                /* common chosen settings for your SoC */
        };

        cpus {
                #address-cells = <m>;
                #size-cells = <n>;

                cpu@0 {
                device_type = "cpu";
                compatible = "<compatibles>";
                /* ... your CPU definitions ... */
        };

        soc {
                /* Your SoC definitions and peripherals */
                /* such as ram, clock, buses, peripherals. */
        };
};
```

Hint

It is possible to structure multiple `<VENDOR>/<soc>.dtsi` files in
sub-directories for a cleaner file system structure. For example organized
pre SoC series, like this: `<VENDOR>/<SERIES>/<soc>.dtsi`.

### Multiple CPU clusters

Devicetree reflects the hardware. The memory space and peripherals available to
one CPU cluster can be very different from another CPU cluster, therefore each
CPU cluster will often have its own `.dtsi` file.

CPU cluster `.dtsi` files should follow the naming scheme
`<soc>_<cluster>.dtsi`. A `<soc>_<cluster>.dtsi` file will look
similar to a SoC `.dtsi` without CPU clusters.

## Write Kconfig files

Zephyr uses the Kconfig language to configure software features. Your SoC
needs to provide some Kconfig settings before you can compile a Zephyr
application for it.

Setting Kconfig configuration values is documented in detail in
[Setting Kconfig configuration values](../../build/kconfig/setting.md#setting-configuration-values).

There is one mandatory Kconfig file in the SoC directory, and two optional
files for a SoC:

```text
soc/<vendor>/<your soc>
├── Kconfig.soc
├── Kconfig
└── Kconfig.defconfig
```

`Kconfig.soc`
:   A shared Kconfig file which can be sourced both in Zephyr Kconfig and sysbuild
    Kconfig trees.

    This file selects the SoC family and series in the Kconfig tree and potential
    other SoC related Kconfig settings. In some cases a SOC\_PART\_NUMBER.
    This file must not select anything outside the re-usable Kconfig SoC tree.

    A `Kconfig.soc` may look like this:

    ```kconfig
    config SOC_<series name>
            bool

    config SOC_<SOC_NAME>
            bool
            select SOC_SERIES_<series name>

    config SOC
            default "SoC name" if SOC_<SOC_NAME>
    ```

    Notice that `SOC_NAME` is a pure upper case version of the SoC name.

    The Kconfig `SOC` setting is globally defined as a string and therefore the
    `Kconfig.soc` file shall only define the default string value and not
    the type. Notice that the string value must match the SoC name used in the
    `soc.yml` file.

`Kconfig`
:   Included by [soc/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig).

    This file can add Kconfig settings which are specific to the current SoC.

    The `Kconfig` will often indicate given hardware support using a setting
    of the form `HAS_<support>`.

    ```kconfig
    config SOC_<SOC_NAME>
            select ARM
            select CPU_HAS_FPU
    ```

    If the setting name is identical to an existing Kconfig setting in Zephyr and
    only modifies the default value of said setting, then
    `Kconfig.defconfig` should be used instead.

`Kconfig.defconfig`
:   SoC specific default values for Kconfig options.

    Not all SoCs have a `Kconfig.defconfig` file.

    The entire file should be inside a pair of `if SOC_<SOC_NAME>` / `endif`
    or `if SOC_SERIES_<SERIES_NAME>` / `endif`, like this:

    ```kconfig
    if SOC_<SOC_NAME>

    config NUM_IRQS
            default 32

    endif # SOC_<SOC_NAME>
    ```

### Multiple CPU clusters

CPU clusters must provide additional Kconfig settings in the `Kconfig.soc`
file. This will usually be in the form of `SOC_<SOC_NAME>_<CLUSTER>` so for
a given `soc1` with two clusters `clusterA` and `clusterB`, then this
will look like:

SoC’s When a SoC defines CPU cluster

> ```kconfig
> config SOC_SOC1_CLUSTERA
>         bool
>         select SOC_SOC1
>
> config SOC_SOC1_CLUSTERB
>         bool
>         select SOC_SOC1
> ```
