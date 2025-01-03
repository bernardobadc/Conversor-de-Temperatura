# Importando a biblioteca customtkinter para interface gráfica e Image para inserir uma imagem
from PIL import Image
import customtkinter as ctk


# Definindo variáveis para as cores
green_color = "#15e825"
fore_color = "#F0F0F0"
black_color = "#333333"
menu_option_color = "#6e6d6d"

# Função para validar a entrada do input
def validate_entry(input_value):
    # Limitando a apenas 5 dígitos na entrada do usuário
    if len(input_value) > 6:
        return False

    # Impedindo o uso da vírgula no lugar do ponto
    if "," in input_value:
        return False

    # Usando o startswith para checar se começa com um sinal de "-" para temperaturas negativas. 
    if input_value.startswith("-"):
        input_value = input_value[1:]              # Removendo o sinal do começo para facilitar a validação que virá

    # Validando se são apenas números, ou uma string vazia para o caso do usuário apagar o que foi escrito
    if input_value == "" or input_value.replace(".","",1).isdigit():
        return True
    return False

# Criando as funções para converter a temperatura
def celsius_converter(temperature, scale):
    if scale == 'Fahrenheit':
        temperature = (temperature * 1.8) + 32
        return temperature
    return temperature + 273.15

def fahrenheit_converter(temperature, scale):
    if scale == 'Celsius':
        temperature = (temperature - 32) / 1.8
        return temperature
    temperature = ((temperature - 32) * 5/9) + 273.15
    return temperature

def kelvin_converter(temperature, scale):
    if scale == 'Celsius':
        temperature = temperature - 273.15
        return temperature
    temperature = (temperature - 273.15) * 9 / 5 + 32
    return temperature

# Função para obter os valores do Entry e dos Menu's e fazer a conversão
def make_conversion():
    # Obtendo os valores do Entry e dos Menu Options
    temperature = float(temperature_entry.get())
    actual_scale = option_menu_left.get()
    new_scale = option_menu_right.get()

    # Checando se o usuário não está tentando converter para a mesma escala, se sim, a função retornará None
    if actual_scale == new_scale:
        return None

    if actual_scale == 'Celsius':
        new_temperature = celsius_converter(temperature, new_scale)
        return new_temperature
    elif actual_scale == 'Fahrenheit':
        new_temperature = fahrenheit_converter(temperature, new_scale)
        return new_temperature
    else:
        new_temperature = kelvin_converter(temperature, new_scale)
        return new_temperature
    
# Função para mostrar a nova temperatura, atualizando a label "bottom_label" que fora criada vazia
def update_label():
    # Obtendo a nova temperatura convertida e o valor da escala do option menu à direita, para exibir na mensagem
    new_temperature = make_conversion()
    new_scale = option_menu_right.get()

    # Checando se a variável new_temperature, que recebe o valor do Menu Option da direita é None. 
    # Se for, as escalas são iguais, então retorno uma mensagem para a variável label_text pedindo para utilizar escalas diferentes
    # Se não for, armazeno em label_text a mensagem com a temperatura convertida
    if new_temperature == None:
        label_text = 'Utilize escalas diferentes para fazer a conversão!'
        bottom_label.configure(font=("Arial", 16))
    else:
        label_text = f'{new_temperature:.1f}°{new_scale[0:1:]}'
        bottom_label.configure(font=("Arial", 30))

    # Atualizando o texto da label
    bottom_label.configure(text=label_text)
    

# Criando a janela e definindo as propriedades da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("400x500")
window.title("Conversor de Temperatura")
window.resizable(width=False, height=False)
window.iconbitmap("assets/temperatura.ico")


# Criando a label da temperatura
main_label = ctk.CTkLabel(window, text="Digite a Temperatura Atual", font=("Arial", 26), text_color=green_color)
main_label.pack(padx=30, pady=65)

# Registrando a validação do input

validate_command = window.register(validate_entry)

# Criando o entry da temperatura

temperature_entry = ctk.CTkEntry(window, 
                                 placeholder_text="Temperatura Atual",
                                 fg_color= fore_color,
                                 text_color= black_color,
                                 border_color= green_color,
                                 border_width=1,
                                 font=("Arial", 20),
                                 width=200,
                                 height=35,
                                 corner_radius=15,
                                 validate="key",
                                 validatecommand=(validate_command, '%P'))

temperature_entry.place(relx=0.5, rely=0.3, anchor="center")

# Adicionando a imagem do botão
image = ctk.CTkImage(Image.open("assets/ciclo.png"), size=(45, 45))

# Criando o botão de conversão e associando a imagem
conversion_btn = ctk.CTkButton(window,
                               image=image,
                               text="",
                               width=25,
                               height=25,
                               fg_color=black_color,
                               corner_radius=15,
                               hover_color="#000000",
                               command=update_label)

conversion_btn.place(relx=0.5, rely=0.5, anchor="center")

# Criando as caixas de seleção
option_menu_left = ctk.CTkOptionMenu(window,
                                      values=["Celsius", "Fahrenheit", "Kelvin"],
                                      fg_color=menu_option_color,
                                      button_color=menu_option_color,
                                      button_hover_color="#4e4b4b",
                                      font=("Arial", 14),
                                      width=135,
                                      height=35)
option_menu_left.place(relx=0.2, rely=0.5, anchor="center")

option_menu_right = ctk.CTkOptionMenu(window,
                                      values=["Celsius", "Fahrenheit", "Kelvin"],
                                      fg_color=menu_option_color,
                                      button_color=menu_option_color,
                                      button_hover_color="#4e4b4b",
                                      font=("Arial", 14),
                                      width=135,
                                      height=35)
option_menu_right.set("Fahrenheit")
option_menu_right.place(relx=0.8, rely=0.5, anchor="center")

# Criando a label que exibirá a temperatura convertida só que sem texto, para depois apenas atualizar o texto na função
bottom_label = ctk.CTkLabel(window, text="", font=("Arial", 30), text_color=green_color)
bottom_label.place(relx=0.5, rely=0.7, anchor="center")

window.mainloop()