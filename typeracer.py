from selenium.webdriver.common.keys import Keys
from ffdriver import FfDriverSession

class TypeRacerAuto:
    __type_racer_url = "https://play.typeracer.com/"
    __driver_session = None
    __enter_race_css = "a.gwt-Anchor"
    __span_attribute_css = "span[unselectable='on']"

    def __init__(self):
        self.__driver_session = FfDriverSession()

    def create_type_racer_session(self):
        self.__driver_session.get_url(self.__type_racer_url)
        self.__driver_session.wait_until_elem_by_css(self.__enter_race_css)
        
        # remove unwanted cookies acceptance dialogs
        js = "var cookieaccept = document.querySelector('.qc-cmp-ui-container'); if(cookieaccept) cookieaccept.parentNode.removeChild(cookieaccept)"
        self.__driver_session.exec_js(js)

        # enter new race by keyboard shortcut and wait
        self.__driver_session.sim_key_in_session(Keys.CONTROL, Keys.ALT, 'i')
        self.__driver_session.suspend_session_until(15)

        # locate words to type
        elem_text_spans = self.__driver_session.locate_elems_by_css(self.__span_attribute_css)
        
        # there may be sentences starting with one letter only, so a space has to be added
        text = None
        if len(elem_text_spans) == 2:
            text = "%s %s" % (elem_text_spans[0].text, "".join([elem.text for elem in elem_text_spans[1:]]))
        else:
            text = "%s%s %s" % (elem_text_spans[0].text, elem_text_spans[1].text, "".join([elem.text for elem in elem_text_spans[2:]]))
        print("Word to type: %s" % text)

        self.__driver_session.sim_typing(text, 0.12)


if __name__ == "__main__":
    cheat = TypeRacerAuto()
    cheat.create_type_racer_session()
