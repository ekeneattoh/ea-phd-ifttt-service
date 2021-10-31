import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    return func.HttpResponse(
        json.dumps({
            "data": [
                {
                    "status": "Light is ON",
                    "environment": "Home"
                }
            ]

        })
    )
