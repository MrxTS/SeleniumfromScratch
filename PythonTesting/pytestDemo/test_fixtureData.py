import pytest

from pytestDemo.baseClass import baseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(baseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad[2])

