from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, FunctionTransformer, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd

# Datos de ejemplo
data = {
    'age': [25, np.nan, 35, 40, 23],
    'income': [50000, 60000, np.nan, 100000, 30000],
    'gender': ['male', 'female', 'female', 'male', 'male'],
    'country': ['US', 'Canada', 'US', 'US', 'Canada']
}
df = pd.DataFrame(data)

# Definimos las columnas numéricas y categóricas
numeric_features = ['age', 'income']
categorical_features = ['gender', 'country']

# Pipelines para preprocesar características numéricas y categóricas
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('log_transform', FunctionTransformer(np.log1p, validate=True)),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinamos los transformadores en un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Pipeline completo con preprocesamiento y una transformación polinómica
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('poly', PolynomialFeatures(degree=2))
])

# Ajustamos el pipeline a los datos
pipeline.fit(df)

# Transformamos los datos
processed_data = pipeline.transform(df)

print(processed_data)
