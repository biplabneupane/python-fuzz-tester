# Fuzzing Input Analysis

**Total Files Analyzed:** `5`

**Unique Patterns Detected:** `3`

**File Size Stats:**
- Smallest File: `3 bytes`
- Largest File: `230 bytes`
- Average File Size: `109.60 bytes`

| File Name | Decoded Data | Hex Representation | Size | Most Common Byte | Category | Pattern Detection |
|-----------|-------------|--------------------|------|------------------|----------|-------------------|
| `slow-unit-8fbcf56f7e4354e7d1824d784599bac7debf339f` | `'<non-UTF8 data>'` | `900ef8...` | `3 bytes` | `0x90 (1 times)` | `Uncategorized binary` | `No obvious repeating patterns.` |
| `slow-unit-8befccf5d514d4d98a37d838880a6442535908b7` | `'<non-UTF8 data>'` | `ffffffffffffff096868...` | `230 bytes` | `0x68 (118 times)` | `Uncategorized binary` | `⚠️ Possible repeating pattern detected: f` |
| `slow-unit-57010ff039d6392e1152edb1a787e272c9afb088` | `'<non-UTF8 data>'` | `ffffffffffffffffffff...` | `81 bytes` | `0xff (78 times)` | `Uncategorized binary` | `⚠️ Possible repeating pattern detected: f` |
| `slow-unit-b5270b8cb6c17810f6060a54cbd224c35b93c8f6` | `'<non-UTF8 data>'` | `4c4c4c4c4c4c4c4c4c4c...` | `219 bytes` | `0xea (114 times)` | `Uncategorized binary` | `⚠️ Possible repeating pattern detected: 4c` |
| `slow-unit-1c8ab50f2d14424868876eb659b46b6d6d87eeb1` | `'<non-UTF8 data>'` | `21212121212121e4dede...` | `15 bytes` | `0x21 (11 times)` | `Uncategorized binary` | `⚠️ Possible repeating pattern detected: 21` |