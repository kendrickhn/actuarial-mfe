# Used Car Price Prediction: EDA + Baseline Model

This project is part of my data science portfolio, aiming to predict the **selling price** of used cars based on key features like mileage, engine size, brand, and more. The goal is to support smarter car buying decisions and pricing strategies using data.
--
## Dataset

The data comes from a Kaggle competition and includes:

- `train.csv`: historical car sales with features and selling price
- `test.csv`: features only (no price)
- `sample.csv`: template for competition submission
--
## Project Structure

- `notebooks/used_car_model.ipynb`: full exploration + baseline modeling
- `data/`: raw training, test and sample submission files
- `INSIGHT.md`: business insights and recommendations
- `README.md`: project overview (this file)

## Key Steps

1. **Data Cleaning & Feature Engineering**
   - Converted units (e.g. `mileage`, `engine`, `bhp`)
   - Extracted new features like `car_age`, `brand`, `is_automatic`, etc.
   - Imputed missing values

2. **Exploratory Data Analysis (EDA)**
   - Visualized feature distributions and correlations
   - Analyzed top predictors and high-price outliers

3. **Modeling**
   - Trained a baseline Linear Regression model
   - Evaluated performance using MAE & RMSE
   - Visualized feature importance
--
## Performance

| Metric       | Value             |
|--------------|-------------------|
| MAE          | 172,060.51        |
| MSE          | 105,478,156,675.32|
--
## Example Visuals



## Next Steps

- Try tree-based models (Random Forest, XGBoost)
- Add brand-level pricing insight
- Deploy via Streamlit

## Connect

- GitHub: [@kendrickhn](https://github.com/kendrickhn)
- Kaggle: [@kendrickhn](https://www.kaggle.com/kendrickdhnguyen)

---

## Why This Project?

Used cars are a major purchase — this project demonstrates how data science can help consumers and dealerships understand market trends and fair pricing, while showcasing my technical skills in:

- Data cleaning & wrangling
- Feature engineering
- Regression modeling
- Visualization & storytelling
