import requests
import pickle
import os

def pickle_iris(filename="my-iris.pkl"):

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    
    response = requests.get(url) 

    if response.status_code != 200: # check request is valid or not
        print("Failed to download dataset.")
        return
    
    data = response.text.strip() # strip trailing space
    rows = [row.split(",") for row in data.split("\n") if row]
    
    with open(filename,"wb") as f: # 
        pickle.dump(rows,f)
    
    print(f"Iris data set has been pickled into {filename}")


def de_pickle(filename="my-iris.pkl"):
    
    if not os.path.exists(filename): # checking if we already have a pickle file o not
        print(f"File '{filename}' not found! Please pickle first")
        return
    
    with open(filename,"rb") as f:
        data = pickle.load(f)

    print(f"Loaded {len(data)} rows from {filename}") # print hte len of data pickles 
    for row in data[:5]:
        print(row)

if __name__ == "__main__":
    print("\nOptions:\n1. Pickle Iris dataset\n2. De-pickle and view\n")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        pickle_iris()
    elif choice == "2":
        de_pickle()
    else:
        print("Invalid choice! Please enter 1 or 2.")

    