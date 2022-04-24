import psycopg2.extras


def handler(event, context, connection):
    cursor = connection.cursor()
    query_statement = """INSERT INTO raw
    (submission_timestamp,age,race,gender,nationality,edu_qualification,job_title,years_exp,num_jobs,in_malaysia,is_remote,state,company_type,industry,industry_other,job_specialisation,job_other,avg_work_hours,avg_workdays_week,gross_monthly_salary,starting_salary,happy_rating,job_satisfaction_rating,thoughts,email,code)
    VALUES %s"""
    try:
        psycopg2.extras.execute_values(
            cursor,
            query_statement,
            [
                (
                    event["queryStringParameters"]["submission_timestamp"],
                    int(event["queryStringParameters"]["age"]),
                    event["queryStringParameters"]["race"],
                    event["queryStringParameters"]["gender"],
                    event["queryStringParameters"]["nationality"],
                    event["queryStringParameters"]["edu_qualification"],
                    event["queryStringParameters"]["job_title"],
                    event["queryStringParameters"]["years_exp"],
                    int(event["queryStringParameters"]["num_jobs"]),
                    event["queryStringParameters"]["in_malaysia"],
                    event["queryStringParameters"]["is_remote"],
                    event["queryStringParameters"]["state"],
                    event["queryStringParameters"]["company_type"],
                    event["queryStringParameters"]["industry"],
                    event["queryStringParameters"]["industry_other"],
                    event["queryStringParameters"]["job_specialisation"],
                    event["queryStringParameters"]["job_other"],
                    float(event["queryStringParameters"]["avg_work_hours"]),
                    float(event["queryStringParameters"]["avg_workdays_week"]),
                    float(event["queryStringParameters"]["gross_monthly_salary"]),
                    float(event["queryStringParameters"]["starting_salary"]),
                    int(event["queryStringParameters"]["happy_rating"]),
                    int(event["queryStringParameters"]["job_satisfaction_rating"]),
                    event["queryStringParameters"]["thoughts"],
                    event["queryStringParameters"]["email"],
                    event["queryStringParameters"]["code"],
                )
            ],
        )
        connection.commit()
        cursor.close()
        return {
            "statusCode": 201,
            "body": {
                "message": "User successfully added!",
            },
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": {
                "message": "Error inserting user into table:\n {e}",
            },
        }
    finally:
        if connection is not None:
            connection.close()
