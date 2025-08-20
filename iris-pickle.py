import requests
import pickle


"""
import the iris data set using requests module and pickling it usin pickle module

"""

def pickle_iris():

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    response = requests.get(url)

    data = response.text

    l1 = data.split("\n")
    # print(l1)

    l2 = [item.split(",") for item in l1]
    # print(l2)

    with open("my-iris.pkl", "wb") as f:
        pickle.dump(l2,f)


# to read the pickle module

def de_pickle():
    with open ("my-iris.pkl", "rb") as f:
        print(pickle.load(f))

if __name__ == "__main__":
    print("\nIf want to picke iris data set press 1\nTo de-pickle press 2\n")

    if input("Enter Your Choose: ") == "1":
        pickle_iris()
    else:
        de_pickle()