#Importando Pacotes 
import pickle
import streamlit as st
import numpy as np

 
# Carregando a Máquina Preditiva
pickle_in = open('lr.pickle','rb') 
maquina_preditiva = pickle.load(pickle_in)
pickle_in = open('X.pickle', 'rb') 
X = pickle.load(pickle_in)

#Manter a sessão em cache 
@st.cache()
  
# Criando a função que irá fazer a predição usando os dados impostados pelo usuário do Sistema 
def predict_price(location,sqft,bath,br):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = br
    if loc_index >= 0:
        x[loc_index] = 1

    return maquina_preditiva.predict(x.reshape(1, -1))[0]

#função paara colocar uma imagem de fundo

# Essa função é para criação da webpage  
def main():  

    # Elementos da webpage
    html_temp = """ 
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:white;text-align:center;">SAE</h1> 
    <h2 style ="color:white;text-align:center;">Sistema de previsão imobiliário-PROJETO EM DESENVOLVIMENTO DE SISTEMAS </h2> 
    </div> 
    """
      
    # Função do stramlit que faz o display da webpage
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # As linhas abaixo criam as caixas na qual o usuário vai entrar com dados da pessoa que quer o empréstimo para fazer a Predição
    
    location = st.selectbox("Localização",(X.columns[3:]))
    sqft = int(st.number_input("Metros quadrados"))
    bath = int(st.slider("Banheiros",min_value=1,max_value=30,step=1,value=15)) 
    br = int(st.slider('Quartos',min_value=1,max_value=30,step=1,value=15))
    result =""


    #Quando o Usuário clicar no botão "Verificar" a Máquina Preditiva faz seu trabalho
    if st.button("Verificar"): 
        result = predict_price(location,sqft,bath,br) 
        st.success('O valor foi {}'.format(result))
        print(result)
     
if __name__=='__main__': 
    main()
