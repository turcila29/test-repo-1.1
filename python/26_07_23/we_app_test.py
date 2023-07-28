from web_app import name_gen, First_name, Last_name


def test_name_test():
    assert name_gen().split(" ")[0] in First_name 
    assert name_gen().split(" ")[1] in Last_name