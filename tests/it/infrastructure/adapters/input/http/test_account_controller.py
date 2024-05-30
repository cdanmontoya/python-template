from starlette.testclient import TestClient

from tests.resources.factories.infrastructure.acl.dto.insert_account_request_dto_factory import (
    InsertAccountRequestDtoFactory,
)
from tests.resources.fixtures.application_fixture import application


def test_given_no_accounts_when_listing_all_should_return_empty_list(
    application: TestClient,
):
    response = application.get("/accounts")
    assert response.status_code == 200
    assert response.json()["accounts"] == []


def test_given_an_inserted_account_when_listing_all_should_return_a_non_empty_list(
    application: TestClient,
):
    request = InsertAccountRequestDtoFactory()

    response = application.post("/accounts", json=request.model_dump())
    list_response = application.get("/accounts")

    assert response.status_code == 200
    assert response.json()["contact_information"]["email"] == request.email
    assert len(list_response.json()["accounts"]) == 1


def test_given_an_existing_account_when_deleting_should_return_ok(
    application: TestClient,
):
    # TODO: This test should be independent
    response_list = application.get("/accounts")
    account_id = response_list.json()["accounts"][0]["id"]
    delete_response = application.delete(f"/accounts/{account_id}")
    response_list = application.get("/accounts")

    assert delete_response.status_code == 200
    assert len(response_list.json()["accounts"]) == 0