# Bazaar Selenium Autotests  
Autotests for web application [Bazaar Origin](https://bazaarorigin.com/)  

## 📌 Functionality  
- Check keyword search  
- Authorization check  
- Transitions from home page
- Checking H1 headline on the home page  

## 🛠️ Tech
- Python + Pytest  
- Selenium WebDriver  
- Allure для отчетности  

## 🚀 Run Tests 
### **Installing**  
1. Clone the repository:  
   ```sh
   git clone https://github.com/asegorova95/Bazaar_UI_Autotests
   cd Bazaar_UI_Autotests
   
2. Install requirements:

    ```sh
   pip install -r requirements.txt

3. Run tests
    ```sh
    pytest --browser_name=chrome --alluredir=allure-results
   
📊 Allure report generation
  ```sh
    allure serve allure-results
  ```

## Additional options
Run in Chrome (default)
  ```sh
    pytest --alluredir=allure-results
   ```
Run in Firefox
``` sh
   pytest --browser=firefox --alluredir=allure-results 
```

Run in headless (no UI)
``` sh
   pytest --browser=chrome --headless --alluredir=allure-results
   ```

Changing the screen size
``` sh
   pytest --window_size=1280,720 --alluredir=allure-results
 ```
