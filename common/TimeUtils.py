from datetime import datetime, timezone


def getTimeStr():
    return datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')