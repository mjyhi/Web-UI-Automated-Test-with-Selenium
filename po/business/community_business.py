"""社区业务流封装。"""

from ui_tests.po.pages.community_page import CommunityPage
from ui_tests.po.pages.new_post_page import NewPostPage


class CommunityBusiness:
    """社区相关业务流（发帖等）。"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def create_post(self, title: str, content: str) -> CommunityPage:
        """打开发帖页并发布帖子，返回社区页对象。"""
        new_post_page = NewPostPage(self.driver, self.base_url)
        new_post_page.open_new_post()
        new_post_page.create_post(title, content)
        return CommunityPage(self.driver, self.base_url)
