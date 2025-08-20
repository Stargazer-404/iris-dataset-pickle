# iris-dataset-pickle
Used pickle module to pickle iris dataset


📌 README.md (for GitHub)
# Iris Dataset Pickle Project
This is a simple Python project that:
1. Downloads the [Iris dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) from the UCI Machine Learning Repository.
2. Saves (pickles) the dataset to a local file.
3. Allows you to load (de-pickle) the dataset later and view sample rows.

---

## 📂 Project Structure
├── iris_pickle.py # Main script with pickle & de-pickle functions <br>
├── my-iris.pkl # Pickled dataset (generated after running)<br>
└── README.md # Project documentation<br>

## ⚙️ Requirements

- Python 3.7+
- Required libraries:
  - `requests`
  - `pickle` (built-in)
  - `os` (built-in)




## 🚀 Usage
Run the script:<br>
python iris_pickle.py<br>

You’ll see a menu:<br>
Options:<br>
1. Pickle Iris dataset<br>
2. De-pickle and view<br>

## 1️⃣ Pickle the dataset
•	Downloads the Iris dataset from UCI<br>
•	Stores it as my-iris.pkl<br>
Enter your choice (1/2): 1<br>
Output:<br>
Iris dataset has been pickled into my-iris.pkl<br>

## 2️⃣ De-pickle and view data
•	Loads the dataset back into memory<br>
•	Displays how many rows and the first 5 rows<br>
Enter your choice (1/2): 2<br>
Loaded 150 rows from my-iris.<br>
['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']<br>
['4.9', '3.0', '1.4', '0.2', 'Iris-setosa']<br>
...<br>

## 📊 Example Output
Options:<br>
1. Pickle Iris dataset<br>
2. De-pickle and view<br>

Enter your choice (1/2): 2<br>
Loaded 150 rows from my-iris.pkl<br>
['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']<br>
['4.9', '3.0', '1.4', '0.2', 'Iris-setosa']<br>
['4.7', '3.2', '1.3', '0.2', 'Iris-setosa']<br>
['4.6', '3.1', '1.5', '0.2', 'Iris-setosa']<br>
['5.0', '3.6', '1.4', '0.2', 'Iris-setosa']<br>

## 📝 Notes
•	The dataset has 150 rows and 5 columns:<br>
o	Sepal length<br>
o	Sepal width<br>
o	Petal length<br>
o	Petal width<br>
o	Class (species)<br>
•	If you try to de-pickle before pickling, it will warn you to pickle first.<br>

