
def http_connection_check(url,timeout):
    try:
        response=requests.get(url,timeout=timeout)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as httpErr:
        WarnLog("Http Error: {}".format(httpErr))
        return False
    except requests.exceptions.ConnectionError as connErr:
        WarnLog("Error Connecting: {}".format(connErr))
        return False
    except requests.exceptions.Timeout as timeOutErr:
        WarnLog("Timeout Error:{} ".format(timeOutErr))
        return False
    except requests.exceptions.RequestException as reqErr:
        WarnLog("Something Else:{}".format(reqErr))
        return False
    except Exception as err:
        WarnLog("Other error occurred:{}".format(err))
        return False