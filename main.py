from tkinter import *
import requests
import json
import sys

from datetime import datetime

root = Tk()
root.geometry("650x550") # tamanho da janela por padrão
root.resizable(0,0)     # manteremos o tamanho da janela fixo

# titulo para a janela
root.title("Aplicativo do Tempo")

valor_cidade = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def MostrarClima():

# Entre com a chave(key) de sua API que foi gerada em https://home.openweathermap.org/api_keys após 
#ter criado sua conta gratuitamente

    api_key = "429d1cf58ae2f7017f1363be7db4ed26"
    
    # recebe o nome da cidade fornecido pelo usuário
    nome_cidade = valor_cidade.get()
    
    # URL da API
    clima_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + nome_cidade + '&appid='+api_key
    
    # recebe a resposta
    resposta = requests.get(clima_url)
    
    # muda a resposta do json para a leitura do python
    clima_info = resposta.json()
    
    tfield.delete("1.0", "end") # limpa o campo do texto para cuma nova saída 
    
    # na documentação da API , se o 'cod' é 200 , isso significa que os dados meteorológicos foram obtidos com sucesso
    
    if clima_info['cod'] == 200:
        kelvin = 273 # valor em kelvin
    
        temperatura = int(clima_info['main']['temp'] - kelvin)
        sensacao_termica = int(clima_info['main']['feels_like'] - kelvin)
        pressao = clima_info['main']['pressure']
        umidade = clima_info['main']['humidity']
        velocidade_vento = clima_info['wind']['speed']*3.6
        sunrise = clima_info['sys']['sunrise']
        sunset = clima_info['sys']['sunset']
        timezone = clima_info['timezone']
        nublado = clima_info['clouds']['all']
        descricao = clima_info['weather'][0]['description']
        
        hora_nascente = time_format_for_location(sunrise + timezone)
        hora_poente = time_format_for_location(sunset + timezone)
        
        clima = f"\nClima de: {nome_cidade}\nTemperatura (Celsius): {temperatura}°\nSensação térmica (Celsius): {sensacao_termica}°\nPressão: {pressao} hPa\nUmidade: {umidade}%\nSol nasce às: {hora_nascente} e se põe às {hora_poente}\nNublado: {nublado}%\nInformações: {descricao}"
    else:
        clima = f"\n\tO clima para '{nome_cidade}' não foi encontrado\n\tFavor digite um nome válido !!"
    
    tfield.insert(INSERT, clima)   #to insert or send value in our Text Field to display output

# FRONTEND da aplicação

city_head= Label(root, text = 'Digite o nome da cidade', font = 'Arial 18 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = valor_cidade,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = MostrarClima, text = "Conferir Clima", font="Arial 12", bg='powderblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "O clima é:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=48, height=20, font='Roboto 20')
tfield.pack(pady=20, padx=15)
root.configure(background='steelblue')
root.mainloop()