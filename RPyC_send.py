import rpyc
import random_string_microserivce as rsd


class PasswordMicroservice(rpyc.Service):
    """
    Defines a server that provides an images search functionality
    """

    def on_connect(self, conn):
        pass

    @staticmethod
    def exposed_get_password(length, upper, number, special):
        """
        Returns a random password based on parameters.
        """
        return rsd.generate_random_string(length, upper, number, special)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    my_server = ThreadedServer(PasswordMicroservice, port=18861)
    my_server.start()
