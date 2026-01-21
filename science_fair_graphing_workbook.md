# Science Fair Skills: Plotting Data Meaningfully

## Why Graphs Matter in a Science Fair
- A graph is a picture of your results.
- A good graph helps someone understand your experiment in 10 seconds.
- A bad graph can confuse people even if your experiment was great.

Graphs are part of your evidence. Honest labels and honest scales help people trust what you found.

## Variables: What Changed, What You Measured, What You Kept the Same

**Simple definitions table**

| Variable type | What it means | Quick example |
| --- | --- | --- |
| Manipulated (independent) | What you change on purpose | Amount of sunlight |
| Responding (dependent) | What you measure | Plant height |
| Controlled (constants) | What you keep the same | Same soil, same pot size |
| Trials/replicates | Repeating the test to be more reliable | Measure each plant 3 times |

**Example A: Sunlight and plant height**
- Manipulated: amount of sunlight each plant gets
- Responding: plant height (cm)
- Controlled: type of soil, pot size, water amount, plant species
- Trials: measure several plants or measure the same plant multiple times

**Example B: Ramp height and toy car distance**
- Manipulated: ramp height (cm)
- Responding: distance the toy car rolls (cm)
- Controlled: same car, same ramp surface, same release point
- Trials: roll the car 3 or more times for each height

**Mini-check**
- If I changed it on purpose -> manipulated
- If I measured it -> responding
- If I tried to keep it the same -> controlled

Why controls and trials matter: If you do not keep things the same, you cannot tell what really caused the change. Repeated trials help you see if a result is reliable or just a lucky accident.

## Data Types: What Kind of Data Do You Have?
- Numbers that go on a number line (continuous): height, time, temperature
- Counts (discrete): number of seeds sprouted
- Categories (labels): brand A/B/C, type of soil
- Time series: something measured over time (minute-by-minute or day-by-day)

Continuous data can include decimals and can go anywhere on a number line. Discrete counts are whole numbers. Categories are names, not numbers, even if you can put them in order.

## Choosing the Right Graph Type

### Scatter Plot (with optional trendline)
- Best for: two number-line variables (continuous) to see a relationship
- Axes: X = manipulated, Y = responding

| Good example | Bad example |
| --- | --- |
| ![Scatter plot: fertilizer vs plant height (good)](images/scatter_good_fertilizer_vs_height.png)<br>Why it works: Both axes are numbers with units, and the trendline helps you see the pattern. | ![Scatter plot: fertilizer vs plant height with chopped axis (bad)](images/scatter_bad_chopped_axis.png)<br>Why it is misleading: The data are the same, but the chopped y-axis makes the trend look steeper. The axes are also unlabeled. |

**Rule of thumb:** If both variables are numbers, start with a scatter plot and label both axes.

### Line Graph vs Scatter Plot (when to choose each)
- Use a line graph when the X-axis is time or a true sequence (day-by-day, minute-by-minute).
- Use a scatter plot when the X-axis is not time (like grams of fertilizer or ramp height).
- A line implies the values flow from one point to the next. If that is not true, use scatter.

### Line Graph (time series)
- Best for: data measured over time
- Axes: X = time, Y = measurement

| Good example | Bad example |
| --- | --- |
| ![Line graph: cooling over time (good)](images/line_good_cooling.png)<br>Why it works: Time is in order on the X-axis, and the line shows how temperature changes. | ![Line graph: cooling over time with chopped axis (bad)](images/line_bad_chopped_axis.png)<br>Why it is misleading: The y-axis is chopped, which makes changes look bigger than they are. The axes are also unlabeled. |

**Rule of thumb:** If time is on the X-axis, use a line graph and keep the scale honest.

### Bar Chart (compare categories)
- Best for: comparing categories or named groups (non-numeric manipulated values)
- Axes: X = categories, Y = numbers

| Good example | Bad example |
| --- | --- |
| ![Bar chart: plant height by treatment (good)](images/bar_good_fertilizer_treatments.png)<br>Why it works: Each bar is a different treatment (including a water-only control), and the y-axis shows plant height. | ![Bar chart: plant height by treatment with chopped axis (bad)](images/bar_bad_fertilizer_treatments_chopped_axis.png)<br>Why it is misleading: The y-axis does not start at zero, so the differences look much bigger than they are. |

**Rule of thumb:** Use bar charts for categories. If the manipulated variable is numeric and ordered (like grams), use a scatter or line chart instead.

### Histogram (show distribution)
- Best for: many measurements of the same thing
- Axes: X = measurement values, Y = how many times those values appear

| Good example | Bad example |
| --- | --- |
| ![Histogram: toy car distance distribution (good)](images/hist_good_distribution.png)<br>Why it works: Many measurements show the shape of the data and the most common values. | ![Histogram: too many bins (bad)](images/hist_bad_too_many_bins.png)<br>Why it is misleading: The same data are split into too many tiny bins, which hides the overall pattern. The axes are also unlabeled. |

**Rule of thumb:** Use a histogram when you have many measurements and choose a reasonable number of bins.

### Pie Chart (parts of a whole)
- Best for: showing how a whole is divided into categories that add up to 100%.
- Axes: none; each slice is a percent of the total.
- Good uses: percent of time spent on different tasks, percent of types of litter collected, percent of plants that survived vs died.
- Not good for: trends over time, comparisons that are not parts of one whole, or data with many similar values.

| Good example | Bad example |
| --- | --- |
| ![Pie chart: litter types with labels (good)](images/pie_good_litter_types.png)<br>Why it works: The chart shows one whole and each slice is labeled with a percent. | ![Pie chart: unlabeled and exploded slice (bad)](images/pie_bad_unlabeled_exploded.png)<br>Why it is misleading: The slice is exaggerated and there are no labels, so the viewer cannot tell the real sizes. |

**Rule of thumb:** Use a pie chart only when all slices add to one whole and the differences are easy to see.

## Multiple Measurements: How to Show Repeated Trials

When you measure the same thing many times, you have choices. Pick the one that best tells your story and fits your class rules.

**Option A: Individual plots (show every trial)**
- Best when you have only a few trials or you want to show variation clearly.
- Example: three lines on the same time graph, one for each trial.

**Option B: Overlaid samples (all trials on one graph)**
- Best when you have several trials and they follow a similar pattern.
- Use light colors for trials and one bold average line.

**Option C: Error bars (show average plus variability)**
- Best when you want a clean graph but still show how spread out the trials were.
- Error bars show range or standard deviation (ask your teacher which to use).

**Rule of thumb:** If your class wants one clean graph, use the average with error bars. If they want to see every trial, plot each trial separately or overlay them lightly.

### Error Bars Example (Matplotlib)

| Good example | Bad example |
| --- | --- |
| ![Line graph: error bars showing variability (good)](images/line_errorbars_good.png)<br>Why it works: The average is clear and the error bars show how spread out the trials were. | ![Line graph: no error bars and chopped axis (bad)](images/line_errorbars_bad_hidden.png)<br>Why it is misleading: The missing error bars hide variability, and the chopped axis makes changes look bigger. |

### Multiple Time Series Examples (Matplotlib)

| Good example | Bad example |
| --- | --- |
| ![Line graph: multiple trials with average (good)](images/line_multi_overlaid_good.png)<br>Why it works: The individual trials are light, so the average stands out, and the axes are labeled. | ![Line graph: many trials overlaid without labels (bad)](images/line_multi_overlaid_bad_clutter.png)<br>Why it is misleading: The lines overlap and the viewer cannot tell which line is which or how many trials there are. |

**Good alternative: Small multiples (one panel per trial)**

![Line graph: separate panels per trial (good)](images/line_multi_small_multiples_good.png)

Why it works: Each trial is easy to compare because all panels share the same scale.

## Graph Quality Checklist (One-Page Student Checklist)
- Title explains what was tested
- X-axis = manipulated variable, Y-axis = responding variable (most of the time)
- Labels include units (cm, g, s, C)
- Numbers on axes make sense and are evenly spaced
- For bar charts, the y-axis should start at 0
- Do not connect dots unless the X-axis is time or a true sequence
- Data points are easy to see
- If you have multiple trials, show variability with error bars or multiple lines
- Include how many trials you ran (n = 3, n = 5, etc.)
- Legend only if needed
- If you have multiple trials: show all points, an average line, or error bars (explain which and why)

## Google Sheets Tutorial: Making the Graph for Your Project

This section walks you through each chart type in Google Sheets.

**Before you start**
- Put your data in a clean table with headers in row 1.
- Keep each variable in its own column.
- Include units in your headers (for example, "Time (min)").
- If you have multiple trials, put each trial in its own column.

### Scatter Plot in Google Sheets (two number-line variables)
1. Put the manipulated variable in column A and the responding variable in column B.
2. Highlight both columns, including the headers.
3. Click Insert -> Chart.
4. In the Chart editor (Setup tab), set Chart type to Scatter chart.
5. Make sure the X-axis is column A and the Series is column B. If they are flipped, click "Switch rows/columns."
6. Open the Customize tab -> Chart and axis titles. Add a chart title and axis titles with units.
7. Optional: Customize -> Series -> Trendline. Use a trendline only if it helps show a real pattern.

![Google Sheets screenshot placeholder: Scatter chart setup](images/sheets_scatter_setup_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

### Line Graph in Google Sheets (data over time)
1. Put time in column A and your measurement in column B.
2. Highlight both columns, including the headers.
3. Click Insert -> Chart.
4. In the Chart editor (Setup tab), set Chart type to Line chart.
5. Make sure "Use row 1 as headers" and "Use column A as labels" are checked.
6. Add a chart title and axis titles with units (Customize -> Chart and axis titles).
7. Keep the x-axis in order so the line connects points in time order.

![Google Sheets screenshot placeholder: Line chart setup](images/sheets_line_setup_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

### Bar Chart in Google Sheets (compare categories)
1. Put your categories in column A (text labels like "Brand A").
2. Put the numbers you are comparing in column B.
3. Highlight both columns, including the headers.
4. Click Insert -> Chart.
5. In the Chart editor (Setup tab), set Chart type to Column chart or Bar chart.
6. Add a chart title and axis titles with units (Customize -> Chart and axis titles).
7. Check the vertical axis starts at 0 (Customize -> Vertical axis -> Min).

![Google Sheets screenshot placeholder: Column chart setup](images/sheets_bar_setup_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

### Histogram in Google Sheets (distribution of many measurements)
1. Put all measurements in a single column (no categories).
2. Highlight the column, including the header.
3. Click Insert -> Chart.
4. In the Chart editor (Setup tab), set Chart type to Histogram.
5. Adjust bucket size (Customize -> Histogram). Aim for 5 to 10 bins so the shape is easy to see.
6. Add a chart title and axis titles with units (Customize -> Chart and axis titles).

![Google Sheets screenshot placeholder: Histogram setup](images/sheets_histogram_setup_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

### Pie Chart in Google Sheets (parts of a whole)
1. Put the categories in column A and the totals in column B.
2. Highlight both columns, including the headers.
3. Click Insert -> Chart.
4. In the Chart editor (Setup tab), set Chart type to Pie chart.
5. Add a chart title (Customize -> Chart and axis titles).
6. Turn on slice labels or percent labels (Customize -> Pie chart -> Slice label).

![Google Sheets screenshot placeholder: Pie chart setup](images/sheets_pie_setup_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

### Multiple Trials in Google Sheets (overlay, average, and error bars)
1. Put time in column A and each trial in its own column (B, C, D, etc.).
2. Highlight the whole table, including headers.
3. Click Insert -> Chart.
4. Choose Line chart to overlay all trials.
5. To add an average line, create a new column called \"Average\" and use AVERAGE for each row, then include that column in the chart.
6. To add error bars, click the average series in the chart, then Customize -> Series -> Error bars.
7. Make the average line darker and the trials lighter so the average stands out.

![Google Sheets screenshot placeholder: Series error bars](images/sheets_error_bars_placeholder.png)

Placeholder image: replace with a real Google Sheets screenshot if available.

**If you get stuck**
- The chart picked the wrong axis: use "Switch rows/columns" in the Setup tab.
- Values treated as text: remove extra spaces and set the column format to "Number."
- Trendline missing: confirm the chart type is Scatter.
- Histogram looks too spiky or too flat: adjust the bucket size.
- A series is missing: expand the data range or use \"Add series\" in Setup.
- Error bars not showing: select the average series and turn on error bars in Customize.