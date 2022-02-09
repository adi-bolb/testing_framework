class Login:
    def can_login_with_actor(self, actor):
        if actor.name == 'analyst':
            return True
        return False
