# Reproduce the churn model and metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
df=pd.read_csv("data/customer_churn.csv")
X=df.drop(columns=["CustomerID","Churn"]); y=df["Churn"]
cat=X.select_dtypes(include="object").columns.tolist(); num=X.select_dtypes(exclude="object").columns.tolist()
prep=ColumnTransformer([("cat",OneHotEncoder(handle_unknown="ignore"),cat),("num",StandardScaler(),num)])
model=Pipeline([("prep",prep),("rf",RandomForestClassifier(n_estimators=250,max_depth=8,class_weight="balanced",random_state=42))])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model.fit(X_train,y_train); pred=model.predict(X_test); proba=model.predict_proba(X_test)[:,1]
print("Accuracy:",accuracy_score(y_test,pred))
print("Precision:",precision_score(y_test,pred,zero_division=0))
print("Recall:",recall_score(y_test,pred,zero_division=0))
print("F1:",f1_score(y_test,pred,zero_division=0))
print("ROC-AUC:",roc_auc_score(y_test,proba))
