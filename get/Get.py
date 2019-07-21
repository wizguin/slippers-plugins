from world.dataHandler.pluginManager.Plugin import Plugin

class Get(Plugin):
    """
    A plugin that enables handling of get packets,
    found on the ~2007 client.
    """

    def __init__(self, users, rooms, packet):
        super(Get, self).__init__(users, rooms, packet)

    def get_inventory(self, data, user):
        user.send(["gi", "-1", "%".join(map(str, user.inventory))])
