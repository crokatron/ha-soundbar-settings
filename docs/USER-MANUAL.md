# HA Soundbar Settings — visual user manual

[Project overview](../README.md) · [Offline interactive demo](../demo.html)

Start with the numbered picture guide. Each number identifies the exact highlighted control. Work through one step at a time; the longer reference is below it.

### Try the working offline example

Screenshot of this project’s interactive demo. Side-by-side services are explicitly simulated.

![HA Soundbar Settings — numbered controls](images/guide-1.jpg)

1. **Choose an audio setting.** Set levels, a sound mode or night mode in this example.
2. **Send a dummy command.** The simulated cloud accepts the setting without contacting a soundbar.
3. **Read assumed state correctly.** Accepted values are remembered values, not physical readback.

## Detailed task reference

### Find the controls

1. First confirm the soundbar already appears in the official SmartThings integration in HA.
2. Add Mungoon Soundbar Settings, choose the detected soundbar, and open its entities in Devices & services.
3. Add the relevant number, switch and select entities to a dashboard or use their entity controls directly. The integration itself does not provide a separate custom dashboard.

### Adjust dialogue without changing everything

1. Choose one control to test, such as Center speaker level. Note your current physical setting independently if you will want to revert.
2. Move the slider by one whole-number step and listen for the response. Use Voice amplifier only if that is the intended effect.
3. Avoid changing several controls at once while diagnosing compatibility. A cloud response saying COMPLETED means the request was accepted, not that the setting was measured on the hardware.

### Create an evening audio action

1. Use HA’s normal automation editor and select the Night mode entity. Add the intended on/off action at your chosen trigger.
2. Optionally set Sound mode using the exact available option labels. Keep this separate from power/volume actions on the ordinary media player.
3. Test once while you can hear the soundbar. Since writes are not automatically retried, inspect HA errors before repeating a failed command.

### Interpret unknown and assumed readings

1. Unknown after installation does not mean the soundbar is disconnected: the tested device does not provide advanced-setting readback.
2. A value shown after an accepted command is the component’s remembered value. A later change on the remote or Samsung app can leave it out of date.
3. Use the physical device to confirm actual state when it matters. Full graphic equalizer bands are not provided by this component.

## Keep your work

Connection credentials remain with HA’s existing SmartThings integration. Entity restore retains accepted settings for display, but remembered values do not prove current hardware state. Internet access to SmartThings is required.

## If something looks wrong

- No soundbar discovered: verify official SmartThings setup, capability discovery and the device model/label.
- Command rejected: use supported whole-number ranges and exact mode names.
- Slider disagrees with remote: expected readback limitation; inspect the physical setting.
- Breakage after HA upgrade: check compatibility with SmartThings runtime internals.

## What this manual does not promise

Only the supported command payloads are promised. Other Samsung models require testing. Three command tests passed previously; no sound settings or physical-device tests were changed during this documentation work.

Screenshots show the actual application where captured. The offline demo is a deliberately smaller simulation and identifies its dummy services. It never controls devices, sends notifications, uploads files or launches printing.
