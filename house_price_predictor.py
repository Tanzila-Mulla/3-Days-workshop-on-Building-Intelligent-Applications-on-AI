
# House Price Prediction with Linear Regression and Visualization
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")
st.title("🏠 House Price Predictor")
st.markdown("""
<style>
.main {background: linear-gradient(120deg, #fbc2eb 0%, #a6c1ee 100%);}
.stButton>button {background: #6a11cb; color: white; border-radius: 8px; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.write("Enter the area (in square feet) to predict the house price using a simple linear regression model.")

# Example training data (area in sqft, price in $1000s)
areas = np.array([500, 750, 1000, 1250, 1500, 1750, 2000]).reshape(-1, 1)
prices = np.array([50, 75, 100, 120, 150, 170, 200])

# Train the model
model = LinearRegression()
model.fit(areas, prices)

# User input
st.subheader("🔢 Enter Area for Prediction")
user_area = st.number_input("Area (sqft):", min_value=100, max_value=10000, value=1000)

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("Predict Price"):
        predicted_price = model.predict(np.array([[user_area]]))[0]
        st.success(f"Predicted House Price: ${predicted_price * 1000:,.2f}")
        st.info("This is a prediction based on a simple linear regression model.")

with col2:
    # Plotting
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.scatter(areas, prices, color='blue', label='Training Data')
    ax.plot(areas, model.predict(areas), color='red', linewidth=2, label='Regression Line')
    ax.scatter([user_area], model.predict(np.array([[user_area]])), color='green', s=100, label='Your Prediction')
    ax.set_xlabel('Area (sqft)')
    ax.set_ylabel('Price ($1000s)')
    ax.set_title('House Price vs Area')
    ax.legend()
    st.pyplot(fig)

st.markdown("---")
st.write("**Note:** This is a demo using sample data. For real-world use, train with actual market data.")
st.caption("Made with Streamlit and scikit-learn | Linear Regression Visualization Included")
