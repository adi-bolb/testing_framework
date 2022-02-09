from unittest import TestCase
from SystemUnderTestInterfaces.Login import Login
from TestData.EntitiesData.ActorData import ActorData


class ActorTests(TestCase):

    def setUp(self):
        self.login = Login()

    def test_analyst_actor_can_login(self):
        self.assertTrue(self.login.can_login_with_actor(ActorData.analyst()))

    def test_branch_manager_with_expired_credentials_cannot_login(self):
        self.assertFalse(self.login.can_login_with_actor(ActorData.branch_manager_with_expired_credentials()))
