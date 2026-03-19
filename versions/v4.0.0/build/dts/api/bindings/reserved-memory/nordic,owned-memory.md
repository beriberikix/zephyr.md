---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/reserved-memory/nordic,owned-memory.html
original_path: build/dts/api/bindings/reserved-memory/nordic,owned-memory.html
---

# nordic,owned-memory

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic Owned Memory

Memory region with permission attributes. Each enabled region of this kind
will be recorded in the UICR of the compiled domain. Memory ownership and
access is then configured for the domain at boot time, based on the UICR.

Example:

  reserved-memory {
      memory@2fc00000 {
          compatible = "nordic,owned-memory";
          reg = <0x2fc00000 0x1000>;
          status = "okay";
          nordic,access = <NRF_OWNER_ID_APPLICATION NRF_PERM_R>,
                          <NRF_OWNER_ID_RADIOCORE NRF_PERM_W>;
      };
  };

A single local domain can request a memory region to be reserved on behalf of
multiple access owners. A single memory region shall be reserved by at most
one domain, by setting status "okay" on the associated node. For example, if
the region defined above is enabled by Application on behalf of Radiocore,
then the Radiocore's devicetree must set status "disabled" on that node.

Each of the different owners may have a different set of permissions granted,
as also shown above.

Note: one domain can also reserve memory for another domain and not itself.
Whichever domain has status "okay" set on the node does not need to be listed
as one of the access owners.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nordic,access` | `array` | ```text Array of (owner-id, permission-flags) pairs, where:  - Owner ID represents the domain that will have access to this memory.   Valid values can be found in dts/common/nordic/<soc>.dtsi,   where they are defined as NRF_OWNER_ID_*  - Permissions are encoded as a 32-bit bitfield, using the flags found in   include/zephyr/dt-bindings/reserved-memory/nordic-owned-memory.h,   where they are defined as NRF_PERM_*    The same file defines all possible permission flag combinations.   For example, one can use:     <NRF_OWNER_ID_APPLICATION NRF_PERM_RWX>    as a shorthand for:     <NRF_OWNER_ID_APPLICATION (NRF_PERM_R | NRF_PERM_W | NRF_PERM_X)> ``` |
| `zephyr,memory-region` | `string` | ```text Signify that this node should result in a dedicated linker script memory region in the final executable. The region address and size is taken from the <reg> property, while the name is the value of this property. ``` |
| `zephyr,memory-attr` | `int` | ```text Attribute or set of attributes (bitmask) for the memory region. See 'include/zephyr/dt-bindings/memory-attr/memory-attr.h' for a comprehensive list with description of possible values. ``` |

Deprecated properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `owner-id` | `int` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner ID of the domain that will own this memory region. If not defined, the ownership will default to the domain being compiled.  Note: owner ID is not the same as domain ID; see the product specification for details. ``` |
| `perm-read` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has read access to the region. ``` |
| `perm-write` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has write access to the region. ``` |
| `perm-execute` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner can execute code from the region. ``` |
| `perm-secure` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Owner has secure-only access to the region. ``` |
| `non-secure-callable` | `boolean` | ```text Deprecated, applies only if 'nordic,access' is not defined. Memory region is used for non-secure-callable code. ``` |
| `zephyr,memory-region-mpu` | `string` | ```text Signify that this node should result in a dedicated MPU region. Deprecated in favor of 'zephyr,memory-attr'. ``` |

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,owned-memory” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
