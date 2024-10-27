import streamlit as st

def simulation_page():
    st.subheader("Simulation Page")
    st.write("Select a simulation to view:")
    st.markdown("""The Simulations page provides various simulation from Phet, which are a great tool to help build foundational knowledge.""")
    simulations = [
        ("Gene Expression Essentials", """
            <iframe src="https://phet.colorado.edu/sims/html/gene-expression-essentials/latest/gene-expression-essentials_en.html"
                width="650"
                height="500"
                allowfullscreen>
            </iframe>
        """),
        ("Beer's Law Lab", """
            <iframe src="https://phet.colorado.edu/sims/html/beers-law-lab/latest/beers-law-lab_en.html"
                width="650"
                height="500"
                allowfullscreen>
            </iframe>
        """),
        ("Kepler's Laws", """
            <iframe src="https://phet.colorado.edu/sims/html/keplers-laws/latest/keplers-laws_en.html"
                width="650"
                height="500"
                allowfullscreen>
            </iframe>
        """),
        ("Hooke's Law", """
            <iframe src="https://phet.colorado.edu/sims/html/hookes-law/latest/hookes-law_en.html"
                width="650"
                height="500"
                allowfullscreen>
            </iframe>
        """),
        ("pH Scale Basics", """
            <iframe src="https://phet.colorado.edu/sims/html/ph-scale-basics/latest/ph-scale-basics_en.html"
                width="650"
                height="500"
                allowfullscreen>
            </iframe>
        """)
    ]

    simulation_names = [sim[0] for sim in simulations]
    selected_simulation_name = st.selectbox("Select Simulation", simulation_names)
    selected_simulation = next(sim for sim in simulations if sim[0] == selected_simulation_name)

    st.write(f"**{selected_simulation[0]}**")
    st.components.v1.html(selected_simulation[1], height=600)

