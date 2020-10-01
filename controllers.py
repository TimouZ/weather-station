import abc

from flask import make_response, jsonify, request, url_for

from models import TemperatureLocal, TemperatureApi1, ApiLog, ErrorLog
import openweathermap_api

from app import app


class BaseController(abc.ABC):
    def __init__(self):
        self.request = request

    def call(self, *args, **kwargs):
        try:
            app.logger.info("Started {}".format({self.__class__.__name__}))
            return self._call(*args, **kwargs)
        except Exception as e:
            app.logger.exception("Error: {}".format(e))
            return make_response(str(e), getattr(e, "code", 500))

    @abc.abstractmethod
    def _call(self, *args, **kwargs):
        pass


class GetAllTemperatureData(BaseController):
    def _call(self):
        query = TemperatureLocal \
            .select(TemperatureLocal, TemperatureApi1) \
            .join(TemperatureApi1, on=(TemperatureLocal.date_time == TemperatureApi1.date_time), attr="temp_api")
        return query


class GetLocalTemperatureData(BaseController):
    def _call(self, *args, **kwargs):
        query = TemperatureLocal.select()
        return query


class GetRemoteAPITemperatureData(BaseController):
    def _call(self, *args, **kwargs):
        query = TemperatureApi1.select()
        return query


class UpdateLatest(BaseController):
    def _call(self, *args, **kwargs):
        openweathermap_api.API().update_db_data()


class ViewLogs(BaseController):
    def _call(self, log_type):
        app.logger.debug("log_type: ".format(log_type))
        page = int(self.request.args.get("page", 1))
        logs_map = {"api": ApiLog, "error": ErrorLog}

        if log_type not in logs_map:
            raise ValueError("Unknown log_type".format(log_type))

        log_model = logs_map[log_type]
        logs = log_model.select().paginate(page, 10).order_by(log_model.id.desc())
        return logs
