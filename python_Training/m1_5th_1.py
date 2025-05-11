import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data=np.random.rand(100)
labels=[ "class1" if x<=0.5 else "class2" for x in data[:50] ]

def euclidian_distance(x1,x2):
    return abs(x1-x2)

def knn_classifier(train_data,train_labels,test_point,k):
    distances=[(euclidian_distance(test_point,train_data[i]), train_labels[i]) for i in range(len(train_data))]
    distances.sort(key=lambda x: x[0])
    k_nearest_neighbors=distances[:k]
    k_nearest_labels=[label for _, label in k_nearest_neighbors]

    return Counter(k_nearest_labels).most_commom(1)[0][0]

train_data=data[:50]
train_labels=labels
test_data=data[50:]

k_values=[1,2,3,20,30]

print("K nearest neighbors classification")
print("Training Dataset")
print("Testing Dataset")

results={}
for k in k_values:
    print(f"Results for k = {k}: ")
    classified_label=[knn_classifier(train_data,train_labels,test_point,k) for test_point in test_data]
    results[k]=classified_label

    for i, label in enumerate(classified_label,start=51):
        print(f"Point x[i] (values({test_data[i-51]:.4f}) is classified as {label}")
        print("\n")
print("Classification Completed")

for k in k_values:
    clasified_labels=results[k]
    class_1=[test_data[i] for i in range(len(test_data)) if classified_label[i]=="class1"]
    class_2=[test_data[i] for i in range(len(test_data)) if classified_label[i]=="class2"]

                                       
    




