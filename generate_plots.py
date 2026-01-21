import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUTPUT_DIR = "images"


def save_fig(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)

def save_placeholder(title, filename):
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(Rectangle((0.02, 0.02), 0.96, 0.96, fill=False, linewidth=2, edgecolor="#999999"))
    ax.text(0.5, 0.62, title, ha="center", va="center", fontsize=12)
    ax.text(
        0.5,
        0.35,
        "Replace with Google Sheets screenshot",
        ha="center",
        va="center",
        fontsize=9,
        color="#555555",
    )
    save_fig(fig, filename)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
    })

    # Scatter plot (good): Fertilizer amount vs plant height
    fertilizer_g = np.array([0, 2, 4, 6, 8, 10])
    height_cm = np.array([12, 14, 17, 20, 22, 24])

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.scatter(fertilizer_g, height_cm, color="#2a6fbb")
    m, b = np.polyfit(fertilizer_g, height_cm, 1)
    x_line = np.linspace(fertilizer_g.min(), fertilizer_g.max(), 100)
    ax.plot(x_line, m * x_line + b, color="#f39c12", linewidth=2)
    ax.set_title("Plant height vs fertilizer amount")
    ax.set_xlabel("Fertilizer amount (g)")
    ax.set_ylabel("Plant height (cm)")
    save_fig(fig, "scatter_good_fertilizer_vs_height.png")

    # Scatter plot (bad): Same data, chopped y-axis and missing labels
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.scatter(fertilizer_g, height_cm, color="#2a6fbb")
    ax.set_title("Plant height vs fertilizer amount")
    ax.set_ylim(16, 24)  # Chopped axis exaggerates the trend
    # Intentionally omit axis labels and units
    save_fig(fig, "scatter_bad_chopped_axis.png")

    # Line graph (good): Temperature over time while cooling
    time_min = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    temp_c = np.array([85, 80, 76, 72, 69, 66, 63, 61, 59, 58, 57])

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.plot(time_min, temp_c, marker="o", color="#2ca02c")
    ax.set_title("Cooling water over time")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Temperature (C)")
    save_fig(fig, "line_good_cooling.png")

    # Line graph (bad): Same data, chopped axis and missing labels
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.plot(time_min, temp_c, marker="o", color="#2ca02c")
    ax.set_title("Temperature changes during cooling")
    ax.set_ylim(60, 85)  # Cropped axis exaggerates changes
    # Intentionally omit axis labels and units
    save_fig(fig, "line_bad_chopped_axis.png")

    # Multiple time series: three cooling trials (good overlay)
    trial_1 = temp_c
    trial_2 = temp_c + np.array([1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1])
    trial_3 = temp_c + np.array([-1, -1, 0, 1, 0, 1, 0, -1, 0, 0, 1])
    trials = np.vstack([trial_1, trial_2, trial_3])
    avg = trials.mean(axis=0)

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    for trial in trials:
        ax.plot(time_min, trial, color="#7f8c8d", alpha=0.5, linewidth=1.5)
    ax.plot(time_min, avg, color="#1f77b4", linewidth=2.5, label="Average")
    ax.set_title("Cooling water over time (3 trials)")
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Temperature (C)")
    ax.legend()
    save_fig(fig, "line_multi_overlaid_good.png")

    # Multiple time series: separate panels (good small multiples)
    fig, axes = plt.subplots(3, 1, figsize=(5.5, 6), sharex=True, sharey=True)
    for idx, ax in enumerate(axes, start=1):
        ax.plot(time_min, trials[idx - 1], marker="o", color="#2ca02c")
        ax.set_title(f"Trial {idx}")
        ax.set_ylabel("Temp (C)")
    axes[-1].set_xlabel("Time (min)")
    save_fig(fig, "line_multi_small_multiples_good.png")

    # Multiple time series (bad): too many bold lines and no labels
    rng = np.random.default_rng(7)
    clutter_trials = temp_c + rng.normal(0, 1.2, size=(8, time_min.size))
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    for trial in clutter_trials:
        ax.plot(time_min, trial, linewidth=2.0)
    ax.set_title("Cooling water over time (many trials)")
    # Intentionally omit axis labels and legend
    save_fig(fig, "line_multi_overlaid_bad_clutter.png")

    # Bar chart (good): Fertilizer type with a water-only control
    treatments = ["Water only", "Fertilizer A", "Fertilizer B", "Fertilizer C"]
    height_cm_treatments = [15.2, 19.1, 21.4, 18.3]

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.bar(treatments, height_cm_treatments, color="#1f77b4")
    ax.set_title("Average plant height by treatment")
    ax.set_xlabel("Treatment type")
    ax.set_ylabel("Plant height (cm)")
    save_fig(fig, "bar_good_fertilizer_treatments.png")

    # Bar chart (bad): Same data, y-axis does not start at zero
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.bar(treatments, height_cm_treatments, color="#e74c3c")
    ax.set_title("Average plant height by treatment")
    ax.set_xlabel("Treatment type")
    ax.set_ylabel("Plant height (cm)")
    ax.set_ylim(14, 22)  # Cropped axis exaggerates differences
    save_fig(fig, "bar_bad_fertilizer_treatments_chopped_axis.png")

    # Histogram (good): Distribution of toy car distance
    distances_cm = np.array([
        62, 64, 65, 66, 67, 68, 69, 70, 70, 71,
        72, 73, 74, 74, 75, 76, 77, 78, 78, 79,
        80, 81, 82, 83, 83, 84, 85, 86, 88, 90
    ])

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.hist(distances_cm, bins=6, color="#3498db", edgecolor="white")
    ax.set_title("Toy car distance distribution")
    ax.set_xlabel("Distance rolled (cm)")
    ax.set_ylabel("Number of trials")
    save_fig(fig, "hist_good_distribution.png")

    # Histogram (bad): Same data, too many bins and missing labels
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.hist(distances_cm, bins=20, color="#95a5a6", edgecolor="white")
    ax.set_title("Toy car distances (many tiny bins)")
    # Intentionally omit axis labels and units
    save_fig(fig, "hist_bad_too_many_bins.png")

    # Pie chart (good): parts of a whole
    litter_labels = ["Plastic", "Paper", "Metal", "Glass"]
    litter_counts = [40, 30, 20, 10]
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.pie(
        litter_counts,
        labels=litter_labels,
        autopct="%1.0f%%",
        startangle=90,
        colors=["#4c78a8", "#f58518", "#54a24b", "#e45756"],
    )
    ax.set_title("Litter types collected (percent of total)")
    save_fig(fig, "pie_good_litter_types.png")

    # Pie chart (bad): same data, no labels and exaggerated slice
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.pie(
        litter_counts,
        labels=None,
        startangle=90,
        shadow=True,
        explode=[0.12, 0, 0, 0],
        colors=["#cccccc", "#bdbdbd", "#d9d9d9", "#a6a6a6"],
    )
    ax.set_title("Litter types collected")
    save_fig(fig, "pie_bad_unlabeled_exploded.png")

    # Error bars (good): average with variability
    days = np.array([0, 2, 4, 6, 8, 10])
    mean_height = np.array([3.0, 4.5, 6.0, 7.4, 9.0, 10.5])
    std_height = np.array([0.4, 0.5, 0.6, 0.6, 0.7, 0.7])

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.errorbar(
        days,
        mean_height,
        yerr=std_height,
        marker="o",
        color="#1f77b4",
        capsize=4,
        linewidth=2,
    )
    ax.set_title("Seedling height over time (average of 5 trials)")
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Height (cm)")
    save_fig(fig, "line_errorbars_good.png")

    # Error bars (bad): same data, variability hidden and chopped axis
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    ax.plot(days, mean_height, marker="o", color="#1f77b4", linewidth=2)
    ax.set_title("Seedling height over time")
    ax.set_ylim(7.5, 11.0)  # Chopped axis exaggerates changes
    # Intentionally omit axis labels and error bars
    save_fig(fig, "line_errorbars_bad_hidden.png")

    # Google Sheets screenshot placeholders
    save_placeholder("Google Sheets\\nScatter chart setup", "sheets_scatter_setup_placeholder.png")
    save_placeholder("Google Sheets\\nLine chart setup", "sheets_line_setup_placeholder.png")
    save_placeholder("Google Sheets\\nColumn chart setup", "sheets_bar_setup_placeholder.png")
    save_placeholder("Google Sheets\\nHistogram setup", "sheets_histogram_setup_placeholder.png")
    save_placeholder("Google Sheets\\nPie chart setup", "sheets_pie_setup_placeholder.png")
    save_placeholder("Google Sheets\\nSeries error bars", "sheets_error_bars_placeholder.png")


if __name__ == "__main__":
    main()
