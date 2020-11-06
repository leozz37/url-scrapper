import pytest

from scrapper.url_scrapper import Scrapper


@pytest.fixture
def scrapper() -> Scrapper:
    """
    Create an instance to be used across the test suite
    """
    # Set up
    scrapper = Scrapper()
    yield scrapper


def test_create_url_with_success(scrapper: Scrapper) -> None:
    """
    Test if the right URL will be returned
    """
    expected_output = "https://www.google.com/search?tbm=isch&q=Hello%20World"
    resulted_output = scrapper.create_url("Hello World")

    assert expected_output == resulted_output