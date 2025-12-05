# Keyword Research: Base64 Encoder

**Source:** MongoDB, Chrome-Stats, Estimated Data
**Database:** United States (US)
**Date:** 2025-12-05

---

## Summary Metrics

| Metric | Value | Assessment |
|--------|-------|------------|
| Volume US (est.) | 300 | FAIL (<500) |
| Global Volume (est.) | 3,000 | LOW |
| KD% | ~20% | EASY (Green) |
| CPC | $0.15 (est.) | LOW |
| Intent | Commercial | GOOD |

---

## Main Keyword Analysis

| Keyword | Volume (est.) | KD | Intent | Assessment |
|---------|---------------|-----|--------|------------|
| **base64 encoder** | 300 | 20% | C | LOW |
| base64 decode | 2,000 | 35% | C | PASS |
| base64 converter | 500 | 25% | C | PASS |
| base64 to image | 800 | 30% | C | PASS |

**Note:** Better to target "base64 decoder" or "base64 converter" keywords

---

## Market Analysis (MongoDB)

### Top Competitors

| Extension | ID | Description | Optimized? |
|-----------|-----|-------------|------------|
| Base64 Encode/Decode | gkdcpimagggbnjdkjhbnilfeiidhdhcl | Basic tool | NO |
| Base64 Encoder and Decoder | hmndaanmnneonjcekcbeeedioimiffpj | Full functionality | PARTIAL |
| Base64 Decoder | ababhhiegjhaohnipcgjfgfeljakfhhc | Decode only | NO |
| URL Decode/Encode | dgoepmkoiphgabefpbapldnjmbbiaoag | URL encoding | NO |

### Optimization Check

| Criterion | Leader | Requirement | Status |
|----------|-------|------------|--------|
| Title = key | Similar | Exact match | NO |
| Description | ~400 chars | >3,000 chars | NO |
| Localization | <10 langs | >30 langs | NO |

**Conclusion:** Key is FREE but very low volume

---

## SERP Analysis (Google)

**Query:** "base64 encoder"

| # | URL | Type | Soft? |
|---|-----|------|-------|
| 1 | base64encode.org | Service | YES |
| 2 | base64.guru | Service | YES |
| 3 | codebeautify.org | Service | YES |
| 4 | utilities-online.info | Service | YES |
| 5 | meyerweb.com/eric/tools | Service | YES |
| 6 | opinionatedgeek.com | Service | YES |
| 7 | browserling.com | Service | YES |
| 8 | rapidtables.com | Service | YES |
| 9 | w3schools.com | Tutorial | NO |
| 10 | developer.mozilla.org | Docs | NO |

**Softness:** 80% - good!

---

## JTBD Analysis (MongoDB)

```
"When I'm developing websites, I want developer tools,
 so I can debug and test more efficiently"

"When I need to encode/decode data, I want a quick tool,
 so I don't have to write code for it"
```

**Target Audience:**
- Web Developers
- API Developers
- Security Researchers
- Data Engineers

---

## Traffic Calculations

```python
# US Volume (combined keywords)
us_volume = 300 + 2000 + 500  # = 2,800 combined

# Global English (x10)
global_en = us_volume * 10  # = 28,000

# All languages (x10)
global_all = global_en * 10  # = 280,000

# Monthly potential (main keyword only)
monthly_potential = 3000
```

---

## Open Source

| Repository | License | Notes |
|------------|---------|-------|
| Built-in btoa/atob | Native JS | No library needed |
| js-base64 | MIT | npm package |
| base64-js | MIT | npm package |

---

## Conclusion

| Criterion | Assessment | Status |
|----------|--------|--------|
| Volume | 300 US (main) | FAIL |
| Combined Volume | 2,800 US | PASS |
| KD | ~20% | PASS |
| Softness | 80% | PASS |
| Key FREE | YES | PASS |
| Intent | C | GOOD |
| Complexity | TRIVIAL | PASS |

### Recommendation

**NO-GO for primary keyword** / **GO for combined approach**

**Advantages:**
- Trivial implementation (btoa/atob)
- Low competition
- Dev tools niche
- Could combine with other encoders (URL, HTML entities)

**Risks:**
- Very low volume for main keyword
- Online tools dominate
- Limited differentiation
- Below 500 threshold for primary keyword

**Alternative Strategy:**
- Name it "Encoder/Decoder" or "Dev Converter"
- Support multiple formats: Base64, URL, HTML, Unicode
- Target combined keywords

---

*Captain Builders Bootcamp - Lesson 02*
