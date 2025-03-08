import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select Conversion Category", ["Length", "Temperature"])
    
    value = st.number_input("Enter Value", value=0.0, format="%f")
    
    if category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"]
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        result = convert_length(value, from_unit, to_unit)
    else:
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
        result = convert_temperature(value, from_unit, to_unit)

    # **Display the conversion result**
    st.write(f"### Converted Value: {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
