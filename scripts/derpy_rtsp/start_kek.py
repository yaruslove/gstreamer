from kek import GstServer

sources = ['event3_back.mp4', 'event3_front.mp4', 'event3_inside.mp4']

a = GstServer(sources, 'ip', 'port') # fill ip and port
a.run()

# "filesrc location=~/Videos/event_3/event3_back.mp4 ! decodebin ! videoconvert ! x264enc ! rtph264pay name=pay0 pt=96" "filesrc location=~/Videos/event_3/event3_front.mp4 ! decodebin ! videoconvert ! x264enc ! rtph264pay name=pay1 pt=96"