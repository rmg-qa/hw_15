"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=['Desktop', 'Mobile'])
def browser_size_window(request):
    if request.param == 'Desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'Mobile':
        browser.config.window_width = 380
        browser.config.window_height = 700
    yield
    browser.quit()


@pytest.mark.parametrize('browser_size_window', ['Desktop'], indirect=True)
def test_github_desktop(browser_size_window):
    browser.open('https://github.com/')
    browser.element('.//a[contains(text(), "Sign up")]').click()
    assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))


@pytest.mark.parametrize('browser_size_window', ['Mobile'], indirect=True)
def test_github_mobile(browser_size_window):
    browser.open('https://github.com/')
    browser.element('.//div[@class="flex-1"]//child::button').click()
    browser.element('.//a[contains(text(), "Sign up")]').click()
    assert browser.element('[id="signup-form-fields"]').should(have.text('Sign up for GitHub'))
