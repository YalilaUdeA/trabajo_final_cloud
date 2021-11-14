from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

if __name__ == "__main__":
    wine = datasets.load_wine()

    #Datasets: Prep
    x=wine.data
    y=wine.target

    #Train and test data
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3)

    #ML Model: Model Selection
    rf=RandomForestClassifier()
    rf.fit(x_train, y_train)

    #Predictions
    predictions=rf.predict(x_test)

    #Accuracy
    print(accuracy_score(y_test,predictions))

    #Registro
    with open('./outputs/wine_model.pkl', 'wb') as model_pkl:
        pickle.dump(rf, model_pkl)
    