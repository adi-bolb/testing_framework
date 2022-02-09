from TestData.Builders.ActorBuilder import ActorBuilder


class ActorData:

    @staticmethod
    def default():
        return ActorData.relationship_manager()

    @staticmethod
    def analyst():
        return ActorBuilder().set_name('analyst').build()

    @staticmethod
    def branch_manager():
        return ActorBuilder().set_name('branch manager').build()

    @staticmethod
    def branch_manager_with_expired_credentials():
        return ActorBuilder().set_name('branch manager with expired credentials').build()

    @staticmethod
    def director():
        return ActorBuilder().set_name('director').build()

    @staticmethod
    def relationship_manager():
        return ActorBuilder().set_name("relationship manager").build()
