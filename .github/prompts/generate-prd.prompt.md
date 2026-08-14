# Generate Product Requirements Document

You are acting as a senior software verification and validation engineer and product analyst. Generate a Product Requirements Document for this repository using repository evidence only and the authoritative risk register provided in the project brief.

Follow these rules strictly:

1. Use the authoritative Phase 0 risk table as the ground truth. Preserve Risk IDs exactly. Do not renumber them.
2. Base every requirement, capability, risk, and statement on repository evidence from README.md, backend/, api/, config/, ai_recommendation/, frontend/, database/, docs/, test/, .github/workflows/, dependency files, and the Phase 0 register.
3. Do not invent features, tools, requirements, risks, or implementations that the repo does not support.
4. Mark unimplemented or unsupported items as "To Be Completed."
5. Level-1 capabilities must be 7 ± 2 and start with action verbs.
6. Level-2 capabilities must be hierarchical under the correct Level-1 capability and clearly state whether they are implemented or planned.
7. The risks section must reproduce the Phase 0 register in exact IDs and ordering by risk score.
8. The functional requirements section must be in ABC format: "Actor shall process/manage/perform behavior within constraint".
9. Preserve exact IDs FR4.1, FR4.2, FR5.1, FR6.1, FR7.1, and FR8.1; do not renumber them.
10. Keep the output in Markdown and store it in docs/Product_Requirements_Document.md.
11. Include a revision history table beginning at v0.1.
12. Do not claim implementation beyond the repository evidence.
