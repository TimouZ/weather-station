from models import TemperatureLocal, TemperatureApi1


def get_all_temperature_data():
    query = TemperatureLocal \
        .select(TemperatureLocal, TemperatureApi1) \
        .join(TemperatureApi1, on=(TemperatureLocal.date_time == TemperatureApi1.date_time), attr="temp_api")
    for query_data in query:
        print(query_data)
        print(query_data.date_time, query_data.temperature, query_data.temperature_min, query_data.temperature_max,
              query_data.temp_api.temperature, query_data.temp_api.temperature_min, query_data.temp_api.temperature_max)
    return query


def get_local_temperature_data():
    query = TemperatureLocal.select()
    return query


def get_remote_api_temperature_data():
    query = TemperatureApi1.select()
    return query
