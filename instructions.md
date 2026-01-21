# Agent Brief: Middle School Science Fair Workbook — Plotting Data Meaningfully

## Goal (What you are making)
Create a **short, middle-school-friendly workbook** (in **Markdown**) that teaches science fair students how to **choose the right type of plot** and **make graphs that communicate results clearly**.

This workbook will be exported to **PDF**, so formatting and embedded images must print cleanly.

## Audience + Tone
- Audience: **middle school science fair students** (and their parents/teachers)
- Tone: **clear, friendly, encouraging**
- Assume: students know basic math and tables, but may not know “variables,” “axes,” or “trendline.”

## Deliverable Format
- Primary deliverable: a single **Markdown file** (e.g., `science_fair_graphing_workbook.md`)
- All explanatory example graphs in the workbook must be **generated with matplotlib** and included as images in the Markdown.
  - Save images to a folder like: `images/`
  - Reference them in Markdown: `![caption](images/filename.png)`

## Hard Requirements
1. **All plots used for explanation must be created with matplotlib.**  
   - This includes “good” and “bad” examples.
2. The “how to” tutorial students follow should use **Google Sheets** (not matplotlib).
3. The section on selecting plot type must include:
   - **When to use it**
   - **A good example** (with matplotlib image + why it’s good)
   - **A bad example** (with matplotlib image + why it’s misleading)
4. Include a clear section on **variable types**:
   - manipulated/independent variable
   - responding/dependent variable
   - controlled variables/constants
   - repeated trials/replicates (and why they matter)

---

# Suggested Workbook Structure (Use this outline)

## 1) Why Graphs Matter in a Science Fair
- A graph is a “picture of your results”
- A good graph helps someone understand your experiment in 10 seconds
- A bad graph can confuse people even if your experiment was great

## 2) Variables: What Changed, What You Measured, What You Kept the Same
Explain with simple language + a table.

### Required content
- **Manipulated (Independent) Variable**: what you change on purpose  
- **Responding (Dependent) Variable**: what you measure  
- **Controlled Variables (Constants)**: what you keep the same  
- **Trials/Replicates**: repeating measurements to make results more reliable

### Include at least 2 concrete examples (use kid-friendly scenarios)
Example A: “Amount of sunlight” vs “plant height”  
Example B: “Ramp height” vs “toy car distance”

Include a mini-check:
- “If I changed it on purpose → manipulated”
- “If I measured it → responding”
- “If I tried to keep it the same → controlled”

## 3) Data Types: What Kind of Data Do You Have?
Introduce simple categories that connect directly to chart choice:
- **Numbers that can go on a number line (continuous)**: height, time, temperature
- **Counts (discrete)**: number of seeds sprouted
- **Categories (labels)**: brand A/B/C, type of soil
- **Time series**: something measured over time (minute-by-minute / day-by-day)

## 4) Choosing the Right Graph Type (Core Section)
This section must teach chart choice using **good vs bad examples**.
For each plot type below, include:
- **Best for**
- **What to put on the axes**
- **Good example** image (matplotlib) + short explanation
- **Bad example** image (matplotlib) + short explanation of what’s wrong
- A 1-sentence “rule of thumb”

### Plot types to include (minimum set)
1. **Scatter Plot** (with optional trendline)
2. **Line Graph** (time series)
3. **Bar Chart** (compare categories)
4. **Histogram** (show distribution of many measurements)

### Optional (only if kept simple and short)
- **Box-and-whisker** (only if you can explain simply)
- **Dot plot** (often easier than box plots for middle school)

### Examples you can use (pick consistent fake datasets)
Use simple, realistic numbers (10–15 rows max) and keep units consistent.

**Scatter (good):** Fertilizer amount (g) vs Plant height (cm)  
**Scatter (bad):** Using a bar chart for those same continuous x-values (or connecting dots randomly when x isn’t time)

**Line (good):** Temperature (°C) over time (minutes) while cooling  
**Line (bad):** Using a pie chart or bars that imply categories instead of time

**Bar (good):** Average paper towel absorbency for Brand A/B/C  
**Bar (bad):** Using bars for a continuous independent variable (like 1,2,3,4 grams) where a scatter would show trend better

**Histogram (good):** Distribution of 30 measurements of “how far the toy car rolled”  
**Histogram (bad):** Histogram made from only 3 data points or using categories as histogram bins

### “Bad Example” Guidelines (Make them instructive, not silly)
Bad examples should demonstrate common real mistakes:
- Wrong chart type for the data
- Missing axis labels/units
- Uneven scales or chopped axis that exaggerates results
- Too many colors / clutter
- Connecting points when it implies something untrue
- Pie charts for non-parts-of-a-whole data (explain why)

## 5) Graph Quality Checklist (One-Page Student Checklist)
Include a checklist students can use before turning in:
- Title explains what was tested
- X-axis = manipulated variable, Y-axis = responding variable (most of the time)
- Labels include **units** (cm, g, s, °C)
- Numbers on axes make sense and are evenly spaced
- Data points are easy to see
- Legend only if needed
- If you have multiple trials: show averages or show all points (explain which/why)

## 6) Google Sheets Tutorial: Making the Graph for Your Project
This is the hands-on “do this” section students follow.

### Required steps
- Enter data in a clean table (headers in row 1)
- Highlight data
- Insert → Chart
- Choose correct chart type (tie back to Section 4)
- Add/format:
  - Chart title
  - Axis titles + units
  - Legend (if needed)
  - Trendline (for scatter, when appropriate)
  - Show equation/R² only if your rubric wants it (optional)
- Export or copy the chart into their report (simple instructions)

### Include “If you get stuck” troubleshooting
- Chart picked the wrong axis → how to switch rows/columns
- Values treated as text → how to fix
- Trendline missing → ensure scatter chart

## 7) Mini Practice (Quick Student Activity)
Give 2 short practice datasets and ask:
1) Identify manipulated/responding/controlled variables  
2) Pick the best graph type  
3) Explain why (one sentence)  

(Students don’t need to run matplotlib; they can do Sheets.)

## 8) Wrap-Up
A short conclusion:
- “Your graph is part of your explanation”
- Encourage students to ask: “Could someone understand my results without me talking?”

---

# Matplotlib Plot Generation Requirements (for the explanatory images)
Create a small script or notebook (your choice) that generates every example graph image used in the workbook.

## Figure style rules (PDF-friendly)
- Use readable fonts and sizes (export at high DPI)
- Add axis labels and units on **good examples**
- Intentionally omit or misuse labels/scales on **bad examples** (to teach why it matters)
- Keep backgrounds clean, avoid unnecessary decorations
- Save images as `.png` into `images/`

## Naming convention
Use consistent filenames, for example:
- `images/scatter_good.png`
- `images/scatter_bad_wrong_type.png`
- `images/line_good_time_series.png`
- `images/bar_bad_continuous_x.png`
- `images/hist_good_distribution.png`

---

# Success Criteria (What “done” looks like)
- A middle schooler can:
  - correctly label manipulated/responding/controlled variables
  - choose between scatter/line/bar/histogram for common experiments
  - explain what’s wrong with typical “bad graphs”
  - create their final graph in Google Sheets with labels + units
- The Markdown exports to PDF cleanly, with all matplotlib images visible and captioned.
