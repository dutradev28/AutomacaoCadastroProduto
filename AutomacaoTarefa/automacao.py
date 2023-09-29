import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.3
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=724, y=400)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Importar base de dados
tabela = pandas.read_csv("E:\Programação New\PythonPowerup\AutomacaoTarefa\produtos.csv")
print(tabela)

for linha in tabela.index:
    # Cadastrar produto
    pyautogui.click(x=682, y=280)
    
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    # Enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(50000)

