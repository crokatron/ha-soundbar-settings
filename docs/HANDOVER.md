# HA Soundbar Settings: maintainer handover

[One-screen summary](START-HERE.md) · [User manual](USER-MANUAL.md) · [Feature overview](../README.md) · [Recorded validation](../VALIDATION.md)

## Purpose and behaviour to preserve

Expose selected advanced Samsung soundbar settings as native Home Assistant entities. It reuses the official SmartThings integration’s connection instead of requiring another saved token. Developed against the HW-Q990F, it complements ordinary media-player controls rather than replacing the soundbar’s whole interface.

- **Speaker levels:** Bass/subwoofer, centre and rear levels: integer sliders from −6 to +6. (number entities.)
- **Sound mode:** Standard, Surround, Game Pro and Adaptive Sound. (select entity.)
- **Audio switches:** Bass boost, night mode and voice amplifier. (switch entities.)
- **Existing connection:** Use the already configured HA SmartThings OAuth session. (Cloud dependency.)
- **Single-setting commands:** Validate and send one setting per command; no automatic write retry. (Runtime behaviour.)
- **Assumed state:** Show unknown initially and retain the last accepted setting; this is not physical readback. (Display limitation.)

The [demo](../demo.html) is a smaller, labelled simulation with fictional data. It explains cause and effect without the real service; it is not evidence of a working production installation. Numbered screenshots in the user manual distinguish actual-app captures from demo captures.

## Files and sources of truth

| Actual package path | Maintainer role |
| --- | --- |
| [projects-host/ha-custom-components/mungoon_soundbar](../projects-host/ha-custom-components/mungoon_soundbar) | Discovery, command validation and HA entities |
| [tools/test_soundbar.py](../tools/test_soundbar.py) | Command payload tests |
| [demo-source](../demo-source) | Editable demo HTML/CSS/runtime and embedded screenshot tour |
| [SOURCE-MANIFEST.json](../SOURCE-MANIFEST.json) | Original copied-source paths and SHA-256 checkpoint values |

The original working source is under C:/Users/lamon/Desktop/AI TOOLS/NAS for NAS modules; adjacent CAD/watch source locations are recorded by the full backup’s reviewed source manifest. This package contains only the explicitly copied source, not an automatic mirror. The main private nas-projects backup retains the broader shared host context.

## Setup, run and tests

Run commands from this repository root unless a `cd` is shown. Use a disposable checkout and fictional data for first setup. Dependencies, SDKs, signing material and personal data are not bundled. The following are continuation instructions grounded in the retained source, **not commands executed or newly certified by this handover**.

```powershell
python -B tools/test_soundbar.py
```

Install under HA /config/custom_components/mungoon_soundbar, validate/restart HA, then add Mungoon Soundbar Settings. Follow docs/soundbar-settings.md.

Selected project check:

```powershell
python -B tools/test_soundbar.py
```

For the documentation demo alone, serve this repository on loopback with `python -m http.server 8765 --bind 127.0.0.1` and open `/demo.html`. Choose a free port if another preview is running. JavaScript syntax can be checked with `node --check demo-source/runtime.js`. `python demo-source/rebuild.py` rewrites demo.html, so run it only in a disposable checkout or an authorised demo-editing session. A local server cannot provide missing HA/CAD/NAS functions. Inspect browser tests for installed dependencies, fixture requirements and network targets before running them with the approved browser tooling.

## Data, configuration and backup boundaries

Credentials remain with HA SmartThings OAuth; no extra token belongs in this repo. Internet access to SmartThings is required. Unknown/assumed values must not be presented as physical state.

Connection credentials remain with HA’s existing SmartThings integration. Entity restore retains accepted settings for display, but remembered values do not prove current hardware state. Internet access to SmartThings is required.

Git preserves reviewed source and documentation. It does not copy browser storage, application databases, uploaded models/photos, accepted device settings, SDKs or credentials. Maintain independent recovery copies of the data identified above, including matching configuration and asset versions. Never add real secrets to examples, issues or logs. Private source copies on GitHub are not proof of a complete NAS/offsite data backup.

## Current verification and Git state

Before these documentation edits on 14 October 2026, this package was clean on branch `main` at `eb717ce40f30c2a76e3c608c717f93b601325c6b` and its private upload was verified. All 12 manifest-listed source entries matched their stored checksums before editing. The upload follow-up has completed all 17 repositories and is paused; it does not run this tool or back up its live data.

These handover pages and README links accompany the source package. Preserve them when continuing; stage only reviewed changes. Recheck current `git status --short --branch` and `git diff` before starting. No project-specific background schedule was inspected or changed in this documentation pass. Any service schedules in older notes are historical claims to verify in the actual deployment.

Earlier package checks and limits are recorded in [VALIDATION.md](../VALIDATION.md). This handover adds documentation/link/whitespace/secret and source-preservation checks only. No current NAS release, real hardware state, fresh installation, complete data restoration or offsite-backup freshness was verified here.

## Recovery approach

1. Preserve the current installation/data before changing it. Identify the exact code commit and data snapshot required; do not assume this package matches the running service.
2. Recover source into a new folder. Verify the source manifest and restore the project-specific configuration/assets described above separately. Recreate dependencies from the retained project files and guides.
3. Restore user data into an isolated instance or clean test browser. Check a representative editable record, associated files and save/reload behaviour, then compare to the original. Do not test recovery by overwriting production.
4. Record what actually restored and what remains missing. A demo opening or a passing syntax check is not a production recovery drill. Real deployment/device actions need the existing authorised workflow.

## Known limits and next work

Only the supported command payloads are promised. Other Samsung models require testing. Three command tests passed previously; no sound settings or physical-device tests were changed during this documentation work.

**Priority:** Retest on the actual Q990F and installed HA release, one setting at a time. Test other models before advertising support; check SmartThings discovery/capabilities before changing sound settings.

Common symptoms to check for this tool:

- No soundbar discovered: verify official SmartThings setup, capability discovery and the device model/label.
- Command rejected: use supported whole-number ranges and exact mode names.
- Slider disagrees with remote: expected readback limitation; inspect the physical setting.
- Breakage after HA upgrade: check compatibility with SmartThings runtime internals.

Keep [the release checklist](../RELEASE-CHECKLIST.md) and [third-party notes](../THIRD-PARTY.md) with the package. Original contributions use MIT; bundled/upstream code and assets keep their own licences. Public publication is a separate decision; preparing documentation is not permission to publish.
