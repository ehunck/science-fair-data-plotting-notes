# Audit and Improvement Plan for `science_fair_graphing_workbook.md`

## Summary
The workbook is clear and student-friendly, but it can be strengthened by adding missing guidance, expanding explanations, and adding more matplotlib graphics (especially for pie charts and error bars). The Google Sheets tutorial also needs steps for pie charts and multi-series plots.

## Missing or Thin Sections
- **Pie charts**: Guidance exists, but there are no good/bad matplotlib examples.
- **Multiple measurements**: Concepts are described, but there are no error bar examples and no “how to” in Google Sheets for plotting multiple trials.
- **Google Sheets tutorial**: Missing pie chart steps and multi-series (overlay/average/error bars) steps.

## Areas to Expand (Length and Clarity)
- **Why graphs matter**: Add 1–2 sentences about fairness and honest scales.
- **Variables section**: Add a short paragraph explaining why controlled variables matter and how to list them.
- **Data types**: Add 1–2 sentences clarifying continuous vs discrete and how that affects the axis.
- **Chart choice sections**: Add 1–2 sentences for each chart type explaining a common mistake and how to avoid it.
- **Checklist**: Add a few items about sample size, scale honesty, and showing variability.

## New Matplotlib Graphics to Add
- **Pie chart**: Good vs bad using the same data (bad example uses no labels/percent and visual tricks).
- **Error bars**: Good vs bad using the same mean data (bad example hides variability or chops axis).
- **Multiple time series**: Already added; can add a “bad legend” or “mismatched scales” example if needed.

## Implementation Plan
1. Add new matplotlib plots in `generate_plots.py` (pie good/bad, error bars good/bad).
2. Update the workbook to reference new images and expand explanations.
3. Expand Google Sheets tutorial with pie chart and multi-series instructions.
4. Update `progress.md` as changes are made.
