# Moon Restaurant  — Food Delivery App Optimization

**Role:** Business Analyst (Simulated)
**Tools:** SQL (SQLite), Python, Lucidchart, Power BI, Jira
**Type:** Portfolio Project

---

## Problem Statement

Product managers and developers lacked clear visibility into user retention and digital drop-off points, making it difficult to pinpoint where and why users were abandoning their sessions. A 500-row behavioral dataset was gathered and analyzed to expose where the platform loses user engagement.

Two key pain points were identified:
- Users were abandoning sessions at a **12% higher rate** than industry average due to mandatory account creation at checkout
- Users were abandoning carts at a **15% higher rate** than industry average due to carts not saving between sessions

---

## Solution

Acting as the BA, I recommended and documented two features:

1. **Guest Checkout** — removes the mandatory login bottleneck, reducing checkout steps from 6 to 3
2. **Cart Auto-Save** — persists cart items for up to 24 hours after a session ends

---

## Deliverables

### Process Maps
- **As-Is Diagram** — maps the current flow showing the login bottleneck and cart deletion pain points
- **To-Be Diagram** — maps the improved flow with guest checkout and cart saving

### Functional Requirements Documentation
- Feature summaries for both Guest Checkout and Cart Auto-Save
- 4 Agile User Stories (US-101 through US-104) with Acceptance Criteria
- Global out-of-scope items defined

### Dataset
- 500-row CSV simulating user behavior across two periods:
  - **As-Is period** (Mar–Dec 2024): ~21% order completion rate
  - **To-Be period** (Jan–Jul 2025): ~58% order completion rate
- 21 columns including session data, device type, checkout type, drop-off stage, and timing

### SQL Queries (SQLite)
Four queries written against the dataset:
1. Drop-off count by stage
2. Order completion rate before vs. after feature launch
3. Average session time by checkout type (Guest vs. Registered)
4. Abandonment count by device type

### Dashboard *(In Progress)*
Power BI dashboard visualizing KPIs including abandonment rate, average checkout time, and before/after conversion comparison.

---

## Key Findings

| Metric | As-Is | To-Be |
|---|---|---|
| Sessions | 290 | 210 |
| Completed Orders | 60 | 122 |
| Completion Rate | ~21% | ~58% |
| Avg Session Time (Registered) | 361 sec | — |
| Avg Session Time (Guest) | — | 311 sec |

Top drop-off stage in As-Is: **Account Login/Register (142 sessions)**

---

## Project Structure

```
BA Project/
├── data/
│   └── moonrestaurant_user_behavior.csv
├── database/
│   └── moonrestaurant.db
├── scripts/
│   ├── database_setup.py
│   ├── viewDropoff.py
│   ├── viewAbandonment.py
│   ├── viewAvgCheckoutTime.py
│   └── ViewAbandonmentViaDevice.py
├── docs/
│   └── FUNCTIONAL_REQUIREMENTS_DOCUMENTATION.pdf
├── diagrams/
│   └── AS-IS_TO-BE_DIAGRAMS.pdf
├── main.py
└── README.md
```

---

## Author

**Asef Ajmain**
Information Systems — Drexel University