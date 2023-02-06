import logging
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    myAppSettingValue = os.environ.get('myAppSetting')

    if myAppSettingValue:
        return func.HttpResponse(f"myAppSetting is set to {myAppSettingValue}", status_code=200)
    else:
        return func.HttpResponse("myAppSetting is not set", status_code=500)
