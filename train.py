import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# ===============================
# LOAD DATASET DENGAN AUTO DETEK
# ===============================
try:
    df = pd.read_excel("kc_house_data.xlsx")
except:
    df = pd.read_csv("kc_house_data.xlsx")

# ===============================
# Jika semua kolom tergabung jadi satu, split paksa
# ===============================
if len(df.columns) == 1:
    df = df.iloc[:,0].str.split(',', expand=True)
    df.columns = ['id','date','price','bedrooms','bathrooms','sqft_living','sqft_lot',
                  'floors','waterfront','view','condition','grade','sqft_above','sqft_basement',
                  'yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']

# ===============================
# NORMALISASI NAMA KOLOM
# ===============================
df.columns = df.columns.str.lower().str.replace(" ", "_")

# ===============================
# PILIH FITUR & TARGET
# ===============================
features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors']

# Hapus tanda kutip & strip whitespace lalu convert ke float
for col in features + ['price']:
    df[col] = df[col].astype(str).str.replace('"','').str.strip()
    df[col] = df[col].astype(float)

X = df[features]
y = df['price']

# ===============================
# SPLIT DATA
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# TRAIN MODEL
# ===============================
model = LinearRegression()
model.fit(X_train, y_train)

# ===============================
# SIMPAN MODEL
# ===============================
joblib.dump(model, "house_price_model.pkl")

print("Model berhasil dilatih dan disimpan!")
