from selene.support.shared import browser
from selene.support.conditions import have

def test_google_search(open_browser):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_search_negative(open_browser):
    browser.element('[name=q]').type('ajfhakjdfakjdb').press_enter()
    browser.element('[class=card-section]').should(have.text("Your search - ajfhakjdfakjdb - did not match any documents."))
