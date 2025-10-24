"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture()
def browser_size_window(width, height):
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.mark.parametrize('width, height', [(1920, 1080), (1680, 1050), (1440, 1050),
                                           (1280, 720), (900, 700), (650, 700), (380, 625)], )
def test_github_desktop(browser_size_window, width, height):
    if width <= 1011:
        pytest.skip('Проверяется разрешения экранов только для десктопа и планшетов')
    else:
        browser.open('https://github.com/')
        browser.element('.//a[contains(text(), "Sign up")]').click()
        assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))


@pytest.mark.parametrize('width, height', [(1920, 1080), (1680, 1050), (1440, 1050),
                                           (1280, 720), (900, 700), (650, 700), (380, 625)], )
def test_github_mobile(browser_size_window, width, height):
    if width >= 1011:
        pytest.skip('Проверяется разрешение экрана только для мобильных устройств и планшетов')
    else:
        browser.open('https://github.com/')
        browser.element('.//div[@class="flex-1"]//child::button').click()
        browser.element('.//a[contains(text(), "Sign up")]').click()
        assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))
