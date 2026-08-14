## Risk Description
Over-capacity registration occurs when the system allows more students to register for an event than the capacity value the administrator defined at event creation. Because registration is currently handled as a simple database insert with no atomic check against the remaining seat count, near-simultaneous registration requests close to the capacity limit can both succeed, and no automated boundary check stops registration once capacity has already been reached. If this happens, attendance and event management data no longer reflect actual seat availability, the venue may become overcrowded, and administrators lose an accurate record of who is expected to attend.

## Initial Risk Assessment
- **Likelihood Score: 3** — Registration currently performs a simple insert with no atomic check against the remaining seat count, so two students submitting requests at nearly the same moment near the capacity limit can both be accepted — a realistic race-condition scenario under normal usage (e.g., a popular event close to its registration deadline).
- **Impact Score: 4** — Overcapacity registration leads to physical overcrowding at the venue, inaccurate attendance and participation data used in institutional reporting, and disrupted staffing/seating/safety planning, though it does not compromise system security or cause data loss.
- **Initial Risk Score: 3 × 4 = 12**

## Mitigation Strategy
Add server-side capacity validation that checks the current confirmed-registration count against the event's maximum capacity before each registration is committed, wrapped in an atomic database transaction (or a row-level lock on the event record) so two simultaneous requests cannot both read the same "seat available" state and both be approved. The check-and-insert must happen as a single atomic operation rather than two separate steps, rejecting any request that would push the confirmed count past capacity.

## Test Cases
| Test Case ID | Scenario | Expected Result |
|---|---|---|
| TC-CAP-01 | Register students up to the event's exact capacity | All registrations succeed |
| TC-CAP-02 | A registration attempt is made for the (capacity + 1)th student | Registration is rejected with an "Event Full" response |
| TC-CAP-03 | Two students submit registration requests at nearly the same time when exactly one seat remains | Exactly one registration succeeds; the other is rejected — no overbooking occurs |
| TC-CAP-04 | A student attempts to register after capacity has already been reached, where a waitlist feature exists | Student is added to the waitlist rather than confirmed as registered |

## Revised Risk Assessment (Post-Mitigation)
- **Revised Likelihood Score: 1** — Once TC-CAP-01 through TC-CAP-03 are executed and pass, the atomic capacity check is verified to hold under both boundary and concurrent-access conditions, reducing the likelihood of overcapacity to a residual, low-probability event.
- **Revised Risk Score: 1 × 4 = 4**
- Residual risk remains for registration paths that bypass the standard flow (e.g., a bulk-import or admin-override registration endpoint), if those entry points are not covered by the same atomic capacity check.
