from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

class sauceDemoTest:
    # kullanıcı_adı ve sifre alanlarının boş bırakılması durumu.
    def notEnteredUsernameAndPassword(self): #

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)

        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")

        sleep(5)

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Username is required" == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(5)

    # sadece kullanıcı_adı alanının doldurulması sifre alanının boş bırakılması durumu.
    def notEnteredPassword(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")

        sleep(3)
        
        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")

        kullanıcı_adı.send_keys("abc")
        
        sleep(5)

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Password is required" == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(5)


    # kilitlenmiş bir hesabın sisteme giriş yaparken karşılaştığı sonuç.
    def lockedUser(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")

        sleep(3)

        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")

        kullanıcı_adı.send_keys("locked_out_user")
        sifre.send_keys("secret_sauce")

        sleep(5)

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(3)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage.text)

        if "Epic sadface: Sorry, this user has been locked out." == errorMessage.text:
            print("TEST SONUC: Doğru")
        else:
            print("TEST SONUC: Yanlış")
            
        sleep(5)


    # kullanıcı_adı ve sifre kutucuklarının yanında çıkan uyarı mesajını kapatma durumu.
    def ıcon(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")    
        
        sleep(3)

        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(5)

        errorIcon = driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()

        sleep(3)

    # sisteme giriş yapıldığı takdirde yönlendirilen sayfayı görme durumu.
    def redirectToSite(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        sleep(1)

        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")
        
        kullanıcı_adı.send_keys("standard_user") 
        sifre.send_keys("secret_sauce") 

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(1)

        link = driver.current_url
        if "/inventory.html" in link:
            print("Doğru sayfadasınız.")

        sleep(5)
       
        
    # bir üstteki fonksiyon sonucu açılan sayfada kaç adet ürün olduğunu gösteren durum.  
    def NumberOfProducts(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        sleep(1)

        kullanıcı_adı = driver.find_element(By.ID, "user-name")
        sifre = driver.find_element(By.ID, "password")

        kullanıcı_adı.send_keys("standard_user") 
        sifre.send_keys("secret_sauce") 

        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()

        sleep(1)

        listOfProduct = driver.find_elements(By.CLASS_NAME, "inventory_item") 

        print(f"Toplam Ürün Sayısı: {len(listOfProduct)}")

        sleep(5)



test1 = sauceDemoTest()
test2 = sauceDemoTest()
test3 = sauceDemoTest()
test4 = sauceDemoTest()
test5 = sauceDemoTest()
test6 = sauceDemoTest()


test1.notEnteredUsernameAndPassword()
test2.notEnteredPassword()
test3.lockedUser()
test4.ıcon()
test5.redirectToSite()
test6.NumberOfProducts()