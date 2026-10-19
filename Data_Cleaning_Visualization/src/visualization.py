
import pandas as pd
import matplotlib.pyplot as plt
import os

# Find the project folder
project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Load the cleaned dataset
file_path = os.path.join(
    project_folder,
    "cleaned_data",
    "cleaned_dataset.csv"
)

df = pd.read_csv(file_path)

# Display available numerical columns
numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

print("Numerical columns:", numeric_columns)

# Create a chart if numerical data exists
if numeric_columns:
    column = numeric_columns[0]

    plt.figure(figsize=(10, 5))
    plt.hist(df[column].dropna(), bins=20)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()

    # Save the chart
    output_folder = os.path.join(
        project_folder, "visualizations"
    )
    os.makedirs(output_folder, exist_ok=True)

    chart_path = os.path.join(
        output_folder, "distribution_chart.png"
    )

    plt.savefig(chart_path)
    print("Chart saved at:", chart_path)

    plt.show()
else:
    print("No numerical columns found in the dataset.")

# Step 12: Create additional visualizations

# Bar chart for the first numerical column
if numeric_columns:
    column = numeric_columns[0]

    plt.figure(figsize=(10, 5))
    df[column].dropna().head(10).plot(kind="bar")

    plt.title(f"First 10 Values of {column}")
    plt.xlabel("Record")
    plt.ylabel(column)
    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "bar_chart.png")
    )
    plt.show()


# Correlation heatmap for numerical columns
if len(numeric_columns) >= 2:
    correlation = df[numeric_columns].corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(correlation, cmap="coolwarm", aspect="auto")
    plt.colorbar()

    plt.xticks(
        range(len(numeric_columns)),
        numeric_columns,
        rotation=45,
        ha="right"
    )
    plt.yticks(range(len(numeric_columns)), numeric_columns)

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "correlation_heatmap.png")
    )
    plt.show()

print("Additional visualizations completed!")