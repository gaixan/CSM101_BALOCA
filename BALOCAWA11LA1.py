Machinelearning = [
    ("Supervised", "Decision Tree"),
    ("Supervised", "Random Forest"),
    ("Unsupervised", "K-means"),
    ("Unsupervised", "Gaussian Mixture Model")
]
print("\nLearning Type:", Machinelearning[0][0])
for item in Machinelearning:
    if item[0] == "Supervised":
        print(item[1])
print("\nLearning Type:", Machinelearning[2][0])
for item in Machinelearning:
    if item[0] == "Unsupervised":
        print(item[1])
