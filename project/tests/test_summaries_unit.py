import json

import pytest


def test_create_summary(test_app, monkeypatch):
    pass


def test_create_summaries_invalid_json(test_app):
    response = test_app.post("/summaries/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "url"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.6/v/missing",
            }
        ]
    }

    # response = test_app.post("/summaries/", data=json.dumps({"url": "invalid://url"}))
    # assert response.status_code == 422
    # assert response.json()["detail"][0]["msg"] == "URL scheme should be 'http' or 'https'"


def test_read_summary(test_app, monkeypatch):
    pass


def test_read_summary_incorrect_id(test_app, monkeypatch):
    pass


def test_read_all_summaries(test_app, monkeypatch):
    pass


def test_remove_summary(test_app, monkeypatch):
    pass


def test_remove_summary_incorrect_id(test_app, monkeypatch):
    pass


def test_update_summary(test_app, monkeypatch):
    pass


@pytest.mark.parametrize(
    "summary_id, payload, status_code, detail",
    [
        [
            999,
            {"url": "https://foo.bar", "summary": "updated!"},
            404,
            "Summary not found",
        ],
        [
            0,
            {"url": "https://foo.bar", "summary": "updated!"},
            422,
            [
                {
                    "type": "greater_than",
                    "loc": ["path", "id"],
                    "msg": "Input should be greater than 0",
                    "input": "0",
                    "ctx": {"gt": 0},
                    "url": "https://errors.pydantic.dev/2.6/v/greater_than",
                }
            ],
        ],
        [
            1,
            {},
            422,
            [
                {
                    "type": "missing",
                    "loc": ["body", "url"],
                    "msg": "Field required",
                    "input": {},
                    "url": "https://errors.pydantic.dev/2.6/v/missing",
                },
                {
                    "type": "missing",
                    "loc": ["body", "summary"],
                    "msg": "Field required",
                    "input": {},
                    "url": "https://errors.pydantic.dev/2.6/v/missing",
                },
            ],
        ],
        [
            1,
            {"url": "https://foo.bar"},
            422,
            [
                {
                    "type": "missing",
                    "loc": ["body", "summary"],
                    "msg": "Field required",
                    "input": {"url": "https://foo.bar"},
                    "url": "https://errors.pydantic.dev/2.6/v/missing",
                }
            ],
        ],
    ],
)
def test_update_summary_invalid(test_app, monkeypatch, summary_id, payload, status_code, detail):
    pass


# def test_update_summary_invalid_url(test_app):
#     response = test_app.put(
#         f"/summaries/1/",
#         data=json.dumps({"url": "invalid://url", "summary": "updated!"}),
#     )
#     # assert response.status_code == 422
#     # assert response.json()["detail"][0]["msg"] == "URL scheme should be 'http' or 'https'"
