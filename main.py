import streamlit as st
import plotly.express as px


from backend import get_data

# Add title, text input and widgets
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get the data
    try :
        filtered_data = get_data(place, days, option)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # plot
            figure = px.line(x = dates, y = temperatures, labels={"x": "Date", "y":"Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            Sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            images = {"Clear":"images/clear.png",
                      "Clouds":"images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            st.image([images[condition] for condition in Sky_conditions],caption=dates width=115)
    except KeyError:
        st.write("That place does not exists.")
