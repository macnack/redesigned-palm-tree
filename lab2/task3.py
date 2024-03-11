from typing import Tuple

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

@profile
def get_train_test_data() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    X, y = load_iris(return_X_y=True)
    
    ##### TODO Student #####
    # Podziel dane na zbiór treningowy i testowy w stosunku 70%-30%

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    ########################
    
    return X_train, X_test, y_train, y_test


@profile
def main():    
    ##### TODO Student #####
    # Dokonaj inicjalizacji klasyfikatora z biblioteki scikit-learn
    
    clf = RandomForestClassifier()
    
    ########################
    
    X_train, X_test, y_train, y_test = get_train_test_data()
    
    ##### TODO Student #####
    
    # Wytrenuj klasyfikator z wykorzystaniem zbioru treningowego
    clf.fit(X_train, y_train)

    # Dokonaj ewaluacji na zbiorze testowym
    print(clf.score(X_test, y_test))
    # Wykonaj klasyfikację pojedynczej próbki ze zbioru testowego
    print("Single prediction")
    for _ in range(100):
        clf.predict(X_test[0].reshape(1, -1))
    
    # Wykonaj klasyfikację dla grupy 16 próbek ze zbioru testowego (ang. batch prediction)
    print("Batch prediction")
    for _ in range(100):
        clf.predict(X_test[:16])
    
    ########################
    
    
if __name__ == '__main__':
    main()