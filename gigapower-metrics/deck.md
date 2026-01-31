---
marp: true
theme: default
paginate: true
header: 'Gigapower Efficiency Metrics | Data Capabilities Overview'
footer: '2026-01-28 | Install Insight'
style: |
  section {
    padding: 50px 50px 80px 50px;
  }
  table {
    font-size: 0.8em;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Gigapower Installation Efficiency Metrics

**What We Can (and Can't) Measure**

Install Insight | January 2026

---

# Our data combines AT&T legacy fiber and Gigapower in shared tables

The Snowflake warehouse contains work order data from **two distinct operations**:

| Source | Identifier | Data Maturity |
|--------|-----------|---------------|
| **AT&T Legacy Fiber** | Various flags | Years of data, well-populated tables |
| **Gigapower (FIBERCO)** | `NOTE_SRC='FIBERCO'` filter | Newer operation, sparser coverage |

**Key point**: Tables that work well for AT&T legacy analysis may have **zero rows** for Gigapower installs. The `FIBERCO` flag is how we isolate Gigapower data.

---

# Gigapower has less data coverage than AT&T legacy

Many ML and dispatch tables are populated for legacy fiber but **empty for Gigapower**:

| Table | AT&T Legacy | Gigapower |
|-------|-------------|-----------|
| `VCTD601_TECH_DISPATCH` | ~15M rows | **0 rows** |
| `VCTD600_WO_DISPATCH_UNNECESSARY_ML` | Populated | **0 rows** |
| `VCTD600_WO_DISPATCH_BILLING_ML` | Populated | **0 rows** |
| `VCTD555_REPEAT_1-5` | Populated | **0 rows** (repairs only) |

**Implication**: Metrics calculable for AT&T legacy fiber may not be calculable for Gigapower with current data.

---

# Bottom line: 8 metrics calculable, 6 blocked by data gaps

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

| Calculable (8) | Not Calculable (6) |
|----------------|-------------------|
| Installation Completion Rate | Avoidable Dispatch Rate |
| Single-Visit Completion Rate | Technician Utilization |
| Average Dispatches per Install | On-Time Arrival Rate |
| Median On-Site Duration | Technician Performance |
| Jeopardy Rate & Code Distribution | Billing Attribution |
| Days to Complete (median & P90) | **Customer Satisfaction** *(requires external data)* |
| Cancellation Rate | |
| Appointment Slippage (derivable) | |

---

# Critical constraint: Dispatch logging only reliable from Q4 2025

"On Site" events in `WO_EVENT_HISTORY_TEMP` were **not consistently logged** until Q4 2025:

| Quarter | Gigapower Installs | With Dispatch Event | Coverage |
|---------|-------------------|---------------------|----------|
| Q1 2025 | 285 | 12 | **4.2%** |
| Q2 2025 | 9,552 | 22 | **0.2%** |
| Q3 2025 | 13,622 | 2,638 | **19.4%** |
| **Q4 2025** | 15,309 | 14,765 | **96.4%** |
| Q1 2026 | 2,743 | 2,700 | **98.4%** |

**Result**: Dispatch-based metrics (single-visit rate, on-site duration) are only reliable for Q4 2025 onwards. Historical trend analysis is not possible.

---

<!-- _class: lead -->

# Section 2

## What We CAN Measure

---

# Current Q4 2025+ baseline meets industry benchmarks

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.9em; }
td:nth-child(4) { font-weight: bold; }
</style>

| Metric | Gigapower | Industry Benchmark | Assessment |
|--------|-----------|-------------------|------------|
| Installation Completion Rate | 90.1% | 90%+ | Meets |
| Single-Visit Completion Rate | 74.6% | 70-80% (FTFR proxy) | Within range |
| Avg Dispatches per Install | 1.45 | 1.3-1.5 | Within range |
| Median On-Site Duration | 121 min | 2-4 hrs typical | Efficient |
| Jeopardy Rate | 20.1% | Lower is better | Notable |
| Median Days to Complete | 4 days | Varies | — |
| 90th Percentile Days | 14 days | Varies | — |

**Cohort**: 18,052 installs from Q4 2025+ (96.7% dispatch coverage)

---

# Dispatch coverage improved dramatically in Q4 2025

```
Coverage of "On Site" dispatch events over time:

Q1 2025  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   4.2%
Q2 2025  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0.2%
Q3 2025  ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  19.4%
Q4 2025  ████████████████████████████████████████████████░░  96.4%  ← Logging fixed
Q1 2026  ██████████████████████████████████████████████████  98.4%
```

**Root cause**: Event logging for FIBERCO technician dispatches was introduced or improved in Q4 2025. This is **not** due to self-installs (only 0.6% mention self-install in notes).

---

# Data sources are fragmented across multiple tables

| Metric | Primary Table | Key Filter | Date Restriction |
|--------|--------------|------------|------------------|
| Completion Rate | `VCTD600_WO_WORK_ORDER` | `STS` field | None |
| Single-Visit Rate | `WO_EVENT_HISTORY_TEMP` | `STS='DISPATCH', STS_RSN='On Site'` | **Q4 2025+** |
| Dispatches/Install | `WO_EVENT_HISTORY_TEMP` | Count "On Site" events | **Q4 2025+** |
| On-Site Duration | `WO_EVENT_HISTORY_TEMP` | Time between events | **Q4 2025+** |
| Jeopardy Rate | `WO_EVENT_HISTORY_TEMP` | `STS='JEOPARDY'` | Recommended Q4+ |
| Days to Complete | `VCTD600_WO_WORK_ORDER` | `CRTD_TS` to `STS_TS` | None |

**Note**: All dispatch-based metrics require the `CRTD_TS >= '2025-10-01'` filter.

---

# Additional metrics are derivable but not yet calculated

These can be computed from existing data:

| Metric | Source | Status |
|--------|--------|--------|
| **Appointment Slippage** | `WO_DATES_TEMP` (`ORIGL_DUE_TS` vs actual) | Available, not calculated |
| **Days in Jeopardy** | `WO_EVENT_HISTORY_TEMP` | Available, not calculated |
| **Multi-Visit Breakdown** | `WO_EVENT_HISTORY_TEMP` | Calculated |
| **Jeopardy Code Distribution** | `WO_EVENT_HISTORY_TEMP` | Calculated |

**Already calculated**:
- Multi-visit: 1 visit (74.6%), 2 visits (15.4%), 3 visits (5.2%), 4+ visits (4.8%)
- Top jeopardy codes: GPF (6.3%), UVB (5.9%), UFC (5.2%)

---

<!-- _class: lead -->

# Section 3

## What We CANNOT Measure

---

# Six key metrics have zero Gigapower data

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

| Desired Metric | Would Require | Why Unavailable |
|----------------|---------------|-----------------|
| **Avoidable Dispatch Rate** | ML dispatch tables | Zero rows for Gigapower |
| **Repeat Visit Rate (10/30 day)** | `VCTD555_REPEAT` tables | Repairs only, no installs |
| **Technician Performance** | `VCTD601_TECH_DISPATCH` | Zero rows for Gigapower |
| **Billing Attribution** | ML billing table | Zero rows for Gigapower |
| **Technician Utilization** | Per-tech time tracking | No FIBERCO tech data |
| **On-Time Arrival Rate** | Scheduled vs actual arrival | No actual arrival time |

These tables **exist and are populated** — but not for Gigapower/FIBERCO installs.

---

# ML dispatch tables contain no Gigapower installs

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.95em; }
</style>

Tables designed for dispatch optimization have **zero coverage**:

| Table | Purpose | Gigapower Records |
|-------|---------|-------------------|
| `VCTD600_WO_DISPATCH_UNNECESSARY_ML` | Flag avoidable truck rolls | **0** |
| `WO_KEPLER_DISPATCH_UNNECESSARY_TEMP` | ML unnecessary prediction | **0** when `JT2_DEF='INSTALL'` |
| `VCTD600_WO_DISPATCH_BILLING_ML` | Network vs Customer fault | **0** |

**Impact**: Cannot quantify avoidable truck rolls. Industry baseline is ~25% avoidable — we cannot validate whether Gigapower is better or worse.

---

# Technician-level data is completely absent for FIBERCO

<style scoped>
section { padding: 50px 50px 80px 50px; }
code { font-size: 0.8em; }
</style>

`VCTD601_TECH_DISPATCH` contains **~15 million records** but **zero** for Gigapower.

**What this blocks**: Identifying high/low performers, training opportunities, workload balancing, utilization rates.

**Workaround**: None — only aggregate patterns are visible.

---

# Repeat visit tables track repairs only, not installs

The `VCTD555_REPEAT_1-5` table family is designed for **repair recurrence**, not installation follow-ups:

| What We Want | What the Table Provides |
|--------------|------------------------|
| "Did a completed install need a follow-up visit?" | "Did a repair need to be repeated?" |
| Install quality / first-time-right | Repair effectiveness |

**Context**: Industry "repeat visit rate" metrics (10/30 day windows) assume repair scenarios. For new installs, "single-visit completion rate" is the appropriate proxy — which we **can** calculate at 74.6%.

---

# Customer satisfaction is a blind spot

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

**No direct customer satisfaction data exists in Snowflake.**

| Industry Metric | Telecom Benchmark | Our Data |
|-----------------|-------------------|----------|
| NPS (Net Promoter Score) | 20-30 (T-Mobile: 82) | None |
| CSAT | ISPs: ~64% | None |
| CES (Customer Effort Score) | Lower is better | None |
| Installation Experience Score | — | None |

**Available proxies**: Cancellation rate, days to complete, jeopardy rate, single-visit rate

---

<!-- _class: lead -->

# Section 4

## Why This Matters

---

# Data gaps block meaningful optimization

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

| Gap | Business Impact |
|-----|-----------------|
| No unnecessary dispatch flag | Cannot quantify avoidable truck rolls (~$150-$1,000 each) |
| No technician-level data | Cannot identify training opportunities or performance issues |
| No per-tech utilization | Cannot optimize scheduling beyond aggregate patterns |
| No billing attribution | Cannot allocate costs to Network vs Customer fault |

**Partial workaround**: Jeopardy codes provide a proxy for root cause:
- **GPF** = Outside Plant/Drop/ONT Issues (6.3% of installs)
- **UVB/UFC** = Customer-related issues

---

# Historical trend analysis is impossible for dispatch metrics

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

Because dispatch logging only became reliable in Q4 2025:

| What We'd Want | What We Can Do |
|----------------|----------------|
| "Is single-visit rate improving?" | Only measure current state |
| "Are dispatches per install trending down?" | No baseline for comparison |
| "Did a process change reduce on-site time?" | Cannot measure before/after |

**Going forward**: Q4 2025 becomes the baseline. Future quarters can be compared to it, but no historical context exists.

---

<!-- _class: lead -->

# Appendix

---

# Data source reference

<style scoped>
section { padding: 50px 50px 80px 50px; }
table { font-size: 0.75em; }
</style>

| Table | Purpose | Gigapower Coverage |
|-------|---------|-------------------|
| `VCTD600_WO_WORK_ORDER` | Work order master | Full |
| `WO_NOTES_TEMP` | Technician notes | Full (`NOTE_SRC='FIBERCO'`) |
| `WO_EVENT_HISTORY_TEMP` | Event timeline | Partial (Q4 2025+ for dispatch) |
| `WO_DATES_TEMP` | Date milestones | Partial |
| `VCTD601_TECH_DISPATCH` | Technician dispatches | **None** |
| `VCTD555_REPEAT_1-5` | Repeat visits | **None** (repairs only) |
| `VCTD600_WO_DISPATCH_UNNECESSARY_ML` | ML unnecessary flag | **None** |
| `VCTD600_WO_DISPATCH_BILLING_ML` | Billing attribution | **None** |

---

# Industry benchmark sources

- [Fieldy - 2026 Guide to Field Service KPIs](https://getfieldy.com/blogs/field-service-metrics-kpi-examples)
- [NetSuite - Field Service Metrics Guide](https://www.netsuite.com/portal/resource/articles/erp/field-services-kpis-metrics.shtml)
- [FieldConnect - 17 Field Service Metrics](https://resources.fieldconnect.com/blog/field-service-metrics)
- [TechSee - How to Reduce Truck Rolls](https://techsee.com/blog/reduce-truck-rolls/)
- [CustomerGauge - Telecom NPS Benchmarks](https://customergauge.com/benchmarks/blog/telecommunications-nps-benchmarks-and-cx-trends)
- [Calix - CTC Case Study](https://www.calix.com/blog/2023/04/innovative-broadband-in-a-box-helps-ctc-increase-service-activation-and-cut-truck-rolls-by-50-percent.html)
