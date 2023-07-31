## RTSP Stream server


### 1. GstRtspServer
```  
server = GstRtspServer.RTSPServer()
```  
Этот объект прослушивает порт, создает подключенных к нему клиентов и управляет ими.


### 2. RTSPMountPoints  

Упрощенный код создания
```
### Создаем сервер
server = GstRtspServer.RTSPServer()
server.set_address(ip)
server.set_service(port)
mount_points = GstRtspServer.RTSPMountPoints.new()
sources = source
loop = GObject.MainLoop()
create_sources()
server.set_mount_points(mount_points)

### Создаем новый MediaFactory
factory = GstRtspServer.RTSPMediaFactory.new()

## String type file src
launch_file="filesrc location=home/my_documents/video.mp4 ! decodebin ! videoconvert ! x264enc ! rtph264pay name=pay0"

## Pass string to set launch
factory.set_launch(launch_file)

factory.set_shared(True)

### file_rtsp_stream.sdp - можно задать каким угодно
mount_points.add_factory(f'/file_rtsp_stream.sdp', factory)



### Run rtsp server

try:
    loop.run()
except Exception as e:
    print(e)
    return
```