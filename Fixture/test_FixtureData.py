import pytest

from Fixture.Base import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info("data load")
        print(dataLoad)
        log.info(dataLoad[1])
        print(dataLoad[0])


