
        input_values = {
            "Start_Lat": latitude,
            "Start_Lng": longitude,
            "Distance(mi)": distance,
            "Temperature(F)": temperature,
            "Humidity(%)": humidity,
            "Pressure(in)": pressure,
            "Visibility(mi)": visibility,
            "Wind_Direction": wind_direction,
            "Wind_Speed(mph)": wind_speed,
            "Precipitation(in)": precipitation,
            "Weather_Condition": weather_condition,

            # Road features: default to False
            **{
                feature: "False"
                for feature in ROAD_FEATURES
            },

            
            "Sunrise_Sunset": category_options["Sunrise_Sunset"][
                category_options["Sunrise_Sunset"].index("Day")
            ] if "Day" in category_options["Sunrise_Sunset"]
            else category_options["Sunrise_Sunset"][0],

            "Start_Hour": start_time.hour,
            "Start_Month": start_date.month,
            "Start_DayOfWeek": start_date.weekday(),

            "Selected_Place": st.session_state["accident_place"],
        }

        submitted = st.form_submit_button(
            "✦  Predict severity",
            width="stretch",
        )
