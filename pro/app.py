import pickle
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures

# 1. DEFINE THE CLASS FIRST
class FullFeaturePreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, selective_ccolumns, poly_features_cols, degree=2):
        self.selective_ccolumns = selective_ccolumns
        self.poly_features_cols = poly_features_cols
        self.degree = degree
        self.label_encoders = {}
        self.poly = PolynomialFeatures(degree=self.degree, include_bias=False)

    def fit(self, X, y=None):
        X_copy = X.copy()
        for col in self.selective_ccolumns:
            if col in X_copy.columns:
                le = LabelEncoder()
                le.fit(X_copy[col])
                self.label_encoders[col] = le
        for col, le in self.label_encoders.items():
            X_copy[col] = le.transform(X_copy[col])
        if not all(col in X_copy.columns for col in self.poly_features_cols):
            raise ValueError(f"Polynomial feature columns {self.poly_features_cols} not all found in input for PolynomialFeatures.")
        self.poly.fit(X_copy[self.poly_features_cols])
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for col, le in self.label_encoders.items():
            if col in X_copy.columns:
                X_copy[col] = le.transform(X_copy[col])
            else:
                X_copy[col] = -1
        if not all(col in X_copy.columns for col in self.poly_features_cols):
            raise ValueError(f"Missing columns for polynomial transformation: {self.poly_features_cols}.")
        poly_features_data = self.poly.transform(X_copy[self.poly_features_cols])
        poly_feature_names = self.poly.get_feature_names_out(X_copy[self.poly_features_cols].columns)
        poly_df = pd.DataFrame(poly_features_data, columns=poly_feature_names, index=X_copy.index)
        new_poly_columns = [col for col in poly_feature_names if col not in X_copy.columns]
        X_copy = pd.concat([X_copy, poly_df[new_poly_columns]], axis=1)
        X_copy['area_per_bedroom'] = X_copy['area'] / X_copy['bedrooms'].replace(0, 1)
        X_copy['bathrooms_per_bedroom'] = X_copy['bathrooms'] / X_copy['bedrooms'].replace(0, 1)
        return X_copy

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_price(area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, 
                  hotwaterheating, airconditioning, parking, prefarea, furnishingstatus):
    
    # Create the input DataFrame
    data = pd.DataFrame([[area, bedrooms, bathrooms, stories, mainroad, guestroom, 
                          basement, hotwaterheating, airconditioning, parking, 
                          prefarea, furnishingstatus]], 
                        columns=['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
                                 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 
                                 'parking', 'prefarea', 'furnishingstatus'])
    
    log_prediction = model.predict(data)

    final_price = np.expm1(log_prediction[0])
    
    return f"${final_price:,.2f}"