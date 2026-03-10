```markdown
# 📊 Pandas & Data Analysis Practice Repository

> A comprehensive collection of my data analysis practice using Python's most powerful libraries - Pandas, NumPy, Matplotlib, and Seaborn.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Latest-red.svg)

## 🎯 Project Overview

This repository showcases my journey in mastering data analysis with Python. I've practiced on **6+ real-world datasets** covering various domains including aviation, finance, wine quality, retail, and the famous Titanic dataset.



## 🚀 What I've Learned & Practiced

### 📌 1. Pandas Series Mastery
```python
✅ Creating Series from lists, dictionaries, and arrays
✅ Custom indexing and labeling
✅ Statistical operations (sum, mean, max, min, std)
✅ Data filtering with boolean indexing
✅ Series multiplication and transformation
✅ Using describe() for quick statistical summary
```

### 📌 2. Pandas DataFrame Operations
```python
✅ Creating DataFrames from dictionaries
✅ Loading data from CSV files
✅ Exploring data structure (shape, dtypes, columns, index)
✅ Advanced indexing with loc and iloc
✅ Conditional filtering and multi-condition queries
✅ Setting and resetting index
✅ Multi-level indexing
✅ Using isin() for categorical filtering
```

### 📌 3. Data Exploration Techniques
```python
✅ head() & tail() - Quick data preview
✅ sample() - Random data sampling
✅ shape - Dataset dimensions
✅ describe() - Statistical summary
✅ info() - Data types and memory usage
✅ unique() & nunique() - Unique value analysis
✅ value_counts() - Frequency distribution
✅ Handling missing values with isnull()
```

### 📌 4. Data Manipulation & Transformation
```python
✅ Sorting data with sort_values()
✅ Finding top/bottom records with nlargest() & nsmallest()
✅ Applying functions with apply()
✅ Custom labeling with conditional logic
✅ String manipulation (converting to uppercase)
✅ Creating new calculated columns
✅ Filling missing values with fillna()
✅ Duplicate detection with duplicated()
```

### 📌 5. Advanced Analytics
```python
✅ GroupBy operations for aggregated analysis
✅ Multi-condition filtering with & operator
✅ Statistical measures (mean, median, percentile)
✅ Mathematical operations (sqrt, log)
✅ Finding maximum value index with idxmax()
✅ Survival rate analysis
✅ Gender-based statistical comparison
```

### 📌 6. Data Visualization
```python
✅ Histograms with KDE (Kernel Density Estimation)
✅ Count plots for categorical data
✅ Box plots for distribution analysis
✅ Scatter plots for correlation visualization
✅ Using Seaborn for beautiful statistical plots
✅ Matplotlib integration
```



## 📁 Datasets Analyzed

### 1. ✈️ Airline Ticket Prices Dataset
**Analysis Performed:**
- Price distribution analysis
- Airline and Class categorization
- Custom price labeling (High/Middle/Low)
- Largest and smallest ticket prices
- Statistical summary of pricing

**Key Insights:**
- Applied conditional logic to categorize prices
- Identified pricing patterns across different airlines
- Converted airline names to uppercase for standardization

---

### 2. 🍷 Wine Quality Dataset
**Analysis Performed:**
- Quality rating distribution
- Alcohol content analysis
- Filtering high-quality wines (quality > 6)
- Maximum quality identification

**Key Findings:**
- Calculated average alcohol percentage
- Identified characteristics of good wines
- Statistical correlation between features

---

### 3. 💰 Loan Dataset (20,000 records)
**Analysis Performed:**
- Missing value detection
- Monthly income statistics
- Loan approval rate analysis
- Paid vs. Unpaid loan comparison

**Key Metrics:**
- Total approved loans count
- Average monthly income of borrowers
- Null value handling

---

### 4. 🛒 Superstore Sales Dataset
**Analysis Performed:**
- Total sales calculation
- Average sales computation
- Highest sales transaction identification
- High-value sales filtering (>$1000)

**Business Insights:**
- Identified top-performing transactions
- Analyzed sales distribution patterns

---

### 5. 🚢 Titanic Survival Dataset
**Analysis Performed:**
- Survival rate analysis
- Gender-based survival comparison
- Age distribution analysis
- Female survivor identification
- Multi-condition filtering (age, gender, survival)

**Statistical Findings:**
- Average age of passengers
- Survival count distribution
- Gender-wise survival rates
- Female passengers with age > 30 analysis

---

### 6. 🏠 Housing Prices Dataset
**Analysis Performed:**
- Price statistics (mean, max, min, std)
- Bedroom count analysis
- Multi-condition property filtering
- Price distribution sorting
- Missing value treatment
- Duplicate record detection
- Percentile calculations
- Logarithmic transformations

**Advanced Techniques:**
- Combined price and bedroom filters
- Statistical percentile analysis (25th percentile)
- Data cleaning operations

---

## 🛠️ Technologies & Libraries Used

| Library | Purpose | Skills Demonstrated |
|---------|---------|---------------------|
| **Pandas** | Data manipulation | DataFrame operations, Series handling, CSV reading, data filtering |
| **NumPy** | Numerical computing | Statistical calculations, mathematical operations, array handling |
| **Matplotlib** | Visualization | Plot creation, data representation |
| **Seaborn** | Statistical visualization | Histplot, countplot, boxplot, scatterplot with styling |

---

##  Key Skills Demonstrated

### Data Cleaning
- ✅ Handling missing values
- ✅ Duplicate detection and removal
- ✅ Data type conversions
- ✅ String standardization

### Statistical Analysis
- ✅ Descriptive statistics
- ✅ Distribution analysis
- ✅ Percentile calculations
- ✅ Correlation identification

### Data Filtering
- ✅ Boolean indexing
- ✅ Multi-condition queries
- ✅ Categorical filtering
- ✅ Range-based selection

### Data Transformation
- ✅ Custom function application
- ✅ Column creation
- ✅ Mathematical transformations
- ✅ Conditional labeling

---

## 📊 Visualization Examples

### 1. Age Distribution (Histogram with KDE)
```python
sns.histplot(df["Age"], kde=True)
```
**Purpose:** Understanding passenger age distribution in Titanic dataset

### 2. Survival Count (Count Plot)
```python
sns.countplot(x="Survived", data=df)
```
**Purpose:** Visualizing survival statistics

### 3. Age by Class (Box Plot)
```python
sns.boxplot(x="Pclass", y="Age", data=df)
```
**Purpose:** Comparing age distribution across passenger classes

### 4. Age vs Fare (Scatter Plot)
```python
sns.scatterplot(x="Age", y="Fare", data=df)
```
**Purpose:** Identifying correlation between age and ticket fare

---

## 🎓 Learning Outcomes

Through this practice repository, I have developed:

1. **Strong Foundation in Pandas**
   - Confident in DataFrame and Series operations
   - Skilled in data exploration techniques
   - Proficient in data filtering and selection

2. **Data Analysis Expertise**
   - Can perform comprehensive statistical analysis
   - Able to extract meaningful insights from data
   - Experienced with real-world datasets

3. **Visualization Skills**
   - Create informative statistical plots
   - Use appropriate visualization for different data types
   - Combine multiple visualization libraries

4. **Problem-Solving Ability**
   - Handle missing and duplicate data
   - Apply conditional logic for data categorization
   - Perform multi-step data transformations

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pandas-practice.git
cd pandas-practice

# Install required libraries
pip install pandas numpy matplotlib seaborn

# Run the practice script
python practice.py
```

### Requirements
```txt
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

---

## 📝 Code Structure

```
pandas-practice/
│
├── practice.py          # Main practice file with all code
├── README.md           # This file
├── requirements.txt    # Python dependencies
│
└── datasets/          
    ├── airline_ticket_prices_dataset.csv
    ├── winequalityN.csv
    ├── loan_dataset_20000.csv
    ├── train.csv (Superstore)
    ├── tested.csv (Titanic)
    └── data.csv (Housing)
```

---

## 🎯 Next Steps & Future Improvements

- [ ] Convert code to Jupyter Notebooks for better documentation
- [ ] Add more visualization examples
- [ ] Implement machine learning models on these datasets
- [ ] Create interactive dashboards with Plotly
- [ ] Add data preprocessing pipelines
- [ ] Document insights in separate markdown files
- [ ] Add unit tests for data validation

---

## 📈 Practice Statistics

| Metric | Count |
|--------|-------|
| Datasets Analyzed | 6 |
| Lines of Code | 200+ |
| Pandas Functions Used | 50+ |
| Visualization Types | 4 |
| Statistical Operations | 15+ |
| Data Cleaning Techniques | 5+ |

---

## 🤝 Contributing

This is a personal learning repository, but suggestions are welcome! Feel free to:
- Open issues for improvements
- Suggest new datasets to analyze
- Recommend better practices

---

## 📧 Contact

**Your Name**
- GitHub: [@jawad-hua](https://github.com/jawad-hua)
- LinkedIn: [M0jawad](https://linkedin.com/in/M0jawad)
- Email: jawadmjawad06@example.com

---

## ⭐ Acknowledgments

- Thanks to the open data community for providing datasets
- Pandas documentation for excellent guides
- Seaborn library for beautiful visualizations

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

### ⭐ If you found this helpful, please give it a star!

**Happy Data Analyzing! 📊🐼**

Made with ❤️ and Python

</div>
```

---

