class Setting():
    """  存储设置的类  """

    def __init__(self):
        """ 初始化游戏设置 """

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 20

        self.bullet_speed = 10
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # 外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1表示向右移动 -1 表示向左
        self.fleet_direction = 1
