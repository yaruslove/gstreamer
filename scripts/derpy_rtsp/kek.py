import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GObject, GstRtspServer
import sys

Gst.init(None)

def do_create_element(index, source):
    decode = f"filesrc location={source} ! decodebin ! videoconvert"
    encode = f"x264enc ! rtph264pay name=pay0"
    pipeline = f"{decode} ! {encode}"
    print(pipeline)
    return pipeline

#create server
class GstServer:
    def __init__(
        self,
        source: list[str],
        ip: str,
        port: str,
    ):
        self.__server = GstRtspServer.RTSPServer()
        self.__server.set_address(ip)
        self.__server.set_service(port)
        self.__mount_points = GstRtspServer.RTSPMountPoints.new()
        self.__sources = source
        self.__loop = GObject.MainLoop()
        self.__create_sources()
        self.__server.set_mount_points(self.__mount_points)
        # GObject.Object.unref(self.__mount_points) this bullhit is unsupported
        self.__server.connect('client-connected', self.__client_connected_callback, None)
        self.__client_counter = 0
        self.__server.attach(None)

    def __client_connected_callback(self, server, client, user_data):
        self.__client_counter += 1
        client.connect('closed', self.__client_closed_callback, None)
        if self.__client_counter == len(self.__sources):
            print('pooq')

    def __client_closed_callback(self, client, user_data):
        if self.__client_counter > 0:
            self.__client_counter -= 1
        else:
            sys.stderr.write("Server got more closed connections, than were opened. That's bullshit.\n")
        print('closed pooq')
        
    def __create_sources(self) -> None:
        for index, source in enumerate(self.__sources):
            factory = GstRtspServer.RTSPMediaFactory.new()
            factory.set_launch(do_create_element(index, source))
            factory.set_shared(True)
            self.__mount_points.add_factory(f'/kek{index}', factory)

    def run(self):
        try:
            self.__loop.run()
        except Exception as e:
            print(e)
            return
