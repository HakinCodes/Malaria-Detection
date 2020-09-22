def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200


def test_form(app, client):
    res = client.get("/form")
    assert res.status_code == 200


def test_result(app, client):
    res = client.get("/result")
    assert res.status_code == 200
