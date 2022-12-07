
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestQuestionerror():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_questionerror(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("test")
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'testwork'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.ID, "id_tags_0").click()
    self.driver.find_element(By.ID, "id_tags_1").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
  
testClass = TestQuestionerror()

testClass.setup_method("")
testClass.test_questionerror()
testClass.teardown_method("")