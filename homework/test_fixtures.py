"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture(scope='function')
def window_size_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture(scope='function')
def window_size_mobile():
    browser.config.window_width = 380
    browser.config.window_height = 700
    yield
    browser.quit()


def test_github_desktop(window_size_desktop):
    browser.open('https://github.com/')
    browser.element('.//a[contains(text(), "Sign up")]').click()
    assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))


def test_github_mobile(window_size_mobile):
    browser.open('https://github.com/')
    browser.element('.//div[@class="flex-1"]//child::button').click()
    browser.element('.//a[contains(text(), "Sign up")]').click()
    assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))
