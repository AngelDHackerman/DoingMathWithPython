# Este pipeline asegura que los datos sean consistentes y preparados adecuadamente antes de cualquier análisis o modelado, 
# proporcionando un flujo de trabajo estructurado y repetible.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA

# Supongamos que tenemos un DataFrame 'df' con datos numéricos y categóricos
df = "fictional_data_set_here"

# Definimos las columnas numéricas y categóricas
numeric_features = ['age', 'income', 'score']
categorical_features = ['gender', 'country']

# Pipelines para preprocesar características numéricas y categóricas
numeric_transformer = Pipeline(steps=[
  ('imputer', SimpleImputer(strategy='mean')),
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

# Pipeline completo con preprocesamiento y PCA
pipeline = Pipeline(steps=[
  ('preprocessor', preprocessor),
  ('pca', PCA(n_components=2))
])

# Ajustamos el pipeline a los datos
pipeline.fit(df)

# Transformamos los datos
processed_data = pipeline.transform(df)
