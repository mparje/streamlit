import streamlit as st
import requests

def buscar_repositorios(keyword):
    url = f"https://api.github.com/search/repositories?q={keyword}+streamlit+in:name+in:description+language:Python"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["items"]
    else:
        return []

def mostrar_resultados(repositorios):
    for repo in repositorios:
        st.markdown(f"### [{repo['name']}]({repo['html_url']})")
        st.markdown(f"Por: [{repo['owner']['login']}]({repo['owner']['html_url']})")
        st.markdown(f"Descripción: {repo['description']}")
        st.markdown("---")

st.title("Buscador de aplicaciones Streamlit")
palabra_clave = st.text_input("Ingresa la palabra clave para buscar aplicaciones Streamlit:")

if palabra_clave:
    st.write(f"Resultados para: '{palabra_clave}'")
    repositorios = buscar_repositorios(palabra_clave)
    mostrar_resultados(repositorios)
