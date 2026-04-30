🏥 Emergency Department Synthetic Dataset
A fully synthetic, privacy-safe emergency department dataset designed for data science education, EDA practice, healthcare analytics prototyping, and ML model development.
⚠️ All data in this project is synthetically generated. It does not represent real patients, real events, or any real healthcare institution.
📁 Project Structure
.
├── data/
│   └── ed_synthetic_dataset.csv   # Synthetic ED patient records
├── notebooks/
│   └── eda.ipynb                  # Exploratory Data Analysis notebook
├── generator/
│   └── generate_data.py           # Script to regenerate the dataset
├── README.md
└── requirements.txt
📊 Dataset Overview
The dataset simulates a realistic emergency department workflow and includes fields such as:
Column	Description
patient_id	Unique synthetic patient identifier
arrival_time	Timestamp of ED arrival
triage_level	Acuity score (e.g., ESI 1–5)
chief_complaint	Presenting symptom or reason for visit
age / sex	Demographic attributes
disposition	Outcome (admitted, discharged, transferred, etc.)
length_of_stay_hrs	Total time spent in the ED
diagnosis_code	Synthetic ICD-10-like code
Column availability may vary depending on the version of the dataset generated.
🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/ed-synthetic-dataset.git
cd ed-synthetic-dataset
2. Install dependencies
pip install -r requirements.txt
3. (Optional) Regenerate the dataset
python generator/generate_data.py
4. Explore the data
Open the EDA notebook:
jupyter notebook notebooks/eda.ipynb
🔍 EDA Highlights
The eda.ipynb notebook covers:
Patient volume trends by hour, day, and month
Triage level distribution
Top chief complaints
Length of stay analysis by disposition and acuity
Missing data assessment
🛠️ Requirements
Python 3.8+
pandas
numpy
matplotlib / seaborn
jupyter
Install all at once:
pip install -r requirements.txt
📄 License
This project is licensed under the MIT License.
🙏 Acknowledgements
Inspired by real-world ED workflows and designed to support learning in healthcare data science without compromising patient privacy.
