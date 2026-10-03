import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("StudentTable")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, default=str)
    }


def lambda_handler(event, context):

    method = event.get("requestContext", {}).get("http", {}).get("method")
    path_parameters = event.get("pathParameters") or {}
    student_id = path_parameters.get("id")

    try:

        # CREATE
        if method == "POST":

            body = json.loads(event.get("body") or "{}")

            student_id = body.get("id")
            name = body.get("name")
            age = body.get("age")
            course = body.get("course")
            email = body.get("email")

            if not all([student_id, name, age, course, email]):
                return response(
                    400,
                    {"message": "All fields are required"}
                )

            item = {
                "id": str(student_id),
                "name": name,
                "age": int(age),
                "course": course,
                "email": email
            }

            table.put_item(Item=item)

            return response(
                201,
                {
                    "message": "Student added successfully",
                    "student": item
                }
            )

        # READ ALL
        elif method == "GET" and not student_id:

            result = table.scan()

            return response(
                200,
                {
                    "students": result.get("Items", [])
                }
            )

        # READ ONE
        elif method == "GET" and student_id:

            result = table.get_item(
                Key={"id": student_id}
            )

            if "Item" not in result:
                return response(
                    404,
                    {"message": "Student not found"}
                )

            return response(
                200,
                result["Item"]
            )

        # UPDATE
        elif method == "PUT" and student_id:

            body = json.loads(event.get("body") or "{}")

            name = body.get("name")
            age = body.get("age")
            course = body.get("course")
            email = body.get("email")

            if not all([name, age, course, email]):
                return response(
                    "#n": "name"
                },
                ExpressionAttributeValues={
                    ":name": name,
                    ":age": int(age),
                    ":course": course,
                    ":email": email
                },
                ReturnValues="ALL_NEW"
            )

            return response(
                200,
                {
                    "message": "Student updated successfully",
                    "student": result["Attributes"]
                }
            )

        # DELETE
        elif method == "DELETE" and student_id:

            table.delete_item(
                Key={"id": student_id}
            )

            return response(
                200,
                {
                    "message": "Student deleted successfully",
                    "id": student_id
                }
            )

        else:

            return response(
                400,
                {"message": "Invalid request"}
            )

    except ClientError as e:

        return response(
            500,
            {
                "message": "DynamoDB error",
                "error": str(e)
            }
        )

    except Exception as e:

        return response(
            500,
            {
                "message": "Internal server error",
                "error": str(e)
            }
        )

