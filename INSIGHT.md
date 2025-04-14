# 🔍 Used Car Pricing Insights

This document captures the key insights, business takeaways, and recommendations generated from the `used_car_model.ipynb` notebook. The purpose is to translate raw analysis and model output into meaningful, actionable points for potential car buyers, sellers, or pricing systems.

---

## I. Top Influential Features

| Feature        | Impact on Price |
|----------------|------------------|
| `engine`       | Strong positive correlation with price |
| `max_power`    | Generally increases price (but plateaus at high levels) |
| `car_age`      | Older cars → significantly lower resale price |
| `km_driven`    | Negatively correlated with price |
| `is_automatic` | Automatic cars tend to be priced higher |

**Observation:**  
Technical specifications like engine size and horsepower play a critical role in pricing, followed by age and mileage. Transmission type also introduces variance.

---

## II. Data Highlights

### 1. Missing Values
- Imputed using mean strategy
- Columns affected: `mileage`, `engine`, `max_power`, `seats`

### 2. Outliers
- A few cars had unrealistic prices (10M+) and horsepower (>400 bhp)
- These will require handling in future model iterations

---

## III. Model Performance

| Metric            | Value (Baseline) |
|-------------------|------------------|
| MAE (Mean Abs. Error)  | *to be updated*     |
| RMSE (Root Mean Sq. Err)| *to be updated*     |

**Baseline Model:** Linear Regression  
Used for simplicity and interpretation. Next steps involve trying advanced models like XGBoost or Random Forests.

---

## IV. Key Recommendations

- **Age-sensitive Pricing:** Strong decline in value after year 5 suggests opportunity for depreciation-based pricing models.
- **Transmission Type Adjustment:** Automatics command a premium — worth factoring into automated pricing.
- **Branding Effect:** Preliminary analysis shows some brands (e.g. Toyota, Honda) maintain higher resale values.

---

## V. Next Steps

- Improve performance using tree-based models
- Perform brand-wise analysis (e.g., Toyota vs Hyundai)
- Apply log transformation to price
- Deploy to Streamlit for demo / interactivity

---

Let me know if you’d like to explore segment-level breakdowns or deploy this project to the web!
