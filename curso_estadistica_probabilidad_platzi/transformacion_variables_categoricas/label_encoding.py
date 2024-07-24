# Asigna un número único a cada categoría.

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
encoded_labels = encoder.fit_transform(['red', 'blue', 'green'])
