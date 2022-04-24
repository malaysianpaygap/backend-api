from lambda_func.post_form import handler


def test_post_form_create_new_entry(
    lambda_post_new_salary_entry_event,
    db_connection,
):
    response = handler(
        event=lambda_post_new_salary_entry_event,
        context=None,
        connection=db_connection,
    )
    assert response["statusCode"] == 201
