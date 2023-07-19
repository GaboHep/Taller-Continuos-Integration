import Code


def test_validate_quantity_positive():
    out_1 = Code.validate_quantity("5")
    assert (out_1 == 5)


def test_validate_quantity_negative():
    out_2 = Code.validate_quantity("-5")
    assert (out_2 == None)


def test_calculate_cost_empty():
    out = Code.calculate_cost({})
    assert (out == 0)


def test_calculate_cost_over_100_quantity():
    out = Code.calculate_cost({"Chaulafan": 101})
    assert (out == -1)


def test_calculate_cost_over_5_quantity():
    out = Code.calculate_cost({"Chaulafan": 6})
    assert (out == 44)


def test_calculate_cost_over_10_quantity():
    out = Code.calculate_cost({"Lasagna": 11})
    assert (out == 85)


def test_calculate_cost_over_cost_over_50():
    out = Code.calculate_cost({"Lasagna": 7})
    assert (out == 65)


def test_calculate_cost_over_cost_over_100():
    out = Code.calculate_cost({"Encebollado": 11})
    assert (out == 83)


def test_calculate_cost_special_meal():
    out = Code.calculate_cost({"Restaurant Specials": 11})
    assert (out == 92)
