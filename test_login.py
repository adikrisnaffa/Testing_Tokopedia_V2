from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tokopedia.com")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


#==================================================================================================================================================================
# Scenario: Success Login with correct credential
#     Given I am on the homepage
#     When I Click Sign in
#     And I fill my credential
#     Then I should be logged in
#==================================================================================================================================================================

@pytest.mark.login_positivetest
def test_login_success(context):
    context.find_element_by_xpath('//button[@data-testid="btnHeaderLogin"]').click()
    context.find_element_by_xpath('//input[@data-testid="email-phone-input"]').send_keys('0895356997421')
    context.find_element_by_id("email-phone-submit").click()
    context.find_element_by_xpath('//div[@data-unify="Card"]').click()
    time.sleep(5)

    # assert "Pilih Metode Verifikasi" in context.find_element_by_xpath('//div[@class="css-1gucsjs"]').text()

#==================================================================================================================================================================
# Scenario: Success Login with correct credential
#     Given I am on the homepage
#     When I Click Sign in
#     And I fill wrong my credential
#     Then I should not be logged in
#     And I show error on homepage
#==================================================================================================================================================================

@pytest.mark.login_negativetest
def test_login_failed(context):
    context.find_element_by_xpath('//button[@data-testid="btnHeaderLogin"]').click()
    context.find_element_by_xpath('//input[@data-testid="email-phone-input"]').send_keys('0000000000')
    context.find_element_by_id("email-phone-submit").click()

    # assert "" in context.find_element_by_xpath("login").click()

#==================================================================================================================================================================
# Scenario: Success search something in Search Bar
#     Given I am on the homepage
#     When I fill someting in Search Bar
#     And I get result from search something
#     Then I should not be logged in
#==================================================================================================================================================================

@pytest.mark.search
def test_search(context):
    context.find_element_by_xpath('//input[@data-unify="Search"]').send_keys("Laptop" + Keys.ENTER)
    time.sleep(5)

    assert "Laptop" in context.find_element_by_xpath('//div[@data-testid="dSRPSearchInfo"]').text
    time.sleep(5)


#==================================================================================================================================================================
# Scenario: Success move to window "Tentang Tokopedia", "Mitra Tokopedia", "Mulai Berjualan", "Promo", "Tokopedia Care"
#     Given I am on the homepage
#     When I click Link "Tentang Tokopedia" Text on Header Container
#     And I move to window "Tentang Tokopedia"
#     Then I am on the homepage "Tokopedia"
#==================================================================================================================================================================

Link_Text = [
    ('Tentang Tokopedia', 1, 'Tentang Tokopedia: Ketahui Lebih Banyak Tentang Kami'),                      # Window 1
    ('Mitra Tokopedia', 1, 'Mitra Tokopedia: Kembangkan Usaha Jadi Untung dan Maju'),                      # Window 2
    ('Mulai Berjualan', 1, 'Pusat Seller | Artikel'),                                                      # Window 3
    ('Promo', 1, 'Promo Terbaru Bulan Ini di Tahun 2022 - Cek Kode Promo di Tokopedia'),                   # Window 4
    ('Tokopedia Care', 1, 'Tokopedia Care')                                                                # Window 5
]

@pytest.mark.parametrize('name_window , window , result', Link_Text)
@pytest.mark.move_to_window
def test_move_window(context,name_window,window,result):
    context.find_element(By.LINK_TEXT, name_window).click()
    time.sleep(5)
    context.switch_to.window(context.window_handles[window])
    time.sleep(3)
    assert result in context.title
    time.sleep(5)

#==================================================================================================================================================================
# Scenario: Success Mouse Hover to 'Kategori'
#     Given I am on the homepage
#     When I am mouse hover Link 'Kategori' on Header Container
#     And show list in 'Kategori'
#     And I am mouse hover Link 'Buku' on list in 'Kategori'
#     And show list in 'Buku'
#     And I am mouse hover Link 'Buku Bangunan' on list in 'Buku'
#==================================================================================================================================================================

@pytest.mark.mouse_hover_Kategori
def test_mouse_hover(context):
    ActionChains(context).move_to_element(context.find_element(By.XPATH, '//div[@data-testid="headerText"]')).perform()
    time.sleep(5)
    ActionChains(context).move_to_element(context.find_element(By.LINK_TEXT, "Buku")).perform()
    time.sleep(5)
    ActionChains(context).move_to_element(context.find_element(By.LINK_TEXT, "Buku Bangunan")).perform()
    time.sleep(3)
    context.find_element(By.LINK_TEXT, 'Buku Bangunan').click()
    time.sleep(3)
    assert 'Buku Bangunan' in context.find_element(By.CSS_SELECTOR, 'h1.css-krdkpb').text
    time.sleep(5)

#==================================================================================================================================================================
# Scenario: Success logged in Icon Kategori
#     Given I am on the homepage
#     When I click Icon Kategori
#     And show list in 'Icon Kategori'
#==================================================================================================================================================================

@pytest.mark.HomeDynamic_Icon_Kategori
def test_HomeDynamic_Icon_Kategori(context):
     context.find_element(By.XPATH, '//a[@data-testid="icnHomeDynamicIcon#1"]').click()
     assert 'Kategori' in context.find_element(By.CSS_SELECTOR, 'div.css-1ez3kt7').text


#==================================================================================================================================================================
# Scenario: Success logged in Icon Handphone & Tablet, Top-Up & Tagihan, Travel & Entertainment, Perawatan Hewan, Keuangan, Komputer & laptop
#     Given I am on the homepage
#     When I click Icon Home Dynamic
#     And I am on the homepage
#==================================================================================================================================================================


Icon = [
    ('//a[@data-testid="icnHomeDynamicIcon#2"]', 'Handphone & Tablet Pilihan Terlengkap & Produk Terbaru'),         # Icon 2
    ('//a[@data-testid="icnHomeDynamicIcon#3"]', 'Bayar PLN, Bayar Pulsa & Produk Digital Lainnya | Tokopedia'),    # Icon 3                      
    ('//a[@data-testid="icnHomeDynamicIcon#4"]', 'Cari Berbagai Tiket Destinasi Perjalanan dan Hiburan Menarik'),   # Icon 4                                                   
    ('//a[@data-testid="icnHomeDynamicIcon#5"]', 'Perawatan Hewan Pilihan Terlengkap & Produk Terbaru'),            # Icon 5   
    ('//a[@data-testid="icnHomeDynamicIcon#6"]', 'Cek Tokopedia Keuangan | Tokopedia'),                             # Icom 6
    ('//a[@data-testid="icnHomeDynamicIcon#7"]', 'Komputer & Laptop Pilihan Terlengkap & Produk Terbaru')           # Icon 7                                                              
]

@pytest.mark.parametrize('name_icon ,result_icon', Icon)
@pytest.mark.HomeDynamic_Other_Icon
def test_Other_Icon(context, name_icon, result_icon):
     context.find_element(By.XPATH, name_icon).click()
     time.sleep(5)
     assert result_icon in context.title