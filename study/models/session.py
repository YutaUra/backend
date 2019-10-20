from study.base_session import BaseSession, BaseSessionManager


class StudySessionManager(BaseSessionManager):
    pass


class StudySession(BaseSession):
    objects = BaseSessionManager()
