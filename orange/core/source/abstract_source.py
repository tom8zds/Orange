import abc

from orange.core.source.model import BangumiDetail, Season, SubscribeChannel, TimeTable, WeekDay,Bangumi

class AbstractSource(metaclass=abc.ABCMeta):
    
    @staticmethod
    @abc.abstractmethod
    def update() -> None:
        """
        check api token
        """

    @staticmethod
    @abc.abstractmethod
    def query_season(year:int, season:Season) -> TimeTable:
        """
        获取时间表
        """

    @staticmethod
    @abc.abstractmethod
    def get_bangumi_detail(self, bangumi_id:str) -> BangumiDetail:
        """
        获取番剧详情
        """

    @staticmethod
    @abc.abstractmethod
    def get_rss_detail(self, bangumi_id:str, provider:str) -> SubscribeChannel:
        """
        获取订阅rss详情
        """