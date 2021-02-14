from selenium import webdriver
driver = webdriver.Chrome("C:\webdriver\chromedriver")
driver.get("http://127.0.0.1:8000/login/")
username = ['admin','root','master']
password= ['admin123','root123','master123']
i=0
while (i<3):
    user_input= driver.find_element_by_id ('login_username')
    user_input.send_keys(username[i])
    password_input = driver.find_element_by_id ('login_password')
    password_input.send_keys(password[i])
    login_button = driver.find_element_by_id ('login_button')
    login_button.click()
    current_url= (driver.current_url) 
    try:
        if (current_url == "http://127.0.0.1:8000/backend/dashboard/" ):
            print ("Log in Succesfull")
        profile_image = driver.find_element_by_id ('profile-img')
        profile_image.click()
        logot_link = driver.find_element_by_id ('admin-logot-link')
        logot_link.click()
    except:
        print ("Log in Unsuccesfull")
        i=i+1
        continue
            
    i=i+1
    
#driver.quit() 
    
  