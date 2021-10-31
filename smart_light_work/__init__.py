import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    return func.HttpResponse(
        json.dumps({
            "data": [
                {
                    "id": "Work",
                    "url": "https://ifttt-service.azurewebsites.net/ifttt/v1/actions/smart_light_work?command=on"
                }
            ]

        })
    )
