from addons.tab_actions import TabActions
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="MUb-adFAImllDayoLzYaciJnFHyeBVppQZMAMczkLRg1",
                              project_name="test",
                              job_name="t")
    step_settings = StepSettings(timeout=25000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    ApplicationURL = "http://findbug.kwork.ru/back/?t=1f43e4b23287d28e"
    driver.get(f'{ApplicationURL}')


# сложность от 0 до 100, уровень интелекта 0
    difficult_from = driver.find_element(By.CSS_SELECTOR,
                                         "#difficult_from")
    difficult_from.send_keys("1")
    difficult_to = driver.find_element(By.CSS_SELECTOR,
                                       "#difficult_to")
    difficult_to.send_keys("100")

    intellect = driver.find_element(By.CSS_SELECTOR,
                                    "#intellect")
    intellect.send_keys("0")

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()


# сложность от 0 до 100, уровень интелекта 100
    intellect = driver.find_element(By.CSS_SELECTOR,
                                    "#intellect")
    intellect.clear()

    intellect = driver.find_element(By.CSS_SELECTOR,
                                    "#intellect")
    intellect.send_keys("100")

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()


# сложность от 40 до 80, уровень интелекта 50
    difficult_from = driver.find_element(By.CSS_SELECTOR,
                                         "#difficult_from")
    difficult_from.clear()

    difficult_from = driver.find_element(By.CSS_SELECTOR,
                                         "#difficult_from")
    difficult_from.send_keys("40")

    difficult_to = driver.find_element(By.CSS_SELECTOR,
                                       "#difficult_to")
    difficult_to.clear()

    difficult_to = driver.find_element(By.CSS_SELECTOR,
                                       "#difficult_to")
    difficult_to.send_keys("80")

    intellect = driver.find_element(By.CSS_SELECTOR,
                                    "#intellect")
    intellect.clear()

    intellect = driver.find_element(By.CSS_SELECTOR,
                                    "#intellect")
    intellect.send_keys("50")

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()


# генерация дополнительных результатов
    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()

    sbt = driver.find_element(By.CSS_SELECTOR,
                              "#sbt")
    sbt.click()


# Проверка 'Результатов проведенных тестов'
    _ = driver.find_element(By.XPATH,
                            "//a[. = 'Результаты проведенных тестов']")
    _.click()

    driver.switch_to.window(driver.window_handles[1])

    driver.switch_to.window(driver.window_handles[0])

    driver.addons().execute(
        TabActions.closelasttab(
        ))


# Проверка 'Состояние таблицы вопросов'
    _ = driver.find_element(By.XPATH,
                            "//a[. = 'Состояние таблицы вопросов']")
    _.click()

    driver.switch_to.window(driver.window_handles[1])

    driver.switch_to.window(driver.window_handles[0])

    driver.addons().execute(
        TabActions.closelasttab(
        ))
