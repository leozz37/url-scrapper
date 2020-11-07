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
    Test if the right URL will be returned correctly
    """
    expected_output = "https://en.wikipedia.org/wiki/Brazil"
    resulted_output = scrapper.create_url("Brazil")

    assert expected_output == resulted_output


def test_create_url_with_spaces_with_success(scrapper: Scrapper) -> None:
    """
    Test if the right URL will be returned without spaces correctly
    """
    expected_output = "https://en.wikipedia.org/wiki/Marie_Curie"
    resulted_output = scrapper.create_url("Marie Curie")

    assert expected_output == resulted_output


def test_create_url_multiple_spaces_with_success(scrapper: Scrapper) -> None:
    """
    Test if the right URL will be returned without spaces correctly
    """
    expected_output = "https://en.wikipedia.org/wiki/Alfred_Russel_Wallace"
    resulted_output = scrapper.create_url("Alfred Russel Wallace")

    assert expected_output == resulted_output


def test_get_urls_with_success(scrapper: Scrapper) -> None:
    """
    Test if the size of the set of images is correct
    """
    url = "https://en.wikipedia.org/wiki/Albert_Einstein"
    images_url = scrapper.get_urls(url)

    # This value may vary in the future
    assert len(images_url) == 24


def test_get_urls_zero_images_with_success(scrapper: Scrapper) -> None:
    """
    Test if the size of the set of images is correct
    """
    # If you're wondering, yes I used random Wikipedia article
    url = "https://pt.wikipedia.org/wiki/San_Antonio_la_Isla"
    images_url = scrapper.get_urls(url)

    # This value may vary in the future
    assert len(images_url) == 0
