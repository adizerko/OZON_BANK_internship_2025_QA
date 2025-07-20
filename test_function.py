import pytest
from function import the_tallest_hero


@pytest.mark.parametrize("code",[500, 404, 403])
def test_api_failure(requests_mock, code):
    requests_mock.get("https://akabab.github.io/superhero-api/api/all.json", status_code = code)

    assert the_tallest_hero("Male", True) is None


@pytest.mark.parametrize("gender, work, expected_id", [
    ("Male", True, 681),
    ("Female", False, 42),
    ("Female", True, 284),
    ("Male", False, 728)
])
def test_the_tallest_hero_positive(gender, work, expected_id):
   hero = the_tallest_hero(gender, work)

   assert isinstance(hero, dict)
   assert hero["id"] == expected_id


@pytest.mark.parametrize("gender_male", [
    ("Мужчина"),
    ("M@le"),
    ("M ale"),
    (" Male"),
    ("Male "),
    ("Ma-le"),
    ("Ma1e"),
    (True),
    ("male"),
    ("MALE"),
    (""),
    (None)
])
def test_the_tallest_hero_negative_gender_male(gender_male):
    with pytest.raises(ValueError) as error_info:
        the_tallest_hero(gender_male, True)

    assert str(error_info.value) == "Пол должен быть Male или Female"


@pytest.mark.parametrize("gender_female", [
    ("Женщина"),
    ("Fem@le"),
    ("Fe male"),
    (" Female"),
    ("Female "),
    ("Fema-le"),
    ("Fema1e"),
    (True),
    ("female"),
    ("FEMALE"),
    (""),
    (None)
])
def test_the_tallest_hero_negative_gender_female(gender_female):
    with pytest.raises(ValueError) as exp_info:
        the_tallest_hero(gender_female, True)

    assert str(exp_info.value) == "Пол должен быть Male или Female"


@pytest.mark.parametrize("invalid_work", [
    ("False"),
    ("True"),
    (None),
    (""),
    (233),
    (0),
    (1),
    ("Yes")
])
def test_the_tallest_hero_negative_work(invalid_work):
    with pytest.raises(TypeError) as exp_info:
        the_tallest_hero("Female", invalid_work)

    assert str(exp_info.value) == "Аргумент work должен быть типа bool (True/False)"
