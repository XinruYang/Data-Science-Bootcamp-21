    if submenu == "gdp per capita":
        st.plotly_chart(scatter_geo(covid_groupby, "gdp_per_capita", "gdp per capita", 
        color="gdp_per_capita", size_max=15), use_container_width=True )
    
    if submenu == "Poverty %":
        st.plotly_chart(scatter_geo(covid_groupby, "Poverty %", "Poverty ratio",
         color="Poverty %"),  use_container_width=True )

    if submenu == "total cases":
        st.plotly_chart(scatter_geo(covid_groupby, "total_cases", "total cases", 
        color="total_cases") , use_container_width=True)

    if submenu == "total deaths":
        st.plotly_chart(scatter_geo(covid_groupby, "total_deaths", "total deaths",
            color="total_deaths"), use_container_width=True)

    if submenu == "deaths ratio":
        st.plotly_chart(scatter_geo(covid_groupby, "deaths_ratio", "deaths ratio",
            color="deaths_ratio"), use_container_width=True)
