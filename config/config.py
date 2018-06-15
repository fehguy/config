class Config(object):
    def __init__(self):
        self._values = {
            "cluster": "local",
            "service_type": "test-service",
            "instance_id": "abc123",
            "metrics.influx.host": "localhost",
            "metrics.influx.port": 8086,
            "metrics.influx.database": "mydb"
        }
        return
    
    def get_string(self, key):
        if key in self._values:
            return self._values[key]
        return None

    def get_int(self, key):
        if key in self._values:
            return int(self._values[key])
        return None
