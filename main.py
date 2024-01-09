import pandas as pd
import pyautogui
import time


pyautogui.PAUSE = 0.5


def login():
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    email = "fakeemail@gmail.com"
    password = "thisisapassword"
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("tab")
    pyautogui.press("enter")


def product_registration():
    table = pd.read_csv("produtos.csv")
    
    for row in table.index:
        pyautogui.click(x=906, y=352)
        product_id = table.loc[row, "codigo"]
        product_brand = table.loc[row, "marca"]
        product_type = table.loc[row, "tipo"]
        product_category = str(table.loc[row, "categoria"])
        product_unit_price = str(table.loc[row, "preco_unitario"])
        product_cost = str(table.loc[row, "custo"])
        product_obs = table.loc[row, "obs"]
        pyautogui.write(product_id)
        pyautogui.press("tab")
        pyautogui.write(product_brand)
        pyautogui.press("tab")
        pyautogui.write(product_type)
        pyautogui.press("tab")
        pyautogui.write(product_category)
        pyautogui.press("tab")
        pyautogui.write(product_unit_price)
        pyautogui.press("tab")
        pyautogui.write(product_cost)
        pyautogui.press("tab")
        if not pd.isna(product_obs):
            pyautogui.write(product_obs)
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)


def main():
    login()
    product_registration()


if __name__ == "__main__":
    main()
