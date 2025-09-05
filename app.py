import streamlit as st

def calculate_mass_balance(initial_pulp_mass, initial_brix, final_brix):
    """
    Calculates the required amount of sugar to add to a pulp
    to reach a desired Brix level using a mass balance equation.
    
    Args:
        initial_pulp_mass (float): The initial mass of the pulp in kg.
        initial_brix (float): The initial Brix value of the pulp (%).
        final_brix (float): The final desired Brix value of the pulp (%).
    
    Returns:
        tuple: A tuple containing the final mass of the pulp and the
               mass of sugar to be added, both in kg.
    """
    try:
        # Convert Brix to decimal
        x1 = initial_brix / 100
        x2 = 1.0  # Sugar is 100% soluble solids
        x3 = final_brix / 100

        # General mass balance: M1 + M2 = M3
        # Soluble solids balance: M1*x1 + M2*x2 = M3*x3

        # Substitute M3 from the general balance into the solids balance
        # M1*x1 + M2*x2 = (M1 + M2)*x3
        # M1*x1 + M2*x2 = M1*x3 + M2*x3
        # M2*x2 - M2*x3 = M1*x3 - M1*x1
        # M2*(x2 - x3) = M1*(x3 - x1)
        # M2 = M1 * (x3 - x1) / (x2 - x3)

        # Calculate the mass of sugar to add (M2)
        m2 = initial_pulp_mass * (x3 - x1) / (x2 - x3)
        
        # Calculate the final mass of the pulp (M3)
        m3 = initial_pulp_mass + m2

        return m3, m2
    
    except ZeroDivisionError:
        return None, None

# Streamlit web app interface
st.title('Calculadora de Balance de Masa de Pulpa')
st.markdown("""
Esta aplicación resuelve un problema de balance de masa para determinar la cantidad de azúcar necesaria 
para ajustar el nivel de Brix de una pulpa de fruta.
""")
st.image('https://raw.githubusercontent.com/username/repository/main/image_10f59a.jpg', caption='Diagrama del problema de balance de masa')

st.header('Datos del Problema')

# Input fields for user data
initial_pulp_mass_input = st.number_input('Masa Inicial de Pulpa ($M_1$) en kg:', min_value=0.0, value=50.0, step=0.1)
initial_brix_input = st.number_input('Brix Inicial de la Pulpa (%) ($X_1$):', min_value=0.0, max_value=100.0, value=7.0, step=0.1)
final_brix_input = st.number_input('Brix Final Deseado (%) ($X_3$):', min_value=0.0, max_value=100.0, value=10.0, step=0.1)

if st.button('Calcular'):
    if final_brix_input <= initial_brix_input:
        st.error("El Brix final deseado debe ser mayor que el Brix inicial para que la adición de azúcar tenga sentido.")
    else:
        # Perform the calculation
        final_mass, sugar_to_add = calculate_mass_balance(initial_pulp_mass_input, initial_brix_input, final_brix_input)
        
        if final_mass is not None and sugar_to_add is not None:
            # Display the results
            st.subheader('Resultados')
            st.success(f"Para ajustar la pulpa a **{final_brix_input}% Brix**, se debe agregar:")
            st.metric("Azúcar a agregar ($M_2$)", f"{sugar_to_add:.2f} kg")
            st.markdown(f"La masa final de la pulpa será de **{final_mass:.2f} kg**.")
            st.info("Este cálculo se basa en un balance de masa asumiendo que el azúcar añadido es 100% sólidos solubles.")
        else:
            st.error("Ocurrió un error en el cálculo. Por favor, revise los valores ingresados.")

st.markdown("""
<br>
<br>
---
**Nota:** El código en este script asume la imagen se encuentra en la misma carpeta del repositorio. 
Reemplace `username/repository` con su usuario y nombre de repositorio de GitHub.
""", unsafe_allow_html=True)
```
***
### ⚙️ Instrucciones para el despliegue

1.  **Guarda el código**: Guarda el código anterior en un archivo con el nombre `app.py`. Este será el archivo principal de tu aplicación Streamlit.

2.  **Crea un repositorio en GitHub**:
    * Ve a **GitHub** y crea un nuevo repositorio público.
    * Sube el archivo `app.py` y, si deseas que se muestre en la aplicación, la imagen del problema (`image_10f59a.jpg`) a este repositorio.
    * Es recomendable incluir un archivo `requirements.txt` que especifique las dependencias del proyecto. Para este caso, el contenido sería simplemente:
        ```
        streamlit
        
