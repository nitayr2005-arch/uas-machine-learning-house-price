from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# ===============================
# CORS agar fetch aman
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ===============================
# Load model
# ===============================
model = joblib.load("house_price_model.pkl")

# ===============================
# Input schema
# ===============================
class HouseInput(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    floors: int

# ===============================
# Serve index.html manual
# ===============================
@app.get("/")
def serve_index():
    index_path = os.path.join(os.getcwd(), "index.html")
    return FileResponse(index_path)

# ===============================
# Endpoint prediksi
# ===============================
@app.post("/predict")
def predict(data: HouseInput):
    try:
        # Debug: lihat input di console
        print("Data diterima:", data)

        # Siapkan features untuk model
        features = np.array([[
            data.bedrooms,
            data.bathrooms,
            data.sqft_living,
            data.floors
        ]])

        # Prediksi harga
        prediction = model.predict(features)[0]

        # Debug: lihat prediksi di console
        print("Prediksi:", prediction)

        return {"predicted_price": round(prediction, 2)}

    except Exception as e:
        # Kalau error, tampilkan pesan
        print("ERROR:", e)
        return {"predicted_price": None, "error": str(e)}
